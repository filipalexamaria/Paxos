# Paxos

#Important

Paxos est le plus important algorithme dans la distribution de calcul 

#Problème de consensus
-Validité- seulement les valeurs propose peut etre decide; 

-Acord-  un noeud peut decide une valeur; 

-Intégrité- chaque noeud peut decide un valeur une fois;

-Termination -chaque noeud decide en fin une valeur ;

#Hypothèses

-Partielle - pour la partie termination ;

-Echouer-modul bruyant-class abstract;

-duplication de message, réordonnancement, moins;

#Elire un seul auteur en utilisant omega

-auteur impose sa proposition à tout le monde

-tout le monde decide

#Problem avec omega 

-plusieurs noeuds peuvent être initialement proposants
