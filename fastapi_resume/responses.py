from typing import Any

import orjson
from fastapi.responses import JSONResponse


class ORJSONPrettyResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return orjson.dumps(
            content,
            option=orjson.OPT_NON_STR_KEYS
            | orjson.OPT_SERIALIZE_NUMPY
            | orjson.OPT_INDENT_2,
        )
