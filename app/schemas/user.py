from pydantic import BaseModel, EmailStr, Field

# -------------------------
# CREATE USER
# -------------------------
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)


# -------------------------
# LOGIN USER
# -------------------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# -------------------------
# OUTPUT USER (SAFE RESPONSE)
# -------------------------
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
