# eda_runner.py
# Full pipeline: load → clean → EDA → save

from ingestion.data_loader import load_raw
from eda.cleaner import clean
from eda.plots import plot_distributions, plot_correlation, plot_class_balance
from utils.logger import log

def run():
    log("=== Running EDA Pipeline ===")

    df = load_raw()
    df_clean = clean(df)

    plot_distributions(df_clean)
    plot_class_balance(df_clean)
    plot_correlation(df_clean)

    log("=== EDA Completed Successfully ===")

if __name__ == "__main__":
    run()
