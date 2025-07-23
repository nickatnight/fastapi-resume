from fastapi import APIRouter
from fastapi.responses import JSONResponse


def create_health_router(data_file: str) -> APIRouter:
    """Create a router for health check endpoints"""
    from fastapi_resume.utils import load_resume_data

    router = APIRouter()

    @router.get("/health")
    def health_check() -> JSONResponse:
        """Health check endpoint"""
        try:
            load_resume_data(data_file)
            return JSONResponse(
                status_code=200,
                content={
                    "status": "healthy",
                    "message": "Resume data loaded successfully",
                },
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"status": "unhealthy", "message": str(e)},
            )

    return router
