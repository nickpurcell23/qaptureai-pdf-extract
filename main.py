from fastapi import FastAPI, UploadFile, File
import pdfplumber
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/extract")
async def extract_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text = ""
    with pdfplumber.open(io.BytesIO(content)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return {"text": text}
