from fastapi import APIRouter, UploadFile, File, HTTPException, Response
from ..converters.documents import convert_document

router = APIRouter()

@router.post("/convert")
async def convert_doc(file: UploadFile = File(...), output_format: str = "docx"):
    # Por exemplo, suportando PDF para docx
    supported_input_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if file.content_type not in supported_input_types:
        raise HTTPException(status_code=400, detail="Tipo de documento não suportado para conversão.")

    input_bytes = await file.read()
    try:
        result_bytes = convert_document(input_bytes, output_format)
        return Response(
            content=result_bytes,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename="converted_document.{output_format}"'}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
