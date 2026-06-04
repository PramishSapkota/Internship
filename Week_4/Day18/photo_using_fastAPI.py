from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI()


@app.post("/resize-image")
async def resize_image(file: UploadFile = File(...), width: int = 300, height: int = 300):

    # 1. Read image bytes
    image_bytes = await file.read()

    # 2. Open image using PIL
    image = Image.open(io.BytesIO(image_bytes))

    # 3. Resize image
    resized_image = image.resize((width, height))

    # 4. Save to memory buffer
    buffer = io.BytesIO()
    resized_image.save(buffer, format=image.format)
    buffer.seek(0)

    # 5. Return image as response
    return StreamingResponse(buffer, media_type="image/jpeg")