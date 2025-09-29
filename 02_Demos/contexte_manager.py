# with open("demo_file.txt","w") as f:
#     f.write("Bonjour ceci est un test de context manager")

# with open("demo_file.txt","r") as f:
#     contenu = f.read()
#     print(contenu)


class Resource:
    def __enter__(self):
        print("Connexion ouverte")
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("Connexion fermée")

    def process(self,data):
        print(f"Traitement : {data}")

with Resource() as r:
    r.process("donee brute")