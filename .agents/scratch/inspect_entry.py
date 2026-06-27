from youtube_transcript_api import YouTubeTranscriptApi
api = YouTubeTranscriptApi()
t_list = api.list('Q46OLxFshAQ')
t = next(iter(t_list))
data = t.fetch()
print("Type of data:", type(data))
print("Type of first element:", type(data[0]))
print("Attributes of first element:", dir(data[0]))
try:
    print("Keys if dict:", data[0].keys())
except Exception as e:
    print("Not a dict or no keys():", e)
print("Representing first element:", repr(data[0]))
