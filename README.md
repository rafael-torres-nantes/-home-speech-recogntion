# 🎙️ AraraBots@AtHome-SpeechRecogntion

Seja bem-vindo !!! O __Repositório AtHome-SpeechRecognition-Whisper__ documenta o projeto de reconhecimento de fala em casa utilizando o modelo Whisper. Aqui você encontrará informações detalhadas sobre o projeto, incluindo:

## 📌 Navegação

- [📝 Sobre o Whisper e SpeechRecognition](#introdução)
- [📁 Estrutura do Repositório](#estrutura-do-repositorio)
- [💻 Desenvolvimento](#desenvolvimento)
  - [🔧 Ferramentas e tecnologias utilizadas](#ferramentas-e-tecnologias-utilizadas)

 ## 📝Sobre o Whisper e SpeechRecognition

O projeto AtHome-SpeechRecognition-Whisper visa desenvolver um sistema de reconhecimento de fala em casa utilizando o modelo Whisper de última geração. O sistema será capaz de:

- __Transcrever áudio em tempo real:__ O sistema transcreverá áudio de conversas, entrevistas, palestras e outros eventos em tempo real, com alta precisão.
- __Controlar dispositivos domésticos inteligentes:__ O sistema poderá ser utilizado para controlar dispositivos domésticos inteligentes por voz, como luzes, TVs, ar-condicionado e muito mais.
- __Realizar tarefas automatizadas:__ O sistema poderá ser utilizado para realizar tarefas automatizadas, como agendar compromissos, enviar mensagens de texto, tocar música e muito mais.

## 📁 Estrutura do Repositório

Neste repositório, você encontrará 3 pastas, sendo elas:
- 3 pastas com os temas da trilha de Métodos Ágeis;
- 1 arquivo README com o detalhes sobre as informações da trilha;

Cada pasta contém os arquivos produzidos durante o processo de aprendiza, podendo incluir:
- __assets__ : Pasta que contém imagens e documentações do processo de aprendizado;
- __src__ : Pasta que contém os códigos utilizados durante os estudos;
- -  __tests__: Contém os testes do projeto.
- __README.md__ : Arquivo de texto que contém detalhes sobre o projeto;

## 💻 Desenvolvimento

### 🔧 Ferramentas e tecnologias utilizadas

[OpenAi](https://github.com/openai/whisper)
We used Python 3.9.9 and PyTorch 1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.8-3.11 and recent PyTorch versions. The codebase also depends on a few Python packages, most notably OpenAI's tiktoken for their fast tokenizer implementation. You can download and install (or update to) the latest release of Whisper with the following command:
```
pip install -U openai-whisper
```

It also requires the command-line tool ffmpeg to be installed on your system, which is available from most package managers:
```
sudo apt update && sudo apt install ffmpeg
```

You may need rust installed as well, in case tiktoken does not provide a pre-built wheel for your platform.
```
pip install setuptools-rust
```

# Install Sounddevice

```
pip install sounddevice
```

(SoundDevice Documentation)[https://readthedocs.org/projects/python-sounddevice/downloads/pdf/latest/]
```
import sounddevice as sd
```

# Install SoundFile

```
pip install soundfile
```
