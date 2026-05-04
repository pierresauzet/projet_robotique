### EXERCICE 1 :
A partir du code fournit dans l'exmple : Ex1 : API thymiodirect — Connexion et structure et de la fonction obs, nous pouvons ainsi 
récupérer les différentes données des capteurs avant permettant la détection d'obstacle

### EXERCICE 2 :
En utilisant ex2.py— Évitement d'obstacles & contrôle clavier et le code précédent, nous pouvons ainsi récupérer les valeurs de boutons "button.center" et 
"button.forward" nous permettant ainsi de détecter l'appui à partir d'un test et de déclancher les fonctions avancer où reculer

### EXERCICE 3 :
Pour cet exercice, il suffit de faire une boucle sur les différents capteurs et de tester si cette distance est inferieur ou égale à 140 000/valeurs

### EXERCICE 4 :
Pour cet exercice, les fonctions tourner à gauche, tourner à droite, devront être implémentées et fonctionnent en activant uniquement un moteur sur deux. Pour chaques tour, si le capteur de suivi de ligne gauche détecter
du noir, le robot tournera a gauche et si celui ci détecte du noir à droite, celui ci tournera à droite

### Exercice 5 :
Dans cet exercice, on peut réutiliser les différentes fonctions de l'exercice précédent tout en rajoutant une fonction de recule (fonction avancer avec des valeurs négatives) tout en modifiant les seuils et les capteurs:
Le seuil devient ici une valeur pondéré gauche ou droite, si toutes ces sommes dépassent le seuil, il recule donc

### EXERCICE 6 :
Non traité
### EXERCICE 7 :
Non traité
### Exercice 8 :
Non traité
### Exercice 9 : 
Ici, récupérant deux robots différents et en créant deux fonctions d'observations distinctes (une pour chaques robots) nous pouvons ainsi nous retrouver avec deux robots dont le but va être différentes
Le robot leader avancera constamment alors que le robot suiveur lui détectera lorsque ses capteurs avant auront une valeur suppérieur à 15*14000/valeur et avancera pour la garder inferieur à celle ci 
### Exercice 10 :
Pour cet exercice, le même fonctionnement avec deux fonctions d'observations sera réutilisé, cependant une machine à état sera utilisé :
- Les robots ont un état actif par défaut
- Si les capteurs détecte un obstacle, le deuxième robot passe à un état d'attente pendant 2 seconde
- le premier robot utilise un algorithme similaire à l'exercice 5 afin d'esquiver l'obstacle


### Implémentation du convoi 

Notre étant le numéro, on nous a assigné ce convoi : 

Groupe 4 : Timide / Dirigé / Attraction-Répulsion 

Nous avons donc déclaré trois robots, et trois fonctions obs décrivant chaque comportement. 

Après implémentation, nous nous sommes rendu compte que la logique du convoi ne permettait pas un évitement. 

2 des robots (timide et attraction/repulsion) possèdent un comportement linéaire sans aucun mouvement de virage, ce qui les empêche d’esquiver un obstacle. 

Le robot au comportement “dirigé” s’est néanmoins montré intéréssant, étant capable de suivre un objet devant lui (tourne à droite s’il détecte un objet à droite, à gauche si détecte à gauche, sinon avance. 

Il fait donc un très bon suiveur, il faut donc juste trouver un bon comportement pour le leader du convoi. 

### Amélioration du convoi 

Nous avons donc choisi d’ajouter un robot de type anxieux, capable de longer un obstacle tout en l’évitant. 

Ce nouveau convoi est celui décrit dans convoi_2_fonctionnel, et visible dans la vidéo. 

![seance_4/]
