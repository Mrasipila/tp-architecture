## Réalisation d'une architecture distribuée pour un site de "booking"


Pour démarer le serveur veuillez executer les commandes : 
```
flask init-db  
flask run
```
Le projet a été developpé sur l'IDE Python PyCharm
Pour accéder à la page aller à l'adresse "http://127.0.0.1:5000/index"

Ce projet consiste en la réalisation d'une architecture distribuée pour un site de "booking" dans un delai de une semaine après le cours.
Notre site représenté par la vue dans l'architecture et par les fichiers html/css dans notre répertoire contient 3 interfaces.

> La vue principale du site qui envoie le formulaire 

> La vue qui confirme la transaction 

> La vue qui affiche les transactions


Oui je l'ai utilisé elle se trouve dans le fichier API.py et son appel dans vue.py du webserver flask. Le webserver va faire un appel et stocker les données dans la base de données SQLite3 dont l'instance est hebergée dans le fichier "instance". Si vous voulez recharger la db il faudra executer la commande "flask init-db" sur le shell de l'os (représenté par le signe $).  


Notre POST du formulaire est idempotent car on désactive le bouton lors de l'envoi de la requête grâce à Jinja. 

L'avantage de Python dans ce projet est que le code peut être être utilisé sur n'importe quelle machine grâce à venv. 

J'ai utilisé la librairie Requests pour les appel sur l'API REST. 

Sur la plateforme de dev j'ai accès aux logs des échanges de requêtes serveur/clients
