from typing import Any, Dict
# from urllib import request
from fastapi import APIRouter, Request
from app.models import DiagramPayload
from fastapi.templating import Jinja2Templates
from app.schema import get_schema, generate_mermaid

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/visualize")



@router.get("")
async def index(request: Request):

    return templates.TemplateResponse("index.html", context={"request": request})


@router.post("/create")
async def index(payload: DiagramPayload) -> Dict[str, Any]:
    scheme = get_schema(payload.path)
    data = generate_mermaid(schema=scheme, direction=payload.direction)
    return {"data": data}
