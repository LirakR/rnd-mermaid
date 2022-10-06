from typing import Optional
from pydantic import BaseModel


class MermaidBase(BaseModel):
    ...


class DiagramPayload(MermaidBase):
    path: str
    direction: Optional[str] = "LR"
