from fastapi import APIRouter, Request, Depends, Response
from src.dependences import Auth, get_session
from src.config import settings

router = APIRouter()

@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", 
    "PATCH", "DELETE"])
async def proxy(path: str, request: Request, token: str = Depends(Auth().return_token), 
                session=Depends(get_session)):
    url = f"{settings.user_service_url}/{path}"

    headers = {
        k: v
        for k, v in request.headers.items()
        if k.lower() not in {"host", "content-length"}
    }
    headers["Authorization"] = f"Bearer {token}"

    async with session.request(
        method=request.method,
        url=url,
        params=request.query_params,
        headers=headers,
        data=await request.body(),
    ) as response:
        body = await response.read()

        response_headers = {
            k: v
            for k, v in response.headers.items()
            if k.lower() not in {
                "content-length",
                "transfer-encoding",
                "content-encoding",
            }
        }
    print(token)
    return Response(
        content=body,
        status_code=response.status,
        headers=response_headers,
    )
