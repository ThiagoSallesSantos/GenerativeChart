## Description: Database routes

from fastapi import APIRouter, HTTPException

from src.model.prompt import get_chart_prompt
from src.model.generative import generate_chart_data 

from src.chart.types import BarChart, PieChart, ChartDescription
from src.chart.chart import plot_bar_chart, plot_pie_chart

from src.routes.utils import convert_bytesio_to_base64

from src.routes.schemas.input import CreateChart
from src.routes.schemas.output import ChartResponse

router = APIRouter(prefix="/chart", tags=["Chart"])

@router.post("/bar/", response_model=ChartResponse,
    summary="Create a bar chart",
    description="""
        Receive data to create a bar chart
    """,
)
def create_bar_chart(
    data: CreateChart,
):
    try:
        bar_chart_description = ChartDescription.BAR
        prompt_chart = get_chart_prompt(query=data.query, chart_description=bar_chart_description.value, raw_data=data.data)

        generated_bar_data: BarChart = generate_chart_data(prompt=prompt_chart, output_scheme=BarChart)

        file_bytes = plot_bar_chart(bar_chart_data=generated_bar_data)

        image_base64 = convert_bytesio_to_base64(file_bytes=file_bytes)
        
        return ChartResponse(image_base64=image_base64)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/pie/", response_model=ChartResponse,
    summary="Create a pie chart",
    description="""
        Receive data to create a pie chart
    """,
)
def create_pie_chart(
    data: CreateChart,
):
    try:
        pie_chart_description = ChartDescription.PIE
        prompt_chart = get_chart_prompt(query=data.query, chart_description=pie_chart_description.value, raw_data=data.data)

        generated_pie_data: PieChart = generate_chart_data(prompt=prompt_chart, output_scheme=PieChart)

        file_bytes = plot_pie_chart(pie_chart_data=generated_pie_data)

        image_base64 = convert_bytesio_to_base64(file_bytes=file_bytes)

        return ChartResponse(image_base64=image_base64)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))