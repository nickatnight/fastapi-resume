from typing import Any, Callable

from fastapi import APIRouter, Depends


def create_contact_router(get_resume_data: Callable[[], dict[str, Any]]) -> APIRouter:
    """Create a router for contact-related endpoints"""
    router = APIRouter()

    @router.get("/contact")
    def get_contact(
        resume_data: dict[str, Any] = Depends(get_resume_data),
    ) -> dict[str, Any]:
        """Get contact information"""
        return {"contact": resume_data.get("contact", {})}

    return router
