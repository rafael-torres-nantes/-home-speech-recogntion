from controller.transcribe_audio import generate_audio_file, run_transcribe

# Exemplo de uso
if __name__ == "__main__":

    # Gera um arquivo de áudio
    generate_audio_file(rec_duration=5)

    # Realiza a transcrição
    run_transcribe('audio_folder/input_audio.wav')