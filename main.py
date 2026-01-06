from src.scraping.scrape_climate import scrape_climate
from src.cleaning.clean_data import clean_data
from src.analysis.anomaly_analysis import analyze


def main():
    scrape_climate()
    clean_data()
    analyze()


if __name__ == "__main__":
    main()
