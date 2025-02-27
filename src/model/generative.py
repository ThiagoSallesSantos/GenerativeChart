import ollama

from pydantic import BaseModel

def generate_chart_data(prompt: str, output_scheme: BaseModel) -> BaseModel:
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        format=output_scheme.model_json_schema(),
        options=ollama.Options(
            temperature=0.0,
            num_ctx=16384
        ),
        keep_alive=0
    )

    chart_data = output_scheme.model_validate_json(response.response)

    return chart_data
