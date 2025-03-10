from math import sqrt
from Estrella import Estrella

def main():
    # Ejemplo de uso
    estrella1 = Estrella(1, 2, 3)
    estrella2 = Estrella(4, 5, 6)

    print(estrella1)  # Output: (1, 2, 3)
    print(estrella2)  # Output: (4, 5, 6)
    print(estrella1.galaxia())  # Output: Galaxia Desconocida
    print(estrella2.galaxia())  # Output: Galaxia Desconocida
    print(estrella1.distancia(estrella2))  # Output: 5.196152422706632
    print(estrella2.distancia(estrella1))  # Output: 5.196152422706632

if __name__ == "__main__":
    main()