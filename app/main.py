from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from app.pipeline import load_data, summary_by_category, monthly_revenue
from app.charts import revenue_by_category_chart, monthly_revenue_chart

app = FastAPI(title="Sales Data Pipeline")


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/summary")
def summary():
    try:
        df = load_data()
        return summary_by_category(df)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found at /data/sales.csv")


@app.get("/monthly")
def monthly():
    try:
        df = load_data()
        return monthly_revenue(df)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found at /data/sales.csv")


@app.get("/chart/category", response_class=Response)
def chart_category():
    df = load_data()
    png = revenue_by_category_chart(summary_by_category(df))
    return Response(content=png, media_type="image/png")


@app.get("/chart/monthly", response_class=Response)
def chart_monthly():
    df = load_data()
    png = monthly_revenue_chart(monthly_revenue(df))
    return Response(content=png, media_type="image/png")
