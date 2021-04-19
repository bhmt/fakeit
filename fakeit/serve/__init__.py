from typing import Dict, Any
import signal
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve as hyper_serve
from fastapi import FastAPI
from .router import GeneratedRouter
from models.definition import Definition


shutdown_event = asyncio.Event()


def _signal_handler(*_: Any) -> None:
    shutdown_event.set()


def serve(title: str, description: str, mapping: Dict[str, Definition], port: int):
    app = FastAPI(title=title, description=description)
    router = GeneratedRouter(mapping)
    app.include_router(router)

    conf = Config()
    conf.bind = [f"0.0.0.0:{port}"]

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGTERM, _signal_handler)
    loop.run_until_complete(
        hyper_serve(app, conf, shutdown_trigger=shutdown_event.wait)
    )
