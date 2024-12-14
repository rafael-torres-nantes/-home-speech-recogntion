import os
import soundfile as sf
import sounddevice as sd
from scipy.io.wavfile import write

class AudioRecording:
    
    def __init__(self, sample_frequence=44100, microfone_channel=1, directoryName='audio_folder/'):
        """
        Construtor da classe AudioUtils que inicializa os parâmetros de frequência de 
        amostragem, canal do microfone e diretório de armazenamento dos arquivos de áudio.

        Parâmetros:
        - sample_frequence (int): Frequência de amostragem do áudio em Hz (padrão: 44100).
        - microfone_channel (int): Número de canais do microfone (padrão: 1).
        - directoryName (str): Nome do diretório onde os áudios serão armazenados (padrão: 'audio_folder/').
        """
        self.sample_frequence = sample_frequence
        self.microfone_channel = microfone_channel
        self.directoryName = directoryName

    def record_audio(self, saveAudioOn=False, duration=10, audioName='input_audio.wav'):
        """
        Função para gravar áudio usando o microfone.

        Parâmetros:
        - saveAudioOn (bool): Indica se o áudio gravado deve ser salvo em arquivo (padrão: False).
        - duration (int): Duração da gravação em segundos (padrão: 10).
        - audioName (str): Caminho completo do arquivo onde o áudio será salvo (padrão: 'audio_folder/input_audio.wav').

        Uso: Certifique-se de que o dispositivo de entrada esteja configurado corretamente.
        """
        print("Aguarde! Áudio está sendo gravado...")
        # Grava o áudio com a frequência de amostragem e o número de canais definidos
        recording = sd.rec(int(duration * self.sample_frequence), samplerate=self.sample_frequence, channels=self.microfone_channel)
        sd.wait()  # Aguarda o término da gravação

        # Monta o caminho completo do arquivo no diretório
        audioPath = os.path.join(self.directoryName, audioName)

        if saveAudioOn:
            write(audioPath, self.sample_frequence, recording)  # Salva o áudio em um arquivo

        print("Áudio gravado com sucesso!")

    def play_audio(self, audioName='input_audio.wav'):
        """
        Função para reproduzir o áudio gravado.

        Parâmetros:
        - audioName (str): Nome do arquivo de áudio a ser reproduzido (padrão: 'input_audio.wav').
        """
        # Monta o caminho completo do arquivo no diretório
        file = os.path.join(self.directoryName, audioName)

        # Lê o arquivo de áudio e sua frequência de amostragem
        audioFile, sample_frequence = sf.read(file)
        sd.play(audioFile, sample_frequence)  # Reproduz o áudio
        sd.wait()  # Aguarda o término da reprodução

    def delete_files(self):
        """
        Função para deletar todos os arquivos .wav do diretório especificado.
        """
        # Lista todos os arquivos no diretório
        files = os.listdir(self.directoryName)
        print("Arquivos no diretório:", files)

        # Remove apenas os arquivos com extensão .wav
        for file in files:
            if os.path.splitext(file)[1] == ".wav":
                os.remove(os.path.join(self.directoryName, file))

        print("Arquivos deletados com sucesso!")
    
    def list_available_channels(self):
        """
        Função que lista os dispositivos de entrada (microfones) disponíveis no sistema.
        """
        print(sd.query_devices())  # Exibe os dispositivos disponíveis

if __name__ == "__main__":
    # Instancia a classe com os parâmetros padrão
    audio_utils = AudioRecording()

    # Lista os dispositivos de entrada disponíveis
    audio_utils.list_available_channels()

    # Configura a gravação de áudio e salva o arquivo gravado
    saveAudioOn = True
    audio_utils.record_audio(saveAudioOn)

    # Reproduz o áudio gravado
    audio_utils.play_audio()
