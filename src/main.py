from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from src.api.views import router as api_router
from src.utilities.decoder import WeirdTextDecodeError


app = FastAPI()

app.include_router(api_router, prefix="/api/v1")


@app.exception_handler(WeirdTextDecodeError)
async def decoding_exception_handler(request: Request, exc: WeirdTextDecodeError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )
