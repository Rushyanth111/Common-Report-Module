from pydantic import BaseModel

class DepartmentReport(BaseModel):
    Code: str
    Name: str

