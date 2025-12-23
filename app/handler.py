import json
from sqlalchemy import text
from app.db import engine

def _response(status_code: int, payload: dict):
    return {
        "statusCode": status_code,
        "headers": {
            "content-type": "application/json",
        },
        "body": json.dumps(payload),
    }

def lambda_handler(event, context):
   
    path = event.get("rawPath", "/")
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

    # 1) Probar API Gateway -> Lambda (no DB)
    if path == "/" and method in ("GET", "POST", "PUT", "DELETE"):
        return _response(200, {"ok": True, "message": "Hello from Orbital Parcel Ops!"})

    # 2) Probar Lambda -> DB
    # GET /health hace SELECT 1
    if path == "/health" and method == "GET":
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return _response(200, {"ok": True, "db": "ok"})
        except Exception as e:
            # No expongas credenciales; solo el error para debug
            return _response(500, {"ok": False, "db": "error", "detail": str(e)})

    # 404 para el resto
    return _response(404, {"ok": False, "error": "Not Found", "path": path, "method": method})