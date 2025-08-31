# src/controllers.py
import csv
from modules.bruteForce import BruteForce

def lire_csv_actions(csv_path: str):
    """Lit le CSV et retourne les listes (noms, prix, bénéfices_en_%)."""
    noms = []
    prix = []
    benefs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            nom = (row.get("Actions") or "").strip()
            p = float(str(row.get("Coût par action (en euros)") or "0").replace(",", "."))
            b = float(str(row.get("Bénéfice (après 2 ans)") or "0").replace("%", "").replace(",", "."))
            noms.append(nom)
            prix.append(p)
            benefs.append(b)
    return noms, prix, benefs

def optimiser(csv_path: str, budget: float):
    """Lit les données, lance BruteForce et retourne le résultat."""
    noms, prix, benefs = lire_csv_actions(csv_path)
    bf = BruteForce(noms, prix, benefs, budget)
    return bf.solve()
