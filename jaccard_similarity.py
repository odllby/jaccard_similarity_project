import re
from typing import List, Tuple, Set , Union

# Normalisation et Tokenization
# Cette fonction prend une chaîne de texte en entrée et retourne un ensemble de tokens uniques.
def tokenize_text(text: str) -> Set[str]:
    # Convertir le texte en minuscules
    text_normalized = text.lower()
    # Utiliser une expression régulière pour extraire les mots
    tokens = re.findall(r'\b\w+\b', text_normalized)
    # Retourner un ensemble de tokens uniques
    return set(tokens)

#  -----------------  Fonction principales de similutde de Jaccard  -----------------
# Cette fonction calcule la similarité de Jaccard entre deux ensembles de tokens.

def calculate_jaccard_similarity(prhase1: str, phrase2: str) -> float:
    """Calcule la similarité de Jaccard entre deux phrases."""
    
    set1 = tokenize_text(prhase1)
    set2 = tokenize_text(phrase2)
    
    # Gerer les cas ou les ensembles sont vides
    if not set1 and not set2:
        return 0.0 # Si les deux ensembles sont vides, ils sont identiques
    
    # Trounver l'intersection et l'union des deux ensembles
    intersection = set1.intersection(set2)
    intersection_size = len(intersection)
    
    # Trouver l'union des deux ensembles
    union = set1.union(set2)
    union_size = len(union)
    
    # Appeler la formule de Jaccard
    jaccard_score  = intersection_size / union_size
    return jaccard_score

# Ajouton un test simple pour verifier le fonctionnement de la fonction
if __name__ == "__main__":
    print("\n--- Calculateur Interactif de Similitude de Jaccard ---")
    
    # Utilisation de input() pour lire l'entrée de l'utilisateur
    p1 = str(input("Entrez la première phrase (A) : "))
    p2 = str(input("Entrez la deuxième phrase (B) : "))

    # Calcul du score
    score = calculate_jaccard_similarity(p1, p2)

    # Affichage détaillé des ensembles (utile pour la compréhension)
    set_a = tokenize_text(p1)
    set_b = tokenize_text(p2)
    intersection_set = set_a.intersection(set_b)
    union_set = set_a.union(set_b)

    print("\n--- Détails de l'Analyse ---")
    print(f"Ensemble A (Unique) : {set_a}")
    print(f"Ensemble B (Unique) : {set_b}")
    print(f"Intersection (Commun): {intersection_set} (Taille: {len(intersection_set)})")
    print(f"Union (Total Unique): {union_set} (Taille: {len(union_set)})")

    print("\n--- Résultat Final ---")
    print(f"Le Score de Similitude de Jaccard est : {score:.4f}")
    
    # Interprétation simple du score
    if score >= 0.8:
        print("Les phrases sont très similaires.")
    elif score > 0.3:
        print("Les phrases partagent un certain chevauchement lexical.")
    else:
        print("Les phrases sont peu similaires.")