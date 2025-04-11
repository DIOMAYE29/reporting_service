from fastapi import FastAPI

# Créer l'instance FastAPI
app = FastAPI()

# Importer les routes (exemple)
from app.routers import reports

# Inclure les routes
app.include_router(reports.router)

# Exemple de route de test
@app.get("/")
async def root():
    return {"message": "Reporting Service OK"}