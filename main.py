#pylint: disable=missing-docstring
#pylint: disable=import-error

import importlib
import os
from fastapi import FastAPI

ACTIVE_MODULES_DIR = "modules/active/"

app = FastAPI()

for filename in os.listdir(ACTIVE_MODULES_DIR):
    if filename.endswith(".py"): #NOTE: Consider excluding __init__.py
        MODULE_NAME = f"{ ACTIVE_MODULES_DIR }.{filename[:-3]}"
        module = importlib.import_module(MODULE_NAME)
        app.include_router(module.router)
