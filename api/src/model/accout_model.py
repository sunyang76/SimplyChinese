from pydantic import BaseModel


class GenericResponse(BaseModel):
    message: str | None
    status: bool

class LoginResponse(GenericResponse):
    token: str

class AccessRequest(BaseModel):
    email: str


class LoginByCodeRequest(BaseModel):
    email: str
    passcode: str


class LoginByKeyRequest(BaseModel):
    email: str
    keycode: str


class SignupRequest(BaseModel):
    email: str
    name: str
