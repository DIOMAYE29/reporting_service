from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from ..utils import generate_pdf_report
from ..database import fetch_historical_data

router = APIRouter()

@router.post("/generate-report")
async def generate_report():
    data = await fetch_historical_data()  # Récupère les données de ThingsBoard/farmOS
    report_path = generate_pdf_report(data)
    return {"report_url": f"/download-report/{report_path}"}

@router.get("/download-report/{filename}")
async def download_report(filename: str):
    return FileResponse(f"reports/{filename}", media_type="application/pdf")