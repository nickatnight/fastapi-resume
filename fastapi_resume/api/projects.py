from typing import Any, Callable

from fastapi import APIRouter, Depends


def create_projects_router(get_resume_data: Callable[[], dict[str, Any]]) -> APIRouter:
    """Create a router for projects-related endpoints"""
    router = APIRouter()

    @router.get("/projects")
    def get_projects(
        resume_data: dict[str, Any] = Depends(get_resume_data),
    ) -> dict[str, Any]:
        """Get projects"""
        return {"projects": resume_data.get("projects", [])}

    return router
