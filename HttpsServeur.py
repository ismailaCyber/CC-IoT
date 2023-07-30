import ssl
import http.server
import socketserver

# Port utilisé pour le serveur
PORT = 443

# Chemin vers le certificat SSL/TLS
CERTFILE = '/home/ismael/Documents/nfv/certificat.pem'
# Chemin vers la clé privée SSL/TLS
KEYFILE = '/home/ismael/Documents/nfv/cle_privee.pem'

# Configuration du serveur avec le certificat et la clé privée SSL/TLS
https = socketserver.TCPServer(('localhost', PORT), http.server.SimpleHTTPRequestHandler)
https.socket = ssl.wrap_socket(https.socket, certfile=CERTFILE, keyfile=KEYFILE, server_side=True)

# Lancement du serveur HTTPS
print("Serveur HTTPS en cours d'exécution sur le port :", PORT)
https.serve_forever()