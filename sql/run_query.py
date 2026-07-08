"""Run every SQL statement in a file against practice.db and print the results.

Usage: python sql/run_query.py sql/01_joins.sql
       python sql/run_query.py "SELECT * FROM customers LIMIT 5"
"""
import sqlite3
import sys
from pathlib import Path

import pandas as pd

DB = Path(__file__).parent / "practice.db"
arg = sys.argv[1]
sql = Path(arg).read_text() if arg.endswith(".sql") else arg

conn = sqlite3.connect(DB)
pd.set_option("display.max_rows", 30)
pd.set_option("display.width", 140)

# naive split on ';' is fine for practice files
for i, stmt in enumerate(s.strip() for s in sql.split(";") if s.strip()):
    # skip pure comment blocks
    if all(line.strip().startswith("--") or not line.strip()
           for line in stmt.splitlines()):
        continue
    print(f"\n--- statement {i + 1} " + "-" * 50)
    try:
        print(pd.read_sql_query(stmt, conn))
    except Exception as e:
        print(f"ERROR: {e}")
conn.close()
