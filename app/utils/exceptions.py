from fastapi import HTTPException

def not_found(detail: str = "Resource not found"):
    return HTTPException(status_code=404, detail=f"{detail} not found")

def bad_request(detail: str = "Invalid request"):
    return HTTPException(status_code=400, detail=detail)

def conflict(detail: str = "Conflict occurred"):
    return HTTPException(status_code=409, detail=detail)

def unauthorized(detail: str = "Unauthorized"):
    return HTTPException(status_code=401, detail=detail)