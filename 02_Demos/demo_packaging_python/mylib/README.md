# MyLib — Packaging et installation locale

> Les commandes ci-dessous sont à exécuter depuis le dossier **`Demo_Packaging_Python\mylib`**, qui contient déjà ce package prêt à être buildé et installé.

Ce dépôt contient déjà tout le nécessaire pour le package :

* `pyproject.toml` — configuration du package.
* `src/mylib/__init__.py` — point d’entrée du package.
* `src/mylib/core.py` — fonctions principales.

---

## Construire le package

```powershell
python -m build
```

Cela crée les fichiers `.whl` et `.tar.gz` dans `dist/`.

> Astuce : on peux aussi installer en mode développement avec
> `pip install --user -e .`
> Ce mode rend le package éditable : toute modification du code source est prise en compte immédiatement sans réinstaller.

---

## Installer localement

```powershell
pip install --user dist\mylib-0.1.0-py3-none-any.whl
```

---

## Vérifier l’installation

```powershell
pip list
# on doit voir "mylib"
```

---

## Tester l’utilisation

Créer un script dans un autre dossier, par exemple `use_mylib.py` :

```python
from mylib import greet

print(greet("Toto"))
```

Exécuter :

```powershell
python use_mylib.py
```

---

## Désinstaller

```powershell
pip uninstall mylib
```

Vérifier :

```powershell
pip list
# "mylib" ne doit plus apparaître
```
