import os
import whisper

class SpeechToText:
    """
    Classe para realizar a transcrição de áudio para texto usando o modelo Whisper.
    """

    def __init__(self):
        """
        Inicializa a classe SpeechToText.
        """
        self.model = None  # O modelo Whisper será carregado quando necessário

    def load_model(self, model_name="small", model_directory="models"):
        """
        Carrega o modelo Whisper especificado e o salva em um diretório específico.

        Parâmetros:
        - model_name (str): Nome do modelo a ser carregado. 
          Opções incluem: 'tiny', 'base', 'small', 'medium', 'large'.
        - model_directory (str): Diretório onde o modelo será salvo.
        """
        # Verifica se o diretório existe, caso contrário, cria
        if not os.path.exists(model_directory):
            os.makedirs(model_directory)
        
        print(f"Carregando o modelo Whisper: {model_name} na pasta '{model_directory}'...")
        
        # Carrega o modelo, especificando o diretório de cache
        self.model = whisper.load_model(model_name, download_root=model_directory)
        
        print("Modelo carregado com sucesso.")

    def transcribe_audio(self, audio_file='audio_test.wav', language=None, task="transcribe", verbose=True):
        """
        Transcreve ou traduz um arquivo de áudio usando o modelo Whisper.

        Parâmetros:
        - audio_file (str): Nome do arquivo de áudio a ser transcrito.
        - language (str): Código do idioma do áudio (ex: 'en' para inglês, 'pt' para português). 
          Se None, o modelo tentará detectar automaticamente.
        - task (str): Tarefa a ser realizada. 
          - 'transcribe' para transcrição no idioma original.
          - 'translate' para traduzir para o inglês.
        - verbose (bool): Exibe informações detalhadas durante o processo se True.

        Retorna:
        - str: Texto transcrito ou traduzido.
        """
        # Verifica se o modelo foi carregado
        if self.model is None:
            raise ValueError("Modelo Whisper não carregado. Use 'load_model()' antes de transcrever.")

        # Check o caminho completo para o arquivo de áudio
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"O arquivo de áudio '{audio_file}' não foi encontrado.")

        # Transcrição do áudio
        print(f"Transcrevendo o arquivo: {audio_file}...")
        result = self.model.transcribe(audio=audio_file, 
                                       language=language, 
                                       task=task, 
                                       verbose=verbose,
                                       fp16=False)

        transcribed_text = result['text'].encode()
        print("Transcrição concluída.")
        print("Texto transcrito:")
        print(transcribed_text)

        return transcribed_text

    def detect_language(self, audio_file='audio_test.wav'):
        """
        Detecta o idioma predominante no áudio fornecido.

        Parâmetros:
        - audio_file (str): Nome do arquivo de áudio.

        Retorna:
        - str: Idioma detectado.
        """
        if self.model is None:
            raise ValueError("Modelo Whisper não carregado. Use 'load_model()' antes de detectar o idioma.")

        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"O arquivo de áudio '{audio_file}' não foi encontrado.")

        # Carrega e processa o áudio
        audio = whisper.load_audio(audio_file)
        audio = whisper.pad_or_trim(audio)

        # Gera o espectrograma log-Mel
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

        # Detecta o idioma
        _, probs = self.model.detect_language(mel)
        detected_language = max(probs, key=probs.get)
        print(f"Idioma detectado: {detected_language}")

        return detected_language

    def decode_audio(self, audio_file='audio_test.wav',decoding_options=None):
        """
        Decodifica o áudio usando opções avançadas de decodificação.

        Parâmetros:
        - audio_file (str): Nome do arquivo de áudio.
        - decoding_options (whisper.DecodingOptions): Opções de decodificação do Whisper. 
          Se None, serão usadas as opções padrão.

        Retorna:
        - str: Texto decodificado.
        """
        if self.model is None:
            raise ValueError("Modelo Whisper não carregado. Use 'load_model()' antes de decodificar.")

        # Verifica se o arquivo de áudio existe
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"O arquivo de áudio '{audio_file}' não foi encontrado.")

        # Carrega e processa o áudio
        audio = whisper.load_audio(audio_file)
        audio = whisper.pad_or_trim(audio)

        # Gera o espectrograma log-Mel
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

        # Define opções de decodificação
        if decoding_options is None:
            decoding_options = whisper.DecodingOptions()

        # Decodifica o áudio
        result = whisper.decode(self.model, mel, decoding_options)
        print("Decodificação concluída.")
        print("Texto decodificado:")
        print(result.text)

        return result.text

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma instância da classe SpeechToText
    stt = SpeechToText()

    # Carrega o modelo desejado (exemplo: 'tiny')
    stt.load_model(model_name="tiny")

    # Realiza a transcrição do áudio especificado
    try:
        transcribed_text = stt.transcribe_audio(audio_file="audio_test.wav", 
                                               language="pt", 
                                               task="transcribe", 
                                               verbose=True)

        # Detecta o idioma do áudio
        detected_language = stt.detect_language(audio_file="audio_test.wav")

        # Realiza a decodificação com opções avançadas
        decoded_text = stt.decode_audio(audio_file="audio_test.wav")

    except Exception as e:
        print(f"Erro: {e}")