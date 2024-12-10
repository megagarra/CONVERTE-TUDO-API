from fastapi import APIRouter, UploadFile, File, HTTPException, Response
from ..converters.video import extract_audio_from_video

router = APIRouter()

@router.post("/extract-audio")
async def extract_audio(file: UploadFile = File(...), output_format: str = "mp3"):
    if "video" not in file.content_type:
        raise HTTPException(status_code=400, detail="O arquivo fornecido não é um vídeo válido.")

    input_bytes = await file.read()
    try:
        audio_bytes = extract_audio_from_video(input_bytes, output_format=output_format)
        return Response(
            content=audio_bytes,
            media_type=f"audio/{output_format}",
            headers={"Content-Disposition": f'attachment; filename="extracted_audio.{output_format}"'}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
