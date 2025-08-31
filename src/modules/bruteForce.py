from itertools import product

class BruteForce:
    """
    Algorithme brute force pour trouver la meilleure combinaison d'actions
    avec une contrainte de budget.
    """

    def __init__(self, names, prices, benefices_pct, budget):
        self.names = names                
        self.prices = prices              
        self.benefices_pct = benefices_pct
        self.budget = budget           

    def solve(self):
        n = len(self.prices)

        meilleur_profit = 0.0
        meilleur_cout = 0.0
        # tuple
        meilleure_combinaison = None  

        # Génère toutes les combinaisons possibles 
        for combinaison in product((0, 1), repeat=n):
            
            # Coût total de la combinaison
            cout_total = sum(
                prix for prendre, prix in zip(combinaison, self.prices) if prendre
            )

            # Si le coût dépasse le budget, on passe 
            if cout_total > self.budget:
                continue

            # Profit total  
            profit_total = sum(
                prix * benef / 100
                for prendre, prix, benef in zip(combinaison, self.prices, self.benefices_pct)
                if prendre
            )

            # Si ce profit est meilleur, on garde cette combinaison
            if profit_total > meilleur_profit:
                meilleur_profit = profit_total
                meilleur_cout = cout_total
                meilleure_combinaison = combinaison

        # Dictionnaire des actions achetées
        actions_achetees = {}
        if meilleure_combinaison is not None:
            for prendre, nom in zip(meilleure_combinaison, self.names):
                if prendre:
                    actions_achetees[nom] = 1
        
        # Résultat 
        return (
            {"Total Profit": round(meilleur_profit, 2)},
            actions_achetees,
            {"Best cost": round(meilleur_cout, 2)},
        )
