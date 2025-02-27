import matplotlib.pyplot as plt

from io import BytesIO

from src.chart.types import BarChart, PieChart

def plot_bar_chart(bar_chart_data: BarChart) -> BytesIO:
    plt.bar(bar_chart_data.categories, bar_chart_data.heights)
    plt.xlabel(bar_chart_data.x_axis)
    plt.ylabel(bar_chart_data.y_axis)
    plt.title(bar_chart_data.title)

    file_bytes = BytesIO()
    plt.savefig(file_bytes, format="png")

    plt.close()

    return file_bytes

def plot_pie_chart(pie_chart_data: PieChart) -> BytesIO:
    plt.pie(pie_chart_data.slices, labels=pie_chart_data.categories, autopct='%1.1f%%')
    plt.title(pie_chart_data.title)
    plt.legend()

    file_bytes = BytesIO()
    plt.savefig(file_bytes, format="png")

    plt.close()

    return file_bytes
