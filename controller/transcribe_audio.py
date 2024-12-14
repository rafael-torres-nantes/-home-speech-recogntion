import os
from devices.mic_devices import AudioRecording
from speech_to_text.speech_recogntion import SpeechToText


def generate_audio_file(rec_duration=5):
    # Instancia a classe com os parâmetros padrão
    audio_utils = AudioRecording()

    # Lista os dispositivos de entrada disponíveis
    audio_utils.list_available_channels()

    # Configura a gravação de áudio e salva o arquivo gravado
    audio_utils.record_audio(saveAudioOn=True, duration=rec_duration)

    # Reproduz o áudio gravado
    audio_utils.play_audio()


def run_transcribe(audio_path="audio_folder/input_audio.wav"):
    # Instancia a classe com os parâmetros padrão
    stt = SpeechToText()

    # Carrega o modelo desejado (exemplo: 'tiny')
    stt.load_model(model_name="tiny")

    # Realiza a transcrição do áudio especificado
    try:
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"O arquivo de áudio '{audio_path}' não foi encontrado.")
        
        transcribed_text = stt.transcribe_audio(audio_file=audio_path, 
                                                language="pt", 
                                                task="transcribe", 
                                                verbose=True)

        # Detecta o idioma do áudio
        detected_language = stt.detect_language(audio_file=audio_path)

        # Realiza a decodificação com opções avançadas
        decoded_text = stt.decode_audio(audio_file=audio_path)

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    # Gera um arquivo de áudio
    generate_audio_file()

    # Realiza a transcrição
    run_transcribe()