import socket

mon_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mon_socket.bind(('',15555)) # ecoute sur le port 155555 toutes les interface local


while True:
    mon_socket.listen(5) # accepte jusqu'a 5 connexions en file d'attente
    client, address = mon_socket.accept() # attend qu'un client se connecte
    print(f"{address} connectee")

    response = client.recv(255) # recoit max 255 octets du client
    if response != '':
        print(response)
        if response.endswith(b"CLOSE"): # si le message recu fin ipar close
            break

print("close")
client.close()
mon_socket.close()