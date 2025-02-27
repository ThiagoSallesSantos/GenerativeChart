from pydantic import BaseModel

from enum import Enum

from typing import List

class BarChart(BaseModel):
    categories: List[str]
    heights: List[int | float]

    x_axis: str
    y_axis: str
    title: str

class PieChart(BaseModel):
    categories: List[str]
    slices: List[int | float]

    title: str

class ChartDescription(str, Enum):
    BAR = "To format the data in the format to create a bar chart, you need to identify and return a list of the target categories and a list with their respective heights of each bar for each category, provide a name for the x-axis and y-axis, and a name for this chart."
    PIE = "To format the data in the format to create a pie chart, you need to identify and return a list of the target categories and a list of their respective slices for each category, and provide a name for this chart."
