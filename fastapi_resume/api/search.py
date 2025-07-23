from typing import Any, Callable

from fastapi import APIRouter, Depends


def create_search_router(get_resume_data: Callable[[], dict[str, Any]]) -> APIRouter:
    """Create a router for search-related endpoints"""
    router = APIRouter()

    @router.get("/search")
    def search_resume(
        query: str, resume_data: dict[str, Any] = Depends(get_resume_data)
    ) -> dict[str, Any]:
        """Search across all resume data"""
        query_lower = query.lower()
        results = []

        # Search in various fields
        for key, value in resume_data.items():
            if isinstance(value, str) and query_lower in value.lower():
                results.append({"field": key, "value": value})
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        for sub_key, sub_value in item.items():
                            if (
                                isinstance(sub_value, str)
                                and query_lower in sub_value.lower()
                            ):
                                results.append(
                                    {"field": f"{key}.{sub_key}", "value": sub_value}
                                )
                    elif isinstance(item, str) and query_lower in item.lower():
                        results.append({"field": key, "value": item})

        return {"query": query, "results": results, "count": len(results)}

    return router
