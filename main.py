#pylint: disable=missing-docstring
#pylint: disable=import-error

import importlib
import os
from fastapi import FastAPI

ACTIVE_MODULES_DIR = os.path.join("modules", "active")

app = FastAPI()

for filename in os.listdir(ACTIVE_MODULES_DIR):
    if filename.endswith(".py"): #NOTE: Consider excluding __init__.py
        module_name = f"{ ACTIVE_MODULES_DIR.replace(os.sep,'.') }.{filename[:-3]}"
        module = importlib.import_module(module_name)
        app.include_router(module.router)
