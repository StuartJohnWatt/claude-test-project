import io
import matplotlib
matplotlib.use("Agg")  # non-interactive backend, required in a container
import matplotlib.pyplot as plt


def revenue_by_category_chart(summary: list[dict]) -> bytes:
    categories = [r["category"] for r in summary]
    revenues = [r["total_revenue"] for r in summary]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(categories, revenues, color="steelblue")
    ax.bar_label(bars, fmt="$%.0f", padding=4)
    ax.set_title("Total Revenue by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue ($)")
    ax.set_ylim(0, max(revenues) * 1.15)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()


def monthly_revenue_chart(monthly: list[dict]) -> bytes:
    months = [r["month"] for r in monthly]
    revenues = [r["total_revenue"] for r in monthly]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(months, revenues, marker="o", color="steelblue", linewidth=2)
    ax.fill_between(months, revenues, alpha=0.15, color="steelblue")
    ax.set_title("Monthly Revenue Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()
