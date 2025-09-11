import csv
import time
from src.modules.bruteForce import BruteForce
from src.modules.optimized import Optimized

class Controller:
    """
    - Lit le CSV 
    - Sélectionne ('brute' ou 'greedy') et renvoie (summary, picks, cost)
    """

    def __init__(self, csv_path, budget, algo="greedy"):
        self.csv_path = csv_path
        self.budget = float(budget)
        self.algo = algo

    def _read_csv(self):
        names, prices, pcts = [], [], []

        with open(self.csv_path, encoding="utf-8") as f:
            r = csv.DictReader(f)
            for row in r:
                # nom 
                name = (row.get("name") or row.get("Actions #") or "").strip()

                # cout
                price_raw = row.get("price") or row.get("Coût par action (en euros)")
                pct_raw   = row.get("profit") or row.get("Bénéfice (après 2 ans)")


                # prix : remplace virgule → point, supprime espaces/nbsp
                price_txt = str(price_raw or "").strip().replace(",", ".").replace('€', '')
                # pourcentage : enlève le symbole %, normalise virgule → point
                pct_txt   = str(pct_raw   or "").strip().replace("%", "").replace(" ", "").replace(",", ".")

                # validation
                if price_txt == "" or pct_txt == "":
                    continue

                # conversion
                price = float(price_txt)
                pct   = float(pct_txt)

                # filtres
                if price <= 0 or pct <= 0:
                    continue
                if price > self.budget:
                    continue

                names.append(name)
                prices.append(price)
                pcts.append(pct)

        return names, prices, pcts

    def run(self):
        names, prices, pcts = self._read_csv()
        start = time.time()
        if self.algo == "brute":
            solver = BruteForce(names, prices, pcts, self.budget)
        else:  # "greedy"
            solver = Optimized(names, prices, pcts, self.budget)
        result = solver.solve()
        execution_time = time.time() - start
        print(f"Temps d'exécution: {execution_time:.4f}s")
        return result

