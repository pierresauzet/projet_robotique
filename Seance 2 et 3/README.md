#Projet Robotique

	Ce projet à pour but de se familiariser avec les robots Thymio et de leur comportement au travers de différents exercices

#Installation

Afin de pouvoir lancer les programmes, le logiciel webots sera nécessaire. Le dossier ci joint contiens à la fois les documents démonstratifs et explicatifs tel que les vidéos et le readme.
Afin de lancer les simulations et de tester le premier convois, il suffit de changer le controller du deuxième robot et de mettre l'indécis 1 de même pour le deuxième robot mais avec anxieux
Pour le deuxième convois, il suffit de rechanger les controllers 1 et 2 pour indécis 2.

#Explication

Le premier convois ne peux pas fonctionner par principe car même si l'anxieux peut faire le tour sans problème, l'indécis va faire que avancer si il n'y as pas de mur et reculer si il en détecte un. Ainsi on va se retrouver avec un robot qui va avancer et reculer au premier obstacle avec l'anxieux en fin de convois qui lui va essayer de contourner l'indécis coincé.

Le deuxième convois lui est plus convenable puisque l'indécis à été codé d'une différente manière. Si le capteur droit détecte un objet (si le meneur tourne, c'est donc le capteur droit du robot juste après qui va détecter un changement), alors le robot va tourner du même côté que le meneur, si le capteur gauche détecte un changement du côté gauche, le robot va donc tourner du côté gauche tout en avançant tant que le robot détecte un objet à moyenne distance (s'arrête si le meneur est perdu ou si le meneur est vraiment trop proche).

Ici, plusieurs fonctions ont été crées :
	-avancer(vitesse)
	-tourner_g(vitesse)
	-tourner_d(vitesse)
	-delay(s)

Avancer :
comme son nom l'indique cette fonction à pour unique but de mettre tous les moteurs à une certaine vitesse permettant au robot d'avancer.

Tourner_g/d :
Les deux fonctions ont comme même principe de mettre un moteur à une vitesse et l'autre à la vitesse inverse (permet de tourner sans avancer ce qui ne serais pas le cas pour si l'autre moteur était à 0) et permet donc de faire des tournants précis sans avancer.

Delay :
Cette fonction est assez simple et permet uniquement de faire une boucle permettant au robot de rester dans l'état actuel et ne pas passer à la suite. Elle utilise la fonction getTime permettant de compter à partir d'un certains temps et de quitter la boucle quand getTime+delay est atteint. Ce delay est particulièrement utile afin de rectifier certaines trajectoire par exemple les détections à gauches qui sont particulièrement dur à detecter et mettre le robot le plus parallèle possible au mur permettant un gain de temps car celui ci va moins frotter contre le mur.

Le fonctionnement de l'anxieux est un comportement particulièrement compliqué à mettre en œuvre particulièrement car le robot ne possède pas de capteur gauche permettant de détecter si celui ci se rapproche vraiment du mur ou pas. 
Ainsi, notre algorithme est basé sur une détection d'obstacle il tourne à droite, sinon celui ça va aller vers la gauche tout en avançant



