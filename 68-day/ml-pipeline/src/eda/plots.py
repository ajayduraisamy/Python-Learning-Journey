# plots.py
# EDA Visualization

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils.logger import log

def plot_distributions(df):
    log("Generating distribution plots...")
    for col in ["Amount", "Time"]:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.savefig(f"plots/dist_{col}.png")

def plot_correlation(df):
    log("Generating correlation heatmap...")
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(), cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("plots/correlation.png")

def plot_class_balance(df):
    log("Plotting class balance...")
    plt.figure()
    df["Class"].value_counts().plot(kind="bar")
    plt.title("Fraud (1) vs Non-Fraud (0)")
    plt.savefig("plots/class_balance.png")
