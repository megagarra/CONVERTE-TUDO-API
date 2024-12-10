from PIL import Image
from io import BytesIO

def convert_image_format(file_bytes: bytes, output_format: str) -> bytes:
    with Image.open(BytesIO(file_bytes)) as img:
        output_buffer = BytesIO()
        # Convertendo para RGB para evitar problemas com alguns formatos
        img = img.convert("RGB")
        img.save(output_buffer, format=output_format)
        return output_buffer.getvalue()
