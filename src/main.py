# src/main.py
from controllers.fileActions import optimiser
from views.afficherResultat import afficher_resultat

def main():
    csv_path = "ressources/liste_actions.csv"  
    budget = 500

    # Affichage du résultat
    resume, picks, cost = optimiser(csv_path, budget)
    afficher_resultat(resume, picks, cost)

if __name__ == "__main__":
    main()

