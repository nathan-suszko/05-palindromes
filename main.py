"""module de vérification d'un palindrome"""
import string
#### Fonction secondaire

def ispalindrome(p):
    """Vérifie si p est un palindrome"""
    # votre code ici
    p = p.lower()

    p = p.replace('é', 'e')
    p = p.replace('è','e')
    p = p.replace('ê', 'e')
    p = p.replace('ë','e')
    p = p.replace('à','a')
    p = p.replace('â','a')
    p = p.replace('ù','u')
    p = p.replace('û','u')
    p = p.replace('ç','c')
    p = p.replace('î','i')
    p = p.replace('ï','i')
    p = p.replace('ô','o')

    interdits = string.punctuation + " "
    for char in interdits:
        p = p.replace(char, "")

    if p == p[::-1]:
        return True
    return False

#### Fonction principale

def main():
    """fonction principale pour tester """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
