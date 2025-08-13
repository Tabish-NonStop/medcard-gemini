from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from model.gemini_api import GeminiApiModel
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
TEMP_IMAGE_PATH = "current_image.png"  # Temporary file path for uploaded image

app = FastAPI()


@app.post("/process-id/")
async def process_id_image(file: UploadFile = File(...)):
    # Validate image type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are supported.")

    # Save the uploaded image temporarily
    with open(TEMP_IMAGE_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        gemini = GeminiApiModel(API_KEY, TEMP_IMAGE_PATH)
        result = gemini.process_ID_image()

        if result is None:
            raise HTTPException(status_code=500, detail="Failed to parse Gemini API response.")

        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Clean up the temporary file
        if os.path.exists(TEMP_IMAGE_PATH):
            os.remove(TEMP_IMAGE_PATH)
