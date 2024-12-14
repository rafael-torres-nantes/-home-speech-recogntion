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