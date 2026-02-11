from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.utils.file_utils import save_uploaded_file
from backend.services.parser import parse_document

router = APIRouter()


@router.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    try:
        content = await file.read()

        file_path = save_uploaded_file(content, file.filename)

        extracted_text = parse_document(file_path)

        return {
            "filename": file.filename,
            "stored_path": file_path,
            "text_length": len(extracted_text),
            "preview": extracted_text[:1000]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
