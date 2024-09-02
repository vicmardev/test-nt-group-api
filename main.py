from fastapi import FastAPI, HTTPException
from models import NumberSet
app = FastAPI()
number_set = NumberSet()

@app.post("/extract/{number}")
async def extract_number(number: int):
    try:
        number_set.extract_number(number)
        return {"message": f"El número {number} ha sido extraído."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/missing_number")
async def missing_number():
    missing = number_set.find_missing_number()
    return {"numero_extraido": missing}
