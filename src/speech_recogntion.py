import os
import utils_mic
import whisper

def speechRecogntion(audioName='audio_test.wav', directoryName='audio_folder/'):
    # Obtém uma lista de todos os arquivos no diretório
    audioFile = os.path.join(directoryName, audioName)
   
    # Models
    # tiny - base - small - medium
    model = whisper.load_model("small")
    
    # transcribe audio
    text = whisper.transcribe(model=model,audio=audioFile)
    print(text['text'])


utils_mic.record_audio(saveAudioOn=True, durantion=5)
speechRecogntion()