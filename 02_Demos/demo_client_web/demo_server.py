import socket
import threading
import os

HOST = ""          # écoute sur toutes les interfaces
PORT = 11111
FILENAME = "test.txt"  # fichier par défaut à servir

def http_response(body: bytes, status="200 OK", content_type="text/plain; charset=utf-8"):
    headers = [
        f"HTTP/1.1 {status}",
        f"Content-Type: {content_type}",
        f"Content-Length: {len(body)}",
        "Connection: close",
        "",
        "",
    ]
    return "\r\n".join(headers).encode("utf-8") + body

class ClientThread(threading.Thread):
    def __init__(self, clientsock, addr):
        super().__init__(daemon=True)
        self.clientsock = clientsock
        self.addr = addr

    def run(self):
        try:
            # On lit juste la première ligne de la requête (si c’est un navigateur)
            _ = self.clientsock.recv(1024)

            if not os.path.exists(FILENAME):
                body = b"[ERROR] File not found"
                self.clientsock.sendall(http_response(body, status="404 Not Found"))
                return

            # Envoie du fichier avec un en-tête HTTP minimal — pour que le navigateur affiche
            with open(FILENAME, "rb") as f:
                body = f.read()
            # Si tu sers du texte, text/plain va bien ; pour binaire, ça marche aussi (le navigateur téléchargera)
            self.clientsock.sendall(http_response(body, status="200 OK", content_type="text/plain; charset=utf-8"))
        finally:
            self.clientsock.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(10)
        print(f"[SERVER] Ouvre ton navigateur sur http://127.0.0.1:{PORT}/")
        while True:
            csock, addr = s.accept()
            ClientThread(csock, addr).start()

if __name__ == "__main__":
    main()
