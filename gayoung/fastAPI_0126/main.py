from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os 
from controller import user, board, root

def uris():
    return [user.router, board.router, root.router]

app = FastAPI()

static_dir =  os.path.join(os.path.dirname(__file__),"update")
app.mount("/update",StaticFiles(directory=static_dir), name="update")

apis = uris()
for r in apis:
    app.include_router(r)


