from pydantic import BaseModel, EmailStr


class TALoginDTO(BaseModel):
    email: EmailStr
    password: str