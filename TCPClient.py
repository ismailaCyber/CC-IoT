import socket
import ssl

# Configuration du client
HOST = 'localhost'
PORT = 8888
CERTFILE = '/home/ismael/Documents/nfv/certificat.pem'

# Création d'un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuration du socket pour accepter les connexions SSL
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(CERTFILE)
sock_ssl = context.wrap_socket(sock, server_hostname=HOST)

# Connexion au serveur
sock_ssl.connect((HOST, PORT))

# Envoi de données au serveur
data = b'Hello Serveur!'
sock_ssl.sendall(data)

# Réception de la réponse du serveur
response = sock_ssl.recv(1024)
print(response.decode())

# Fermeture de la connexion SSL
sock_ssl.shutdown(socket.SHUT_RDWR)
sock_ssl.close()