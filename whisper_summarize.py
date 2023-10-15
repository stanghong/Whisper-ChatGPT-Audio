
import openai
#https://medium.com/gitconnected/using-the-whisper-api-to-transcribe-audio-files-45fb36d1aa1b

import whisper
# brew install ffmpeg # you may need to install

openai.api_key = 'YOURAPIKEY'
model = whisper.load_model("base")

file_path = 'MA1.m4a'

def transcribe_audio(model, file_path):
    transcript = model.transcribe(file_path)
    return transcript['text']

def CustomChatGPT(user_input):
    messages = [{"role": "system", "content": "You are an office administer, summarize the text in key points"}]
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    return ChatGPT_reply


transcription = transcribe_audio(model, file_path)
summary = CustomChatGPT(transcription)
print(summary)



