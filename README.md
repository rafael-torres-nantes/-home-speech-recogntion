# 🎙️ Study - Speech Recognition using Whisper

## 👨‍💻 Projeto desenvolvido por: 
[Rafael Torres Nantes](https://github.com/rafael-torres-nantes)

## Índice

* [📚 Contextualização do projeto](#-contextualização-do-projeto)
* [🛠️ Tecnologias/Ferramentas utilizadas](#%EF%B8%8F-tecnologiasferramentas-utilizadas)
* [🖥️ Funcionamento do sistema](#%EF%B8%8F-funcionamento-do-sistema)
   * [🧩 Parte 1 - Backend](#parte-1---backend)
   * [🎨 Parte 2 - Frontend](#parte-2---frontend)
* [🔀 Arquitetura da aplicação](#arquitetura-da-aplicação)
* [📁 Estrutura do projeto](#estrutura-do-projeto)
* [📌 Como executar o projeto](#como-executar-o-projeto)
* [🕵️ Dificuldades Encontradas](#%EF%B8%8F-dificuldades-encontradas)

## 📚 Contextualização do projeto

O projeto Speech Recognition - Whisper visa desenvolver um sistema de reconhecimento de fala em casa utilizando o modelo Whisper de última geração. O sistema será capaz de:

- __Transcrever áudio em tempo real:__ O sistema transcreverá áudio de conversas, entrevistas, palestras e outros eventos em tempo real, com alta precisão.
- __Controlar dispositivos domésticos inteligentes:__ O sistema poderá ser utilizado para controlar dispositivos domésticos inteligentes por voz, como luzes, TVs, ar-condicionado e muito mais.
- __Realizar tarefas automatizadas:__ O sistema poderá ser utilizado para realizar tarefas automatizadas, como agendar compromissos, enviar mensagens de texto, tocar música e muito mais.

### Sobre o Whisper

Whisper é um modelo de reconhecimento de fala desenvolvido pela OpenAI. Ele é capaz de transcrever e traduzir áudio com alta precisão. O modelo é treinado em uma grande quantidade de dados de áudio e texto, o que permite que ele funcione bem em uma variedade de idiomas e sotaques.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)
[<img src="https://img.shields.io/badge/OpenAI-Whisper-FF9900?logo=openai&logoColor=white">](https://github.com/openai/whisper)
[<img src="https://img.shields.io/badge/Scipy-8CAAE6?logo=scipy&logoColor=white">](https://www.scipy.org/)
[<img src="https://img.shields.io/badge/Soundfile-FF6F00?logo=python&logoColor=white">](https://pypi.org/project/SoundFile/)
[<img src="https://img.shields.io/badge/Sounddevice-FF6F00?logo=python&logoColor=white">](https://pypi.org/project/sounddevice/)
[<img src="https://img.shields.io/badge/FFmpeg-007ACC?logo=ffmpeg&logoColor=white">](https://ffmpeg.org/)
[<img src="https://img.shields.io/badge/Setuptools_Rust-FF6F00?logo=rust&logoColor=white">](https://pypi.org/project/setuptools-rust/)

## 🖥️ Funcionamento do sistema

### 🧩 Parte 1 - Backend

O backend da aplicação foi desenvolvido utilizando **Python** com diversas bibliotecas para gravação, reprodução e transcrição de áudio. As principais funcionalidades incluem a gravação de áudio, reprodução de áudio e transcrição de áudio utilizando o modelo Whisper.

* **Gravação e Reprodução de Áudio**: O arquivo [`devices/mic_devices.py`](devices/mic_devices.py) contém a lógica para gravação e reprodução de áudio utilizando a biblioteca `sounddevice`.
* **Transcrição de Áudio**: O arquivo [`speech_to_text/speech_recogntion.py`](speech_to_text/speech_recogntion.py) contém a lógica para transcrição de áudio utilizando o modelo Whisper.

### 🎨 Parte 2 - Frontend

O frontend foi construído para fornecer uma interface amigável ao usuário, permitindo que áudios sejam gravados e transcritos automaticamente. A estrutura utiliza **HTML, CSS, JavaScript**, e os scripts de comunicação com o backend são gerenciados pelo **FastAPI**.

* **Estilos e Imagens**: A pasta `public/css` contém os arquivos de estilo para o layout da aplicação, enquanto a pasta `public/images` armazena os recursos visuais.
* **Scripts**: Os arquivos `scripts/script.js` e `scripts/check_api.js` são responsáveis pela lógica de interação com o backend e validações do frontend.

## 🔀 Arquitetura da aplicação

O sistema é baseado em uma arquitetura de microserviços, onde o backend se comunica com os serviços da AWS para análise e processamento dos documentos. O AWS Bedrock desempenha um papel central na geração dos resumos, enquanto **Fitz** lida com a leitura e extração dos textos dos documentos.

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── .gitignore
├── controller/
│   └── transcribe_audio.py
├── devices/
│   └── mic_devices.py
├── env/
│   ├── install_whisper_ubuntu.sh
│   └── install_whisper_windows.sh
├── LICENSE
├── main.py
├── README.md
└── speech_to_text/
    └── speech_recogntion.py
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rafael-torres-nantes/AtHome-SpeechRecogntion-Whisper.git
   ```

2. **Instale as dependências:**
   ```bash
   # Para Ubuntu
   bash env/install_whisper_ubuntu.sh

   # Para Windows
   bash env/install_whisper_windows.sh
   ```

3. **Execute o script principal:**
   ```bash
   python main.py
   ```

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram enfrentadas, como:

- **Integração com dispositivos de áudio:** A configuração e utilização de diferentes dispositivos de áudio exigiu testes e ajustes para garantir a compatibilidade e funcionalidade do sistema.
- **Transcrição de áudio:** A implementação do modelo Whisper para transcrição de áudio exigiu ajustes para lidar com diferentes idiomas e sotaques.
- **Gerenciamento de dependências:** A instalação e configuração das dependências do projeto, especialmente em diferentes sistemas operacionais, foi um desafio contínuo.
