document.addEventListener('DOMContentLoaded', () => {
    // --- DOM Elements ---
    const leadForm = document.getElementById('lead-form');
    const submitBtn = document.getElementById('submit-btn');
    const settingsToggle = document.getElementById('settings-toggle');
    const settingsModal = document.getElementById('settings-modal');
    const settingsClose = document.getElementById('settings-close');
    const webhookSave = document.getElementById('webhook-save');
    const webhookUrlInput = document.getElementById('webhook-url');
    const toastContainer = document.getElementById('toast-container');

    // --- Local Storage Keys ---
    const WEBHOOK_KEY = 'apex_n8n_webhook_url';

    // --- Initialize Webhook URL ---
    const storedWebhook = localStorage.getItem(WEBHOOK_KEY);
    if (storedWebhook) {
        webhookUrlInput.value = storedWebhook;
    }

    // --- Toast System ---
    function showToast(message, type = 'info', duration = 5000) {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        let iconHtml = '<i class="fa-solid fa-circle-info toast-icon"></i>';
        if (type === 'success') {
            iconHtml = '<i class="fa-solid fa-circle-check toast-icon"></i>';
        } else if (type === 'error') {
            iconHtml = '<i class="fa-solid fa-triangle-exclamation toast-icon"></i>';
        }

        toast.innerHTML = `
            ${iconHtml}
            <div class="toast-content">${message}</div>
        `;
        
        toastContainer.appendChild(toast);

        // Slide out and remove toast after duration
        setTimeout(() => {
            toast.style.transform = 'translateX(120%)';
            toast.style.opacity = '0';
            setTimeout(() => {
                toast.remove();
            }, 300);
        }, duration);
    }

    // --- Modal Management ---
    settingsToggle.addEventListener('click', () => {
        settingsModal.classList.add('active');
    });

    settingsClose.addEventListener('click', () => {
        settingsModal.classList.remove('active');
    });

    settingsModal.addEventListener('click', (e) => {
        if (e.target === settingsModal) {
            settingsModal.classList.remove('active');
        }
    });

    // Save Webhook configuration
    webhookSave.addEventListener('click', () => {
        const url = webhookUrlInput.value.trim();
        if (!url) {
            localStorage.removeItem(WEBHOOK_KEY);
            showToast('Webhook URL cleared.', 'info');
            settingsModal.classList.remove('active');
            return;
        }

        try {
            new URL(url); // validate structure
            localStorage.setItem(WEBHOOK_KEY, url);
            showToast('n8n Webhook URL updated successfully!', 'success');
            settingsModal.classList.remove('active');
        } catch (_) {
            showToast('Please enter a valid URL (including http:// or https://)', 'error');
        }
    });

    // --- Form Validation Helpers ---
    function validateField(input) {
        const group = input.closest('.input-group');
        let isValid = true;

        if (input.required) {
            if (!input.value.trim()) {
                isValid = false;
            }
        }

        // Email validation
        if (isValid && input.type === 'email' && input.value) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            isValid = emailPattern.test(input.value.trim());
        }

        // Phone number validation (extremely basic check for digits/plus sign)
        if (isValid && input.type === 'tel' && input.value) {
            // strip spacing and characters
            const digits = input.value.replace(/\D/g, '');
            // must have at least 10 digits
            isValid = digits.length >= 10;
        }

        if (isValid) {
            group.classList.remove('invalid');
        } else {
            group.classList.add('invalid');
        }

        return isValid;
    }

    // Event listeners for real-time validation
    const inputs = leadForm.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', () => validateField(input));
        input.addEventListener('change', () => validateField(input));
    });

    // --- Form Submit Handler ---
    leadForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // 1. Check all validations
        let formIsValid = true;
        inputs.forEach(input => {
            if (!validateField(input)) {
                formIsValid = false;
            }
        });

        if (!formIsValid) {
            showToast('Please correct the highlighted fields before submitting.', 'error');
            return;
        }

        // 2. Check for configured Webhook URL
        const webhookUrl = localStorage.getItem(WEBHOOK_KEY);
        if (!webhookUrl) {
            showToast('Please configure your n8n Webhook URL in the settings panel.', 'info');
            settingsModal.classList.add('active');
            return;
        }

        // 3. Collect form data
        const formData = {
            customer_name: document.getElementById('customer_name').value.trim(),
            customer_phone: document.getElementById('customer_phone').value.trim(),
            customer_email: document.getElementById('customer_email').value.trim(),
            service_type: document.getElementById('service_type').value,
            service_location: document.getElementById('service_location').value.trim(),
            request_details: document.getElementById('request_details').value.trim()
        };

        // 4. Send POST request
        submitBtn.classList.add('loading');

        try {
            const response = await fetch(webhookUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                mode: 'cors', // Enable CORS
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                showToast('Lead submitted! Outbound qualification call starting shortly...', 'success', 6000);
                leadForm.reset();
                // Clear validation classes
                inputs.forEach(input => {
                    input.closest('.input-group').classList.remove('invalid');
                });
            } else {
                const text = await response.text();
                showToast(`Server returned error: ${response.status} ${text || 'Unknown Error'}`, 'error');
            }
        } catch (error) {
            console.error('Submission error:', error);
            showToast('Could not reach n8n. Check your URL configuration or ensure n8n is running.', 'error');
        } finally {
            submitBtn.classList.remove('loading');
        }
    });
});
