def saluer(nom):
    return f"Bonjour {nom}"

if __name__ == "__main__":
    print("utils.py exécuté directement")
else:
    print("utils.py importé")
    print(__name__)