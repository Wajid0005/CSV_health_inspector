from pathlib import Path
from loader import load_data
from analyzer import CSVInspector

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "IPL_Matches_2008_2022.csv"
REPORT_PATH = BASE_DIR / "report.txt"


def main():
    data = load_data(CSV_PATH)
    inspector = CSVInspector(data)
    report = inspector.generate_report()

    with REPORT_PATH.open("w", encoding="utf-8") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    main()