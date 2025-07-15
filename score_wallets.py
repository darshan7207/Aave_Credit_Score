
import json
import pandas as pd
import numpy as np
from utils import preprocess_data, engineer_features, generate_scores
import matplotlib.pyplot as plt

def main(input_file, output_csv="wallet_scores.csv"):
    with open("C:/Users/asus/OneDrive/Desktop/Credit_Scoring_Project/user-wallet-transactions.json", "r") as f:
        raw_data = json.load(f)

    df = preprocess_data(raw_data)
    features_df = engineer_features(df)
    features_df["score"] = generate_scores(features_df)

    # Save output
    features_df[["userWallet", "score"]].to_csv(output_csv, index=False)

    # Plot score distribution
    bins = list(range(0, 1100, 100))
    plt.figure(figsize=(10, 6))
    plt.hist(features_df["score"], bins=bins, edgecolor='black')
    plt.title("Credit Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Number of Wallets")
    plt.grid(True)
    plt.savefig("score_distribution.png")
    print("Wallet scores and graph saved successfully.")

if __name__ == "__main__":
    import sys
    input_path = sys.argv[1] if len(sys.argv) > 1 else "user_transactions.json"
    main("C:/Users/asus/OneDrive/Desktop/Credit_Scoring_Project/user-wallet-transactions.json")
