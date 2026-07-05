from fastapi import FastAPI
from pydantic import BaseModel, Field
from .scoring import score_parcelle, classify_score

app = FastAPI(
    title="3.5.7 FONCIER API",
    description="Prototype API pour l'analyse foncière et le scoring des parcelles.",
    version="0.1.0",
)

class ParcelleInput(BaseModel):
    commune: str = Field(..., examples=["Ormoy-la-Rivière"])
    reference: str = Field(..., examples=["AB 123"])
    surface_m2: float = Field(..., gt=0, examples=[1800])
    zone_plu: str | None = Field(None, examples=["UD"])
    emprise_batie_m2: float | None = Field(None, ge=0, examples=[120])
    maison_en_facade: bool | None = Field(None, examples=[True])
    acces_possible: bool | None = Field(None, examples=[True])
    terrain_angle: bool | None = Field(None, examples=[False])
    contrainte_forte: bool | None = Field(None, examples=[False])

@app.get("/")
def root():
    return {"project": "3.5.7 FONCIER", "status": "prototype", "version": "0.1.0"}

@app.post("/score")
def score(input_data: ParcelleInput):
    score_value, details = score_parcelle(input_data.model_dump())
    return {
        "commune": input_data.commune,
        "reference": input_data.reference,
        "score": score_value,
        "classe": classify_score(score_value),
        "details": details,
    }
