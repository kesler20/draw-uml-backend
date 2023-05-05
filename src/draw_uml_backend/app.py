from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from draw_uml_backend import __version__

# ---------------------------------------------------#
#                                                    #
#     INITIALIZE APPLICATION AND CONFIGURATIONS      #
#                                                    #
# ---------------------------------------------------#

app = FastAPI(
    title="draw_uml_backend",
    description="The backend of the draw uml application",
    version=__version__,
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root():
    response = RedirectResponse(url="/docs")
    return response
