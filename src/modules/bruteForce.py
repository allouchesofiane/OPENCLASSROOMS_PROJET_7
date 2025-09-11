from itertools import product

class BruteForce:
    """
    Algorithme  Force brute 
    Retourne (summary, picks_dict, cost_dict).
    """

    def __init__(self, names, prices, pcts, budget):
        self.names = names
        self.prices = prices
        self.pcts = pcts
        self.budget = float(budget)

    def solve(self):
        n = len(self.prices)
        best_profit = 0.0
        best_cost = 0.0
        best_combo = None

        for combo in product((0, 1), repeat=n):
            # coût
            cost = 0.0
            for take, price in zip(combo, self.prices):
                if take:
                    cost += price
            if cost > self.budget:
                continue

            # profit
            profit = 0.0
            for take, price, pct in zip(combo, self.prices, self.pcts):
                if take:
                    profit += price * pct / 100.0

            if profit > best_profit:
                best_profit = profit
                best_cost = cost
                best_combo = combo

        picks = {}
        if best_combo is not None:
            for take, name in zip(best_combo, self.names):
                if take:
                    picks[name] = 1

        summary = {"Total Profit": round(best_profit, 2)}
        cost    = {"Best cost": round(best_cost, 2)}
        return summary, picks, cost
