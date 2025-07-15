
# Credit Scoring Model for Aave V2 Wallets

## Overview
This project builds a credit scoring system for wallets interacting with the Aave V2 protocol. It processes 100K+ raw DeFi transaction records and assigns each wallet a score between **0 and 1000**, reflecting the reliability and responsibility of its activity.

## How It Works
Each wallet's behavior is analyzed through:
- Types of actions: `borrow`, `repay`, `deposit`, `liquidationcall`, `redeemunderlying`
- Frequency and patterns of transactions
- Ratios like repay-to-borrow and liquidation rate

## Architecture
```
user_transactions.json
        ↓
  preprocess_data()
        ↓
  engineer_features()
        ↓
  generate_scores()
        ↓
wallet_scores.csv + score_distribution.png
```

## How to Run
```bash
python score_wallets.py user_transactions.json
```

## Scoring Logic
The credit score is calculated using:
- `repay_ratio` → high = responsible
- `deposit_ratio` → indicates positive participation
- `liquidation_ratio` → high = risky behavior
- `tx_count` → active wallets get a small bonus

The final score is clipped between 0 and 1000.

## Requirements
- Python 3.8+
- pandas, numpy, matplotlib
