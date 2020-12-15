## Réalisation d'une architecture distribué pour un site de "booking"


Pour démarer le serveur veuillez executer les commandes : flask init-db ET flask run
Le projet a été developpé sur l'IDE Python PyCharm
Pour accéder à la page aller à l'adresse "http://127.0.0.1:5000/index"



Oui je l'ai utilisé elle se trouve dans le fichier API.py et son appel dans vue.py du webserver flask. Le webserver va faire un appel et stocker les données dans la base de données SQLite3 dont l'instance est hebergée dans le fichier "instance". Si vous voulez recharger la db il faudra executer la commande "flask init-db" sur le shell de l'os (représenté par le signe $).  


Notre POST du formulaire est idempotent car on désactive le bouton lors de l'envoi de la requête grâce à Jinja. 
