# pylint: disable=W,C,R
# Imports the Google Cloud client library
#from google.cloud import speech
from google.cloud import speech_v1p1beta1 as speech
import json

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://sazae-san/1.mp3" # "gs://sazae-san/testing_short.mp3"

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=44100,
    language_code="ja-JP", # ja-JP # en-US
    #enable_speaker_diarization=True,
    enable_word_time_offsets=True,
    #diarization_speaker_count=2,
    enable_word_confidence=True,
)

operation = client.long_running_recognize(config=config, audio=audio)

response = operation.result(timeout=3000)

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.

transcript = {"parts" : []}
transcript95 = {"parts" : []}

for result in response.results:
    part = {}
    part["text"] = result.alternatives[0].transcript
    part["confidence"] = result.alternatives[0].confidence
    part["words"] = []
    
    part95 = {}
    part95["text"] = result.alternatives[0].transcript
    part95["confidence"] = result.alternatives[0].confidence
    part95["words"] = []
    
    words_info = result.alternatives[0].words
    for word_info in words_info:
        part["words"].append({"word" : word_info.word, "confidence" : word_info.confidence, "start_time" : str(word_info.start_time), "end_time" : str(word_info.end_time)})
        if word_info.confidence > 0.95:
            part95["words"].append({"word" : word_info.word, "confidence" : word_info.confidence, "start_time" : str(word_info.start_time), "end_time" : str(word_info.end_time)})
        #print(u"word: '{}', confidence: '{}', start_time: '{}', 'end_time: '{}'".format(word_info.word, word_info.confidence, word_info.start_time, word_info.end_time))
    
    transcript["parts"].append(part)
    transcript95["parts"].append(part95)

with open("transcript.json", "w") as j:
	json.dump(transcript, j, ensure_ascii=False)
 
with open("transcript_95.json", "w") as j:
	json.dump(transcript95, j, ensure_ascii=False)
