import socket

host = "localhost"
port = 15555

mon_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mon_socket.connect((host,port))
print(f"Connection au port {port}")


mon_socket.send(b"Salut je m'appelle Toto")
mon_socket.send(bytes("Hey my name is Toto",encoding="UTF-8"))
mon_socket.send(bytes("CLOSE",encoding="UTF-8"))


print("Close")
mon_socket.close()