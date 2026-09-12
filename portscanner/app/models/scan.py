from pydantic import BaseModel

class ScanResult(BaseModel):
    target: str
    port: int
    status: str