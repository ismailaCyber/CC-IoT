import ssl
import http.client

# Adresse du serveur HTTPS
HOST = 'localhost'
# Port HTTPS par défaut
PORT = 443
# Chemin de l'URL à récupérer
PATH = '/'

# Configuration du contexte SSL/TLS
context = ssl.create_default_context()

# Connexion au serveur HTTPS
conn = http.client.HTTPSConnection(HOST, PORT, context=context)

# Envoi de la requête HTTPS
conn.request('GET', PATH)

# Récupération de la réponse HTTPS
response = conn.getresponse()

# Affichage de la réponse HTTPS
print(response.status, response.reason)
print(response.read().decode())

# Fermeture de la connexion HTTPS
conn.close()