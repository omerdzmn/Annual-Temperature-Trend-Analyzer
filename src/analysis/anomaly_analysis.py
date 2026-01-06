import pandas as pd
import matplotlib.pyplot as plt


def analyze():
    """
    Analyze yearly temperature anomalies
    and visualize long-term trends.
    """

    LOCATION_NAME = "Istanbul / Kadıköy"

    df = pd.read_csv("data/processed/climate_cleaned.csv")

    yearly = df.groupby("year")["tavg"].mean().reset_index()
    long_term_avg = yearly["tavg"].mean()
    yearly["anomaly"] = yearly["tavg"] - long_term_avg

    plt.rcParams.update({
        "figure.facecolor": "#ECEFF4",
        "axes.facecolor": "#F8FAFC",
        "axes.edgecolor": "#CBD5E1",
        "axes.labelcolor": "#1E293B",
        "text.color": "#1E293B",
        "xtick.color": "#475569",
        "ytick.color": "#475569",
        "grid.color": "#CBD5E1",
        "font.size": 11
    })

    fig, ax = plt.subplots(figsize=(14, 7))

    ax.axhline(
        long_term_avg,
        linestyle="--",
        linewidth=2,
        color="#64748B",
        label="Long-Term Average"
    )

    ax.plot(
        yearly["year"],
        yearly["tavg"],
        linewidth=2.8,
        alpha=0.6,
        zorder=1,
        label="Yearly Avg Temperature"
    )

    sc = ax.scatter(
        yearly["year"],
        yearly["tavg"],
        c=yearly["anomaly"],
        cmap="coolwarm",
        s=95,
        edgecolors="#334155",
        linewidths=0.7,
        zorder=2,
        label="Temperature Anomaly"
    )

    ax.set_title(
        "Annual Temperature Change Over Years\nIstanbul / Kadıköy",
        fontsize=18,
        fontweight="bold",
        pad=28
    )

    fig.text(
        0.5,
        0.90,
        "Each point represents the average temperature of a year.\n"
        "Red tones indicate warmer-than-average years, blue tones indicate cooler-than-average years.",
        ha="center",
        fontsize=10,
        color="#475569"
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Average Temperature (°C)")
    ax.grid(True, linestyle="--", alpha=0.6)

    cbar = fig.colorbar(sc, ax=ax)
    cbar.set_label("Temperature Difference from Long-Term Average (°C)")

    ax.legend(frameon=True, facecolor="white", edgecolor="#CBD5E1")

    fig.text(
        0.5,
        0.02,
        "Each year represents the annual average temperature derived from daily measurements.",
        ha="center",
        fontsize=10,
        color="#475569"
    )

    plt.tight_layout(rect=[0, 0.04, 1, 0.88])
    plt.show()
