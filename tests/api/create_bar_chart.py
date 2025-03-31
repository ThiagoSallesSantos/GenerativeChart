import requests
import base64

database_connection_config_id = 1

response = requests.post(
    url=f"http://localhost:9876/generate/sql/{database_connection_config_id}/",
    json={
        "query": "Liste todos os clientes",
        "only_sql": False
    }
)

data = response.json()["result"]

response = requests.post(
    url="http://localhost:6789/chart/bar/",
    json={
        "query": "faça um gráfico da quantidade de clientes por país",
        "data": data
    }
)

print(response.json())

image_base64 = response.json()["image_base64"]

with open("./result_bar_chart.png", 'wb') as file:
    file.write(base64.b64decode(image_base64))
