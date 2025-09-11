class Optimized:
    """
    Glouton : tri par % décroissant, puis prix croissant, puis profit € décroissant.
    Retourne (summary, picks_dict, cost_dict).
    """

    def __init__(self, names, prices, pcts, budget):
        self.names = names
        self.prices = prices
        self.pcts = pcts
        self.budget = float(budget)

    def solve(self):
        actions = []
        # Zip itère en parallèle sur les trois listes
        for n, p, pct in zip(self.names, self.prices, self.pcts):
            profit_eur = p * pct / 100.0
            actions.append((n, p, pct, profit_eur))

        # % desc, prix asc, profit € desc
        actions.sort(key=lambda a: (-a[2], a[1], -a[3]))

        remaining = self.budget
        total_cost = 0.0
        total_profit = 0.0
        picks = {}

        for n, p, pct, prof in actions:
            if p <= remaining:
                picks[n] = 1
                total_cost += p
                total_profit += prof
                remaining -= p

        summary = {"Total Profit": round(total_profit, 2)}
        cost    = {"Best cost": round(total_cost, 2)}
        return summary, picks, cost
