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

#Implémentations

python

#essential.java

Ce module fournit une mise en oeuvre directe et minimale de l'algorithme Paxos essentiel. L'objectif principal de ce module est de l'éducation, car il permet un contraste facile entre la mise en œuvre de l'algorithme et celui de la pure pour des raisons pratiques améliorées.

#practical.java

Ce module améliore l'algorithme Paxos essentiel et ajoute le support pour les choses de suivi politica que le leadership, NACKs et persistance de l'état.

#functional.java

Ce module fournit une Paxos entièrement fonctionnelle que l'application utilise un mécanisme simple pour détecter l'échec du leadership coeur ne bat plus et de récupération initiés.

#external.java

Ce module fournit la version de practical.py Cette année prend en charge l'utilisation du leadership de gestion externe pour piloter des détecteurs de défaillance améliorée. Ce module ne fournit pas une solution entièrement fonctionnelle à la direction de la gestion, comme le fait functional.py. Cependant, il sert de base pour le leadership avril beaucoup plus souple, spécifique à l'application de gestion.

#Test

Le répertoire racine de test du référentiel de code source contient les fichiers unittest Utilisé pour exercer la mise en œuvre. Les tests primaires est écrit en Python et correspondent aux modules essentiels, pratiques, fonctionnels et durables. Les tests de Java, qui est également écrit en Python, enveloppent les classes Java avec une interface compatible et utiliser les tests unitaires en Python pour exercer l'application Java. L'interpréteur Jython est nécessaire pour les tests en cours d'exécution CES, mais il est pas nécessaire lors de l'exécution.
