## Description: Output schemas for the API

from pydantic import BaseModel

class ChartResponse(BaseModel):
    image_base64: bytes