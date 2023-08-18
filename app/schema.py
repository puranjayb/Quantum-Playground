from pydantic import BaseModel


class FormSchema(BaseModel):
    review: str