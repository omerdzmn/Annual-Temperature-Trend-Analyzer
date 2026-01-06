import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize():
    df = pd.read_csv("data/processed/climate_cleaned.csv")

    pivot = df.pivot(index="Month", columns="Year", values="Temperature")

    plt.figure(figsize=(14, 6))
    sns.heatmap(
        pivot,
        cmap="coolwarm",
        cbar_kws={"label": "Temperature (°C)"}
    )
    plt.title("Heatmap of Monthly Temperatures Over Years")
    plt.xlabel("Year")
    plt.ylabel("Month")
    plt.tight_layout()
    plt.savefig("outputs/figures/temperature_heatmap.png")
    plt.close()

    # Boxplot
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df["Temperature"])
    plt.title("Temperature Distribution")
    plt.savefig("outputs/figures/temperature_boxplot.png")
    plt.close()

    print("Visualizations saved in outputs/figures")

if __name__ == "__main__":
    visualize()
