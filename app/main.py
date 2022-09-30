from typing import Dict
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import visualize

app = FastAPI()


app = FastAPI(
    title="Model Visualizer",
    description="",
    version="0.10.0",
)



app.mount("/home/lirakr/repos/rnd-mermaid/app/static", StaticFiles(directory="/home/lirakr/repos/rnd-mermaid/app/static"), name="static")


@app.get(
    "/",
    summary="Status",
    responses={200: {"content": {"application/json": {"example": {"status": "OK"}}}}},
)
async def index() -> Dict[str, str]:
    """
    Show application status and docker image details
    """
    return {"status": "OK"}


app.include_router(visualize.router)
