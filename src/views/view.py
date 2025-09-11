class View:
    def render(self, summary, picks, cost, budget=None):
        print("\n=== Résultat ===")
        if budget is not None:
            print(f"Budget       : {budget} €")
        print(f"Profit total : {summary['Total Profit']} €")
        print(f"Coût total   : {cost['Best cost']} €")
        print("Actions achetées :")
        if not picks:
            print("  (aucune)")
        else:
            for nom in picks:
                print(" -", nom)

