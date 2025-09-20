from fastapi import APIRouter, Depends, HTTPException, status, Body
from schemas.generic_response import GenericResponse
from schemas.login_request import LoginRequest
from services import login_service

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login-dummy", response_model=GenericResponse)
async def post_login_dummy(login_request: LoginRequest):
    return login_service.login_dummy(login_request)