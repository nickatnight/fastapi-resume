from typing import Any, Callable

from fastapi import APIRouter, Depends


def create_experience_router(
    get_resume_data: Callable[[], dict[str, Any]],
) -> APIRouter:
    """Create a router for experience-related endpoints"""
    router = APIRouter()

    @router.get("/experience")
    def get_experience(
        resume_data: dict[str, Any] = Depends(get_resume_data),
    ) -> dict[str, Any]:
        """Get work experience"""
        return {"experience": resume_data.get("experience", [])}

    return router
