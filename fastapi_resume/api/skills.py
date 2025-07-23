from typing import Any, Callable

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException


def create_skills_router(get_resume_data: Callable[[], dict[str, Any]]) -> APIRouter:
    """Create a router for skills-related endpoints"""
    router = APIRouter()

    @router.get("/skills")
    def get_skills(
        resume_data: dict[str, Any] = Depends(get_resume_data),
    ) -> dict[str, Any]:
        """Get all skills"""
        return {"skills": resume_data.get("skills", [])}

    @router.get("/skills/{category}")
    def get_skills_by_category(
        category: str, resume_data: dict[str, Any] = Depends(get_resume_data)
    ) -> dict[str, Any]:
        """Get skills for a specific category"""
        skills = resume_data.get("skills", [])

        # Find the category (case-insensitive)
        category_lower = category.lower()
        for skill_category in skills:
            if isinstance(skill_category, dict):
                for cat_name, skill_list in skill_category.items():
                    if cat_name.lower() == category_lower:
                        return {cat_name: skill_list}

        raise HTTPException(
            status_code=404, detail=f"Skills category '{category}' not found"
        )

    return router
