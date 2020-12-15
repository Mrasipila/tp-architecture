## Réalisation d'une architecture distribuée pour un site de "booking"


Pour démarer le serveur veuillez executer les commandes : 
```
flask init-db  
flask run
```

Ce projet consiste en la réalisation d'une architecture distribuée pour un site de "booking".
Notre site représenté par la vue dans l'architecture et par les fichiers html/css dans notre répertoire contient 3 interfaces.

- La vue principale du site qui envoie le formulaire 

- La vue qui confirme la transaction 

- La vue qui affiche les transactions

Notre webserver réalisé en Python sur Flask va instancier une base de donnée contenant les vols et communiquer avec une API REST dans le fichier API.py.
Les modules de API.py seront utilisé par vue.py du webserver flask. Le webserver va faire un appel et stocker les données dans la base de données SQLite3
dont l'instance est hebergée dans le fichier "instance". Si vous voulez recharger la base de données il faudra executer la commande "flask init-db" sur le
shell de l'os (représenté par le signe $).  
  
Notre POST du formulaire est idempotent car on désactive le bouton lors de l'envoi de la requête grâce à Jinja. 

Sur la plateforme de dev j'ai accès aux logs des échanges de requêtes serveur/clients

![alt text](https://github.com/Mrasipila/tp-architecture/blob/IA1-Befa-Airlines/IA1-Befa-Airlines/projet/images/dev.PNG)

Pour accéder à la page aller à l'adresse "http://127.0.0.1:5000/index"
