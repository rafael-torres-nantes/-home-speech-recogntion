import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import os

def record_audio(saveAudioOn=False, durantion=10 , audioName='audio_folder/input_audio.wav'):
     
    '''
     Utilize o comando para acessar os microfones e os canais disponíveis:
     ---------------------------------------------------------------------
     python3 -m sounddevice
     ---------------------------------------------------------------------
     '''

    sample_frequence = 44100
    microfone_channel = 6
    duration = durantion

    print("Aguarde !! Áudio está sendo gravado...")
    recording = sd.rec(int(duration * sample_frequence), samplerate=sample_frequence, channels=microfone_channel)
    sd.wait()

    if saveAudioOn == True:
        write(audioName, sample_frequence, recording)

    print("Áudio gravado com sucesso!")

def reproduzir_audio(audioName='input_audio.wav', directoryName='audio_folder/',sample_frequence=44100):
    # Obtém uma lista de todos os arquivos no diretório
    file = os.path.join(directoryName, audioName)

    audioFile, sample_frequence = sf.read(file)
    sd.play(audioFile, sample_frequence)
    sd.wait()

def deletar_arquivos(directoryName='audio_folder/'):
    # Obtém uma lista de todos os arquivos no diretório
    files = os.listdir(directoryName)

    print(files)
    # Exclui todos os arquivos
    for file in files:
        if os.path.splitext(file)[1] == ".wav":
            os.remove(os.path.join(directoryName, file))

    print("Arquivos deletados com sucesso!")


# saveAudioOn = True
# record_audio(saveAudioOn)
# reproduzir_audio()