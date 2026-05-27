from fastapi import FastAPI, UploadFile, File, Response
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents))
    img_no_bg = remove(img)
    buf = io.BytesIO()
    img_no_bg.save(buf, format="PNG")
    return Response(content=buf.getvalue(), media_type="image/png")