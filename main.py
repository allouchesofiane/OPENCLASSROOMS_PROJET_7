import argparse
from src.controllers.controller import Controller
from src.views.view import View

def main():
    # Construction du parser d’arguments
    parser = argparse.ArgumentParser()
    # Ajout des options 
    parser.add_argument("--csv", default="src/ressources/liste_actions.csv")
    parser.add_argument("--budget", type=float, default=500.0)
    parser.add_argument("--algo", choices=["brute", "greedy"], default="greedy")
    # Lit la ligne de commande, ce que je tape après python main.py.
    args = parser.parse_args()

    controller = Controller(csv_path=args.csv, budget=args.budget, algo=args.algo)
    summary, picks, cost = controller.run()

    view = View()
    view.render(summary, picks, cost, budget=args.budget)

if __name__ == "__main__":
    main()
