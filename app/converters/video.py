import subprocess
import tempfile
import os

def extract_audio_from_video(video_bytes: bytes, output_format: str = "mp3") -> bytes:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".tmp") as temp_in:
        temp_in.write(video_bytes)
        temp_in.flush()
        input_path = temp_in.name

    output_path = os.path.splitext(input_path)[0] + "." + output_format

    try:
        # Extrai áudio do vídeo
        subprocess.run(
            ["ffmpeg", "-i", input_path, "-vn", "-ar", "44100", "-ac", "2", "-b:a", "192k", output_path],
            check=True
        )

        with open(output_path, "rb") as f_out:
            audio_bytes = f_out.read()

        return audio_bytes
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Falha ao extrair áudio: {e}")
    finally:
        # Limpa arquivos temporários
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
