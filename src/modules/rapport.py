
import argparse
import csv
import json
import statistics
from pathlib import Path
from math import isfinite

NAME_ALIASES  = {"actions #", "actions", "action", "nom", "name", "titre"}
PRICE_ALIASES = {"coût par action (en euros)", "prix", "price", "price (€)", "price (eur)", "price_eur", "cost"}
PCT_ALIASES   = {"bénéfice (après 2 ans)", "bénéfice", "profit", "return", "roi %", "roi", "benefit", "gain"}

def norm(s: str) -> str:
    return str(s).strip().lower()

def parse_price(x: str) -> float:
    s = str(x).replace("€", "").replace(" ", "").replace(",", ".")
    try:
        v = float(s)
        return v if isfinite(v) else float("nan")
    except Exception:
        return float("nan")

def parse_pct(x: str) -> float:
    s = str(x).replace("%", "").replace(" ", "").replace(",", ".")
    try:
        v = float(s) / 100.0  # stocké en ratio (ex: 0.12 pour 12%)
        return v if isfinite(v) else float("nan")
    except Exception:
        return float("nan")

def pick_column(columns, aliases):
    cols = list(columns)
    for c in cols:
        if norm(c) in aliases:
            return c
    return None

def stats(arr):
    if not arr:
        return {"count": 0}
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    q1 = arr_sorted[n // 4]
    q3 = arr_sorted[(3 * n) // 4]
    return {
        "count": n,
        "min": min(arr_sorted),
        "q1": q1,
        "median": statistics.median(arr_sorted),
        "q3": q3,
        "max": max(arr_sorted),
        "mean": statistics.mean(arr_sorted),
    }

def explore(csv_path: Path) -> dict:
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []
        name_col  = pick_column(cols, NAME_ALIASES)
        price_col = pick_column(cols, PRICE_ALIASES)
        pct_col   = pick_column(cols, PCT_ALIASES)

        total = 0
        names_nonempty = 0
        seen_names = set()
        dups = 0
        valids = 0
        prices = []
        pcts = []  # en pourcentage (ex: 12.5 pour 12.5%)
        for row in reader:
            total += 1
            name = (row.get(name_col) or "").strip() if name_col else ""
            price = parse_price(row.get(price_col)) if price_col else float("nan")
            pct_ratio = parse_pct(row.get(pct_col)) if pct_col else float("nan")

            if name and name.lower() != "nan":
                names_nonempty += 1
                if name in seen_names:
                    dups += 1
                else:
                    seen_names.add(name)

            valid = True
            if price_col is not None:
                valid = valid and (price == price) and (price > 0)
            if pct_col is not None:
                valid = valid and (pct_ratio == pct_ratio) and (pct_ratio > 0)
            if valid:
                valids += 1
                if price == price:
                    prices.append(price)
                if pct_ratio == pct_ratio:
                    pcts.append(pct_ratio * 100.0)  # stocké en pourcentage pour stats lisibles

        invalids = total - valids
        pct_valid = round((valids / total) * 100.0, 2) if total else 0.0
        pct_invalid = round((invalids / total) * 100.0, 2) if total else 0.0

        return {
            "dataset": csv_path.name,
            "columns_detected": {
                "name": name_col,
                "price_eur": price_col,
                "benefit_pct": pct_col,
            },
            "rows_total": total,
            "rows_with_name": names_nonempty,
            "duplicates_by_name": dups,
            "rows_valid_price_and_pct": valids,
            "pct_valid": pct_valid,
            "pct_invalid": pct_invalid,
            "price_eur_stats": stats(prices),
            "benefit_pct_stats": stats(pcts),
        }

def main():
    ap = argparse.ArgumentParser(description="Exploration/qualité d'un dataset d'actions")
    ap.add_argument("csv_file", type=str, help="Chemin du fichier CSV")
    ap.add_argument("--out", type=str, help="Chemin de sortie JSON (facultatif)")
    args = ap.parse_args()

    result = explore(Path(args.csv_file))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()