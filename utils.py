
import pandas as pd
import numpy as np

def preprocess_data(raw_data):
    # Convert JSON records to DataFrame
    df = pd.DataFrame(raw_data)
    df = df[["userWallet", "action", "timestamp"]]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s', errors='coerce')
    return df

def engineer_features(df):
    grouped = df.groupby("userWallet")
    features = pd.DataFrame()
    features["tx_count"] = grouped.size()
    features["borrow_count"] = grouped.apply(lambda x: (x["action"] == "borrow").sum())
    features["repay_count"] = grouped.apply(lambda x: (x["action"] == "repay").sum())
    features["deposit_count"] = grouped.apply(lambda x: (x["action"] == "deposit").sum())
    features["liquidation_count"] = grouped.apply(lambda x: (x["action"] == "liquidationcall").sum())
    features["redeem_count"] = grouped.apply(lambda x: (x["action"] == "redeemunderlying").sum())

    features["repay_ratio"] = features["repay_count"] / (features["borrow_count"] + 1)
    features["deposit_ratio"] = features["deposit_count"] / (features["tx_count"] + 1)
    features["liquidation_ratio"] = features["liquidation_count"] / (features["tx_count"] + 1)

    features = features.fillna(0).reset_index()
    return features

def generate_scores(df):
    scores = (
        (df["repay_ratio"] * 400)
        + (df["deposit_ratio"] * 300)
        + ((1 - df["liquidation_ratio"]) * 200)
        + (np.minimum(df["tx_count"], 50) * 2)
    )
    return np.clip(scores, 0, 1000).astype(int)
