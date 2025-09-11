# AlgoInvest&Trade — Optimisation d’investissement (Brute-Force & Glouton)

Projet pédagogique d’optimisation d’un portefeuille d’actions sous **contrainte de budget (≤ 500€)**.  
Deux approches sont fournies :  
- **Section 1 — Brute-force** : explore toutes les combinaisons (référence optimale, mais coûteux).  
- **Sections 2–3 — Glouton (Greedy)** : tri par `%` décroissant, prix croissant, profit € décroissant → ultra-rapide, assumé non optimal.



##  Objectif
 Maximiser le profit total après 2 ans en sélectionnant des actions (0/1 par action) sans dépasser le budget.

**Colonnes dans le CSV :**  
- `Actions #`   
- `Coût par action (en euros)`   
- `Bénéfice (après 2 ans)`  en **%**



##  Structure du dépôt

.
├── bruteForce.py          # Section 1 
├── optimized.py           # Sections 2/3 
├── controller.py          # orchestre 
├── view.py                # Rendu console 
├── pseudoCodeOptimized.pdf# pseudo code algorithme optimized           # 
├── pseudoCodeBruteForce.pdf# pseudo code algorithme brute de force
├── dataset1.csv           # Jeu de données 1
├── dataset2.csv           # Jeu de données 2 
├── liste_actions.csv      # liste de données (20actions)
├── slides.pdf             # Slides de soutenance 

##  Prérequis & installation
- **Python **
- Pas de dépendances obligatoires pour l’exécution des algos.

Cloner et se placer dans le dossier :

git clone <votre_repo>.git
cd <votre_repo>


##  Utilisation

### 1- Exécuter l’algo glouton 
python main.py --csv src/ressources/dataset1.csv --budget 500 --algo greedy

### 2- Exécuter l’algo brute-force 
python main.py --csv src/ressources/listeactions.csv --budget 500 --algo greedy

##  Algorithmes

### Brute-force (optimale)
- **Idée** : explorer tous les sous‑ensembles d’actions sous la contrainte de budget, conserver celui au **profit total maximal**.
- **Complexité** : **O(2^n)** en temps, **O(n)** en mémoire.
- **Usage** : validation / pédagogie sur **petites** tailles.

### Glouton (greedy) 
- **Heuristique** : trier par *(% desc, prix asc, profit € desc)* puis ajouter tant que le budget le permet.
- **Complexité** : O(n log n) (tri) + O(n) (sélection) ⇒ global O(n log n), mémoire O(n).
- **Avantages** : temps de réponse ≪ 1s, simple à expliquer aux équipes métier.
- **Limite** : non optimal dans certains cas (classiques du sac à dos 0/1).


##  Performances (mesures fournies)
| Dataset  | Nb actions | Brute-force | Greedy      | Gain (absolu) | Accélération (min.)   |
| dataset1 | 20         | 1.7604 s    | 0.0000 s*   | ≈ **1.7604 s**| **≥ 35 000×**         |
| dataset2 | 1000       | Impossible  | 0.0008 s    | N/A           | N/A                   |


## 🔎 Qualité des données (synthèse d’exploration)
| Dataset          | Lignes totales | Noms uniques | Doublons | Valides (prix>0 & %>0) |
|------------------|---------------:|-------------:|---------:|-----------------------:|
| dataset1.csv     | 1001           | 1000         | 1        | **956 (95,5 %)**       |
| dataset2.csv     | 1000           | 998          | 2        | **541 (54,1 %)**       |
| liste_actions.csv| 20             | 20           | 0        | **20 (100 %)**         |

**Traitement CSV robuste** : normalisation des virgules, retrait des symboles `%/€`, filtrage des valeurs ≤ 0 ou mal formées.  
Les algorithmes opèrent **uniquement** sur les lignes valides. 

##  Sorties & formats
- **Console** : résumé, coût total, profit total, sélection (picks), temps d’exécution.
- **Slides** : `slides.pdf`.

##  Limites & pistes d’amélioration
- **Non optimalité** du greedy dans certains cas (sac à dos 0/1).  
- Ajouter des **filtres métier** (prix min/max, % min, secteurs exclus).   


