"""Problem 04: minimal FastAPI app with GET handler.

Task:
1. Create FastAPI app object
2. Add GET / handler
3. Return JSON, for example: {"status": "ok", "service": "lecture-05"}
4. Run with: uvicorn 04_fastapi_get:app --reload
5. Check in browser: http://127.0.0.1:8000/
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    # TODO: return your health payload
    return {"status": "ok", "service": "lecture-05"}
