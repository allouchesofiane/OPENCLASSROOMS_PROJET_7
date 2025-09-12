class Optimized:
    """
    tri par pourcentage décroissant, puis prix croissant, puis profit € décroissant.
    Retourne (summary, picks_dict, cost_dict).
    """

    def __init__(self, names, prices, pcts, budget):
        # Le contructeur (3 listes et le budget)
        self.names = names
        self.prices = prices
        self.pcts = pcts
        self.budget = float(budget)

    def solve(self):
        # Liste vide
        actions = []
        # Zip itère en parallèle sur les trois listes
        for n, p, pct in zip(self.names, self.prices, self.pcts):
            profit_eur = p * pct / 100.0
            actions.append((n, p, pct, profit_eur))

        # % desc, prix asc, profit € desc
        actions.sort(key=lambda a: (-a[2], a[1], -a[3]))

        budget_restant = self.budget
        total_cost = 0.0
        total_profit = 0.0
        picks = {}

        for n, p, pct, prof in actions:
            if p <= budget_restant:
                # Ajoute n dans picks avec la quantité 1
                picks[n] = 1
                # Mis a jour le profit le cout et budget restant
                total_cost += p
                total_profit += prof
                budget_restant -= p

        summary = {"Total Profit": round(total_profit, 2)}
        cost    = {"Best cost": round(total_cost, 2)}
        # Rtourne un tuple de ttrois dictionnaire
        return summary, picks, cost
