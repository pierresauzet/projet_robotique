import numpy as np 
# les variables :::::::::::::::::::::::::: 
a = 1 # une variable de type entier 
b = 2 # une duxieme variable de type entier 
c = 3.2 # une variable de type reel ( float )
text = " Chaine de caracteres " # une variable de type chaine de caracteres 
bool_var1 = None # une variable booleenne 
bool_var2 = True 
print ( " Variables : " ,a ,b ,c , text , " \ n " ) 
# operateurs :::::::::::::::::::::::::::::: 
addition = a + b 
soustraction = b - a 
produit = a * b 
division = a / b 
division2 = a / c 
puissance = b ** b 
print ( " Operateurs :\ n " ) 
print ( " Addition : " , addition , " \ n " ) 
print ( " Soustraction : " , soustraction , " \ n " ) 
print ( " Produit : " , produit , " \ n " ) 
print ( " Division ( floor division ) : " , division , " \ n " ) 
print ( " Division2 : " , division2 , " \ n " ) 
print ( " puisssance X ^ Y : " , puissance , " \ n " ) 
vecteur_int = np . array ([1 ,2 ,3 ,4]) # vecteur d ’ entiers 
vecteur_float = np . array ([1.6 ,2.8 ,3.3 ,4.1]) # vecteur de reels
matrice = np . array ([[1 ,2 ,] ,[3 ,4]]) # création d ’ une matrice
matrice_zeros = np . zeros ((3 ,4)) # matrice nulle 3 x4 
matrice_ones = np . ones ((2 ,5)) # matrice unitaire 2 x5 
identite = np . eye (3) # matrice identite 
vecteur_float . size # renvoir le nombre d ’ elements 
matrice_zeros . shape # renvoie le nombre lignes ,n , et colonnes ,m , (n , m )
vecteur_int [0] # accede à la valuer du premier element
identite [1 ,2] # accede a la valeur de l ’ element ( ligne , colonne ) 
