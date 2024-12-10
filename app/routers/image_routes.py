from fastapi import APIRouter, UploadFile, File, HTTPException, Response
from ..converters.images import convert_image_format

router = APIRouter()

# Mapeia formatos de entrada para formatos Pillow
VALID_FORMATS = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "bmp": "BMP",
    # caso queira adicionar webp no futuro: "webp": "WEBP"
}

# Mapeamento formato Pillow -> MIME
FORMAT_TO_MIME = {
    "JPEG": "image/jpeg",
    "PNG": "image/png",
    "GIF": "image/gif",
    "BMP": "image/bmp",
    # "WEBP": "image/webp" se necessário
}

@router.post("/convert")
async def convert_image(file: UploadFile = File(...), output_format: str = "PNG"):
    # Verificação do tipo de arquivo suportado como entrada
    if file.content_type not in ["image/jpeg", "image/png", "image/gif", "image/bmp"]:
        raise HTTPException(status_code=400, detail="Tipo de arquivo de imagem não suportado.")

    # Normaliza o formato solicitado
    fmt_lower = output_format.lower()
    if fmt_lower not in VALID_FORMATS:
        raise HTTPException(status_code=400, detail=f"Formato de saída '{output_format}' não suportado.")

    final_format = VALID_FORMATS[fmt_lower]  # Ex: 'jpeg' -> 'JPEG'
    media_type = FORMAT_TO_MIME.get(final_format, "application/octet-stream")

    input_bytes = await file.read()
    try:
        result_bytes = convert_image_format(input_bytes, final_format)
        # Extensão para o nome do arquivo de acordo com o formato final
        extension = final_format.lower() if final_format != "JPEG" else "jpg"

        return Response(
            content=result_bytes,
            media_type=media_type,
            headers={"Content-Disposition": f'attachment; filename="converted_image.{extension}"'}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
