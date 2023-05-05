from draw_uml_backend.app import app
from draw_uml_backend.v1.routes import *
import uvicorn


if __name__ == "__main__":
    # uvicorn draw_uml_backend.index:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)  # type: ignore
