import socket
import ssl

SERVER_HOST = 'localhost'
SERVER_PORT = 8888

# Création d'un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mettre le socket en mode écoute
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f"Serveur en écoute sur {SERVER_HOST}:{SERVER_PORT}")

while True:
    # Attendre une connexion d'un client
    client_socket, client_address = server_socket.accept()
    print(f"Nouvelle connexion de {client_address}")

    # Créer un contexte SSL/TLS sécurisé
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile="/home/ismael/Documents/nfv/certificat.pem", keyfile="/home/ismael/Documents/nfv/cle_privee.pem")

    # Mettre en place la couche SSL/TLS sécurisée
    secure_client_socket = ssl_context.wrap_socket(client_socket, server_side=True)

    # Recevoir des données du client
    data = secure_client_socket.recv(1024)
    print(f"Données reçues : {data.decode()}")

    # Envoyer une réponse au client
    message = "Bonjour, client !"
    secure_client_socket.send(message.encode())

    # Fermer la connexion sécurisée avec le client
    secure_client_socket.close()