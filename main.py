import time
import random

from setup import setup
from lcs import LCS
from dataset_generation.helper_functions import generate_dataset
from dataset_generation.models.dataset_model import Dataset
from genetic_algorithm.models.selection_method_model import SelectionMethod


def main():
    print("Bienvenue dans ce programme de recherche de la plus longue sous-séquence commune!")

    print("\nGénération du dataset en cours...")
    alphabet = input("Entrez une liste d'alphabet séparée par des espaces : ").split()
    num_strings = int(input("Entrez le nombre de chaînes de caractères : "))
    length = int(input("Entrez la longueur des chaînes de caractères : "))

    a = input("Toutes les chaînes auront-elles la même longueur ? (o/n) : ").lower()
    if a == 'o':
        var_length = False
    else:
        var_length = True

    dataset: Dataset = generate_dataset(alphabet=alphabet, seq_length=length, var_length=var_length,
                                        nb_seqs=num_strings)

    print("\nInfos dataset :")
    print(f"\t- Alphabets : {alphabet}")
    print(f"\t- Nombre de chaînes de caractères : {num_strings}")
    print(f"\t- Taille des chaînes de caractères : {length}")
    if a:
        print("\t- Toutes les chaînes auront la même taille")
    else:
        print("\t- Toutes les chaînes n'auront pas la même taille")

    while True:
        print("\nChoisissez un algorithme à exécuter :")
        print("1. Algorithme naïf")
        print("2. Algorithme génétique")
        print("3. Quitter")
        choice = input("Votre choix : ")

        if choice == '1':
            print("\nLancement de l'algorithme naïf!!!")
            for i in range(5):
                time.sleep(0.2)
                if i == 0:
                    print("En recherche.", end='', flush=True)
                else:
                    print(".", end='', flush=True)
            print()
            print("Patientez encore un moment...")
            start = time.process_time()
            lcs = LCS.exact_method(dataset.sequences)
            end = time.process_time()

            if len(lcs) == 0:
                print("\nAucune sous-séquence trouvée !")
            elif len(lcs) == 1:
                print(f"\nLongest Common Subsequence (Méthode exacte) : {lcs[0]}")
                print(f"Temps d'exécution : {end - start} secondes")
            else:
                b = []
                for a in lcs:
                    b.append(a[0])
                print(f"\nLongest Common Subsequence (Méthode exacte) : {b}")
                print(f"Temps d'exécution : {end - start} secondes")

        elif choice == '2':
            max_gens = int(input("\nSpecifier le nombre de générations (nombre d'itérations) : "))
            mutation_rate = float(input("Specifier le taux de mutation (entre 0 et 1) : "))
            population_size = int(input("Specifier la taille d'une population d'une génération : "))

            print("\nLancement de l'algorithme génétique!!!")
            for i in range(5):
                time.sleep(0.2)
                if i == 0:
                    print("En recherche.", end='', flush=True)
                else:
                    print(".", end='', flush=True)
            print()
            print("Patientez encore un moment...")
            start = time.process_time()
            lcs = LCS.genetic_algorithm(chromosomes=dataset.sequences, max_gens=max_gens, mutation_rate=mutation_rate,
                                        population_size=population_size, selection_method=SelectionMethod.TOURNAMENT)
            end = time.process_time()

            print(f"\nLongest Common Subsequence (Méthode optimale) : {lcs[0]}")
            print(f"Temps d'exécution : {end - start} secondes")

        elif choice == '3':
            print("\nMerci d'avoir utilisé ce programme. À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez choisir à nouveau.")


if __name__ == '__main__':
    setup()
    main()
