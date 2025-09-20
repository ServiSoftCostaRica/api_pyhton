from sqlalchemy.orm import Session
import json
from http import HTTPStatus
from schemas.generic_response import GenericResponse
from schemas.login_request import LoginRequest

def login_dummy(login_request: LoginRequest):
    response = GenericResponse(input={"username":login_request.username, "password":login_request.password}, status=HTTPStatus.OK, message='', results = None)
    dict_list = [{"username": login_request.username, "password": login_request.password}]
    response.results = dict_list
    return response