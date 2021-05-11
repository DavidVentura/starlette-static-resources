#!/usr/bin/env python3
import uvicorn

from starlette.applications import Starlette
from starlette_static_resources import StaticResources
from importlib_resources import files


app = Starlette()
app.mount('/', StaticResources(resources=files('example.data')), name='static')

uvicorn.run(app, host='0.0.0.0', port=8008)
