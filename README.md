# AraraBots@AtHome-SpeechRecogntion

(OpenAi)[https://github.com/openai/whisper]
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