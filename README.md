# 🎙️ Study - Speech Recognition using Whisper

Seja bem-vindo! O __Repositório Speech Recognition - Whisper__ documenta o projeto de reconhecimento de fala em casa utilizando o modelo Whisper. Aqui você encontrará informações detalhadas sobre o projeto, incluindo:

## 📌 Navegação

- [📝 Sobre o Whisper e SpeechRecognition](#-sobre-o-whisper-e-speechrecognition)
- [📁 Estrutura do Repositório](#-estrutura-do-repositório)
- [💻 Desenvolvimento](#-desenvolvimento)
  - [🔧 Ferramentas e tecnologias utilizadas](#-ferramentas-e-tecnologias-utilizadas)
  - [📥 Instalação](#-instalação)
  - [🚀 Uso](#-uso)

## 📝 Sobre o Whisper e SpeechRecognition

O projeto Speech Recognition - Whisper visa desenvolver um sistema de reconhecimento de fala em casa utilizando o modelo Whisper de última geração. O sistema será capaz de:

- __Transcrever áudio em tempo real:__ O sistema transcreverá áudio de conversas, entrevistas, palestras e outros eventos em tempo real, com alta precisão.
- __Controlar dispositivos domésticos inteligentes:__ O sistema poderá ser utilizado para controlar dispositivos domésticos inteligentes por voz, como luzes, TVs, ar-condicionado e muito mais.
- __Realizar tarefas automatizadas:__ O sistema poderá ser utilizado para realizar tarefas automatizadas, como agendar compromissos, enviar mensagens de texto, tocar música e muito mais.

### Sobre o Whisper

Whisper é um modelo de reconhecimento de fala desenvolvido pela OpenAI. Ele é capaz de transcrever e traduzir áudio com alta precisão. O modelo é treinado em uma grande quantidade de dados de áudio e texto, o que permite que ele funcione bem em uma variedade de idiomas e sotaques.

## 📁 Estrutura do Repositório

Neste repositório, você encontrará as seguintes pastas e arquivos:

- `audio_folder/`: Pasta onde os arquivos de áudio gravados serão armazenados.
- `devices/`: Contém o arquivo `mic_devices.py` que lida com dispositivos de microfone.
- `env/`: Scripts de instalação para diferentes sistemas operacionais.
  - `install_whisper_ubuntu.sh`
  - `install_whisper_windows.sh`
- `models/`: Contém os modelos Whisper.
  - `tiny.pt`
- `speech_to_text/`: Contém o arquivo `speech_recogntion.py` que lida com a transcrição de áudio.
- `main.py`: Script principal para executar o projeto.
- `.gitignore`: Arquivo para ignorar arquivos e pastas específicas no controle de versão.
- `LICENSE`: Licença do projeto.
- `README.md`: Este arquivo.

## 💻 Desenvolvimento

### 🔧 Ferramentas e tecnologias utilizadas

- [OpenAI Whisper](https://github.com/openai/whisper)
- Python 3.11
- PyTorch
- Scipy
- Soundfile
- Sounddevice
- FFmpeg
- Setuptools-rust

### 📥 Instalação

Para instalar as dependências do projeto, execute os seguintes comandos:

#### Ubuntu

```sh
# OBS: Este script deve ser executado no Python 3.11.9

# Instala a biblioteca scipy
pip install scipy

# Instala a biblioteca soundfile
pip install soundfile

# Instala a biblioteca sounddevice
pip install sounddevice

# Atualiza a biblioteca openai-whisper para a versão mais recente
pip install -U openai-whisper

# Atualiza a lista de pacotes e instala o ffmpeg
sudo apt update && sudo apt install ffmpeg

# Instala a biblioteca setuptools-rust
pip install setuptools-rust
```

#### Windows

```sh
# OBS: Este script deve ser executado no Python 3.11.9

# Instale Chocolatey no PowerShell do Windows
# https://chocolatey.org/install#individual

# Instala a biblioteca scipy
pip install scipy

# Instala a biblioteca soundfile
pip install soundfile

# Instala a biblioteca sounddevice
pip install sounddevice

# Utiliza o Chocolatey para instalar o ffmpeg
choco install ffmpeg

# Atualiza a biblioteca openai-whisper para a versão mais recente
pip install -U openai-whisper
```

### 🚀 Uso

Para utilizar o projeto, siga os passos abaixo:

1. Clone o repositório.
2. Instale as dependências conforme descrito acima.
3. Execute o script `main.py` para iniciar a transcrição de áudio.

```bash
# Clone o repositório
git clone https://github.com/rafael-torres-nantes/AtHome-SpeechRecogntion-Whisper.git

# Navegue até o diretório do projeto
cd AtHome-SpeechRecogntion-Whisper

# Instale as dependências conforme descrito acima
# ...

# Execute o script principal
python main.py
```

#### Exemplo de Código

Aqui está um exemplo de como utilizar o projeto em Python:

```python
import os
from devices.mic_devices import AudioRecording
from speech_to_text.speech_recogntion import SpeechToText

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma instância da classe SpeechToText
    stt = SpeechToText()

    # Carrega o modelo desejado (exemplo: 'tiny')
    stt.load_model(model_name="tiny")

    # Realiza a transcrição do áudio especificado
    try:
        audio_path = "audio_folder/audio_test.wav"

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
```
