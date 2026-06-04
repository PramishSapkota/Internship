from fastapi import FastAPI, UploadFile, File
from PIL import Image
from pathlib import Path
import io
from fastapi.responses import FileResponse #,StreamingResponse

app = FastAPI()

@app.post("/convert")
async def convert_image(file: UploadFile = File(...)):

    # Read uploaded file
    image_bytes = await file.read()

    # Open image
    image = Image.open(io.BytesIO(image_bytes))

    # Create converted directory
    BASE_DIR = Path(__file__).parent
    output_dir = BASE_DIR / "converted"
    output_dir.mkdir(exist_ok=True)

    # Original filename without extension
    original_name = Path(file.filename).stem

    # Determine conversion
    if image.format == "PNG":
        output_file = output_dir / f"{original_name}.jpg"
        media_type = "image/jpeg"

        # JPEG doesn't support transparency
        if image.mode in ("RGBA", "LA", "P"):
            rgb_image = Image.new("RGB", image.size, (255, 255, 255))
            rgb_image.paste(image, mask=image.split()[-1])
            image = rgb_image
        else:
            image = image.convert("RGB")

        image.save(output_file, "JPEG")

    elif image.format == "JPEG":
        output_file = output_dir / f"{original_name}.png"
        media_type = "image/png"
        image.save(output_file, "PNG")

    else:
        return {
            "error": f"Unsupported format: {image.format}"
        }

    return FileResponse(output_file)
    # return StreamingResponse(output_file, media_type=media_type)
    