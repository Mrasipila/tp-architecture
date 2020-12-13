Pour démarer le serveur veuillez executer les commandes : flask init-db ET flask run
Le projet a été developpé sur l'IDE Python PyCharm

# Design : 

Dans notre situation où l’on doit communiquer avec 2 services (API & BDD), notre base de données personnelle ainsi qu’une API hébergée sur un site « .io ». L’architecture de bonne pratique ayant montré dans le temps des avantages de performance et de résiliences est L’architecture de micro-services. Mais n’est pas obligatoire, cela dépend du contexte. On va éviter l’architecture monolithique. 


Ci-dessous le modèle que nous allons utiliser d’une architecture de micro-services simple. Nous n’avons pas besoin de partir sur une architecture Backend for Frontend car il n’y a qu’un seul utilisateur pour cette application. 
