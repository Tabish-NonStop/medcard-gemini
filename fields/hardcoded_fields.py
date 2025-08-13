from pydantic import BaseModel

class base_fields(BaseModel):
    idNumber: str
    name: str
    dateOfBirth: str
    issueDate: str
    expiryDate: str
    gender: str
    address: str
    policyNumber: str
    groupNumber: str