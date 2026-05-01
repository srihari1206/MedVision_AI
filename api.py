from fastapi import FastAPI, HTTPException, UploadFile, File
from PIL import Image
from med_logic import analyze_medicine
from io import BytesIO

app=FastAPI(title="MedVision API", description="Secure Pharmacological Identification API")

@app.post("/analyze")
async def analyze_endpoint(file: UploadFile=File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image format (jpg, png, etc.)")
    try:
        image_bytes=await file.read()
        image=Image.open(BytesIO(image_bytes))
        result = analyze_medicine(image)

        # 5. Return the result as clean JSON
        return {"status": "success", "analysis": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI processing error: {str(e)}")

# Bypass Device Guard if run directly
if __name__ == "__main__":
    import uvicorn
    print("Starting MedVision API Server...")
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
        