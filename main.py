from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers import login_controller
from schemas.generic_response import GenericResponse
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

app.include_router(login_controller.router)

@app.get("/")
async def root():
    return {"Message": "It works"}