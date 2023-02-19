from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, constr
from pydantic.schema import date


class ContactPersonModel(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: EmailStr
    phone: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^(\+)[0-9]{9,18}$",
        )
    ]  # стандарт префикс "+" и 15 цифр но в германии есть 18
    b_date = Optional[date]
    additional_info = str = Field(max_length=500)
