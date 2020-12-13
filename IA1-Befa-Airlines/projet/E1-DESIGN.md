Pour démarer le serveur veuillez executer les commandes : flask init-db ET flask run
Le projet a été developpé sur l'IDE Python PyCharm

# Design : 

Dans notre situation où l’on doit communiquer avec 2 services (API & BDD), notre base de données personnelle ainsi qu’une API hébergée sur un site « .io ». L’architecture de bonne pratique ayant montré dans le temps des avantages de performance et de résiliences est L’architecture de micro-services. Mais n’est pas obligatoire, cela dépend du contexte. On va éviter l’architecture monolithique. 


Ci-dessous le modèle que nous allons utiliser d’une architecture de micro-services simple. Nous n’avons pas besoin de partir sur une architecture Backend for Frontend car il n’y a qu’un seul utilisateur pour cette application. Nous aurons 3 couches. 

![alt text](https://github.com/Mrasipila/tp-architecture/blob/IA1-Befa-Airlines/IA1-Befa-Airlines/projet/Architecture.png)

Non allons partir sur une **Presentation Layer** en : HTML, CSS

**Une Application Layer** en :
Flask

**Une Data Layer** en :
SQLite3 et API Rest

Flask pour le control qu’il nous donne sur la gestion des différents services et puisqu’il s’agit d’une application légère. 

## On a rendu le POST Idempotent en desactivant le bouton à l'appui 

![alt text](https://github.com/Mrasipila/tp-architecture/blob/IA1-Befa-Airlines/IA1-Befa-Airlines/projet/Schéma.png)

## Motif d'architecture MVVM :
* **View :** fichiers HTML/CSS
* **Model :** données SQLITE, JSON
* **View-Model :** vue.py
* **View-Controller :** API.py 

![alt text](https://github.com/Mrasipila/tp-architecture/blob/IA1-Befa-Airlines/IA1-Befa-Airlines/projet/MVVM.png)

On choisit ce motif car la vue de l'utilisateur n'est pas stateless, de plus on a besoin de représenter la données, de formatter la données par une classe à cause des différents services nous offrant de la data. 

## Améliorations : 
Utilisation du javascript pour la génération des options des listes en innerHTML.  
La création de login, mot de passe, authentification pour avoir un espace en fonction de l'user enregistré dans la base de données  
