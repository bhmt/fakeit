from fastapi import FastAPI
import uvicorn
from typing import Dict
from router import GeneratedRouter
from models.definition import Definition


def serve(title: str, description: str, mapping: Dict[str, Definition]):
    title = title or "FakeIt"
    description = description or "Return pseudorandom data"
    app = FastAPI(title=title, description=description)

    router = GeneratedRouter(mapping)
    app.include_router(router)

    uvicorn.run(app, host="0.0.0.0", port=9876, log_level="info")
