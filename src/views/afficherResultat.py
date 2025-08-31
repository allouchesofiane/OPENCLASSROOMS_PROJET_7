# src/views.py
def afficher_resultat(resume: dict, picks: dict, cost: dict):
    print("\n=== Résultat ===")
    print(f"Profit total : {resume['Total Profit']} €")
    print(f"Coût total   : {cost['Best cost']} €")
    print("Actions achetées :")
    if not picks:
        print("  (aucune)")
    else:
        for nom in picks:
            print("  -", nom)


