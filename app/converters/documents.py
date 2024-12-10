import subprocess
import tempfile
import os

def convert_document(input_bytes: bytes, output_format: str) -> bytes:
    # output_format pode ser 'docx', 'pdf', etc.
    with tempfile.NamedTemporaryFile(delete=False, suffix=".tmp") as temp_in:
        temp_in.write(input_bytes)
        temp_in.flush()
        input_path = temp_in.name

    output_path = os.path.splitext(input_path)[0] + "." + output_format

    try:
        subprocess.run(
            ["libreoffice", "--headless", "--convert-to", output_format, input_path, "--outdir", os.path.dirname(input_path)],
            check=True
        )

        with open(output_path, "rb") as f_out:
            result_bytes = f_out.read()

        return result_bytes
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Falha ao converter documento: {e}")
    finally:
        # Limpeza de arquivos temporários
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
