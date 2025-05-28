def caesar(text, shift, mode):
   
# 'text' est ce qu’on veut chiffrer ou déchiffrer.
# 'shift' est le nombre de lettres de décalage ; en gros, si on chiffre la lettre C avec un décalage de 3, on obtient F.
# 'mode' sert à choisir si on veut chiffrer ou déchiffrer (on suppose qu’on connaît le décalage, on veut juste pas le faire a la main...).

   result = ""

# Une chaîne vide où on mettra notre résultat final, basique.

   for char in text:
       if char.isalpha():
           
# Pour chaque caractère du texte, si c’est une lettre...

           if char.isupper():
               base = ord('A')
           else:
               base = ord('a')
               
# On vérifie si c’est une majuscule ou une minuscule, puis on définit la base avec le code ASCII de 'A' (65) ou 'a' (97).

           if mode.lower() == 'encrypt':  # au cas où des gens tapent "ENCRYPT" en caps lock.
               direction = shift
           else:
               direction = -shift
               
# Ici, on détermine si on va "en avant" (chiffrement) ou "en arrière" (déchiffrement).
# Si on chiffre un C avec +3, on obtient F ; si on déchiffre, on revient vers A.

           calcul = (ord(char) - base + direction)%26

# Cette partie est un peu délicate, on joue avec les valeurs ASCII. En gros, si on fait ord("C"), ça nous donne 67, puis on soustrait la base (la base étant ord("A") vu qu'on a prit C majuscule).
# Donc ici, on obtient la valeur « 2 », c’est cette valeur-là qu’on ajoute (ou qu’on soustrait, selon le mode choisi, mais imaginons qu’on veuille chiffrer) avec le décalage (prenons 3 pour notre exercice).
# Ça nous donne un total de 5, ce qui correspond à la position d’un caractère invisible… pour l'instant. En plus de ca, on met tout en modulo 26 pour s’assurer que le résultat ne dépasse jamais 25 (par exemple, si on prend Z et un décalage de 5, on aurait un souci sans ce %26).

           result += chr(base+calcul)

# Et là, comme par magie : on convertit à nouveau le résultat en lettre avec chr() en replaçant la base, genre 5 + 65 = 70 = 'F'.

       else:
           result += char

# Si le caractère n’est pas une lettre (genre un espace, un point...), on le laisse tel quel.
            
   return result
            
print(caesar('Chat', 3, 'encrypt'))

# C’est littéralement un projet de débutant (enfin, plus ou moins, j’ai essayé de rendre ça clair).

# Astuce bonus : si tu veux voir tous les caractères ASCII :
# for i in range(128):
#     print(f"{i} -> {chr(i)}")   
