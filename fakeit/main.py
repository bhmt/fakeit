import sys
import uvicorn
from fastapi import FastAPI
from reader import get_data
from router import GeneratedRouter

filepath = sys.argv[-1]
(data, success) = get_data(filepath)

if success is False:
    print(data)
    sys.exit(-1)

title = data.title or "FakeIt"
description = data.description or "Return pseudorandom data"
paths = data.paths

app = FastAPI(title=title, description=description)

router = GeneratedRouter(paths)
app.include_router(router)

uvicorn.run(app, host="0.0.0.0", port=9876, log_level="info")
