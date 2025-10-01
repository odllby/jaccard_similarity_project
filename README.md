Coefficient de Similitude de Jaccard (Python)

Ce projet implémente le Coefficient de Similitude de Jaccard pour mesurer le degré de chevauchement entre deux phrases basées sur leurs mots.

Le score de Jaccard est calculé comme suit :
J(A,B)=∣A∪B∣∣A∩B∣​
🚀 Comment Exécuter le Programme

Le script jaccard_similarity.py peut être exécuté directement dans votre terminal (via Python) et passera en mode interactif pour vous permettre de comparer deux phrases de votre choix.
Prérequis

Vous devez avoir Python (version 3.x) installé. Aucune bibliothèque externe n'est nécessaire au-delà des modules standards (re et typing).
Instructions

    Naviguer vers le répertoire du projet dans votre terminal.

    Lancer le script avec Python :

    python jaccard_similarity.py

    Le programme vous demandera ensuite d'entrer les deux phrases à comparer.

🧐 Détails et Algorithme (Étapes)

Le calcul se déroule en quatre étapes principales :
Étape 1 : Tokenisation et Normalisation

La fonction tokenize_text nettoie chaque phrase :

    Mise en minuscules (normalisation).

    Extraction des mots (tokenisation) et suppression de la ponctuation.

    Conversion en un ensemble de mots uniques (Set).

Étape 2 : Calcul de l'Intersection (Numérateur)

Nous trouvons la taille des mots communs aux deux ensembles (∣A∩B∣).
Étape 3 : Calcul de l'Union (Dénominateur)

Nous trouvons la taille totale de tous les mots uniques des deux ensembles combinés (∣A∪B∣).
Étape 4 : Score Final

Le score est la division du Numérateur (Intersection) par le Dénominateur (Union). Le résultat est un score entre 0.0 (aucune similarité) et 1.0 (similarité parfaite).
✅ Exemples de Tests

Voici trois exemples pour illustrer comment le score reflète la similarité des phrases :

Phrase A
	

Phrase B
	

Intersection
	

Union
	

Score Jaccard

P1 : Le chat dort.
	

P2 : Le chien dort.
	

{'le', 'dort'} (2)
	

{'le', 'chat', 'dort', 'chien'} (4)
	

2 / 4 = 0.5000

P3 : Le soleil est chaud.
	

P4 : La lune est froide.
	

{'est'} (1)
	

{'le', 'soleil', 'est', 'chaud', 'la', 'lune', 'froide'} (7)
	

1 / 7 ≈ 0.1428

P5 : Python est génial!
	

P6 : python est génial!
	

{'python', 'est', 'génial'} (3)
	

{'python', 'est', 'génial'} (3)
	

3 / 3 = 1.0000
🤝 Contribution (Workflow Git)

Si ce projet est partagé en équipe, suivez le flux de travail Git standard :

    Cloner le dépôt : git clone <URL>

    Créer une nouvelle branche pour les fonctionnalités/corrections : git checkout -b ma-nouvelle-fonctionnalite

    Apporter vos modifications.

    Ajouter et Commiter vos changements : git add . et git commit -m "feat: [Description de la fonctionnalité]"

    Pousser la branche : git push origin ma-nouvelle-fonctionnalite

    Ouvrir une Pull Request sur la plateforme (GitHub/GitLab) pour révision.