# Paxos

# Premier note

Paxos Essential fournit des implémentations de base de l'algorithme Paxos. La caractéristique de cette mise en œuvre, par rapport à d'autres open-source et Implémentations Librement disponible, est que cette bibliothèque est indépendante des domaines d'application et les infrastructures de réseaux. Alors que la plupart des Paxos Implémentations a profondément et inextricablement intégré la logique spécifique à l'application Dans cette mise en œuvre se concentre sur l'algorithme Paxos encapsuler Dans les classes opaques et facilement réutilisables.

Cette bibliothèque fournit Paxos année algorithmiquement correcte qui peut être utilisé à des fins éducatives, en plus de l'utilisation directe dans les applications en réseau de mise en œuvre. La mise en œuvre Ceci est spécialement conçu pour figurer à la fois la compréhension essentielle de Paxos algorithme ainsi que les considérations pratiques qui doivent être prises en compte pour une utilisation dans le monde réel.

Implémentations à la fois Python et Java est fourni.

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
