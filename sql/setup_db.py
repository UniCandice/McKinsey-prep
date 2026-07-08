"""Load all CSVs from datasets/ into a SQLite database (sql/practice.db).

Run:   python sql/setup_db.py
Then:  sqlite3 sql/practice.db          # interactive shell
or:    python sql/run_query.py sql/01_joins.sql
"""
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parent.parent
DB = Path(__file__).parent / "practice.db"

conn = sqlite3.connect(DB)
for csv in sorted((ROOT / "datasets").glob("*.csv")):
    df = pd.read_csv(csv)
    df.to_sql(csv.stem, conn, if_exists="replace", index=False)
    print(f"loaded {csv.stem:20s} {len(df):>6,} rows")
conn.close()
print(f"\nDatabase ready: {DB}")
