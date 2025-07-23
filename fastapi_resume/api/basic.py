from typing import Any, Callable

from fastapi import APIRouter, Depends


def create_basic_router(get_resume_data: Callable[[], dict[str, Any]]) -> APIRouter:
    """Create a router for basic resume information endpoints"""
    router = APIRouter()

    @router.get("/")
    def root(resume_data: dict[str, Any] = Depends(get_resume_data)) -> dict[str, Any]:
        """Root endpoint, full resume"""
        return resume_data

    @router.get("/basic")
    def get_basic_info(
        resume_data: dict[str, Any] = Depends(get_resume_data),
    ) -> dict[str, Any]:
        """Get basic resume information"""
        return {
            "name": resume_data.get("name", {}),
            "about": resume_data.get("about", ""),
            "position": resume_data.get("position", ""),
        }

    return router
