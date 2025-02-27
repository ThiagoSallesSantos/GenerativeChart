## Description: Input schemas for the API

from pydantic import BaseModel

from typing import List, Dict, Tuple, Sequence, Union

class CreateChart(BaseModel):
    query: str
    data: Union[List, Dict, Tuple, Sequence, str]
