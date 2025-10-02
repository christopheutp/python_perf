# venv Python

Commande a taper dans un terminal ouvert a la racine de votre projet.

## Creation d'un environnment virtuel

```
python -m venv .venv
```

## Activer l'environnement virtuel

```
.venv\Scripts\Activate
```

## Installation de dependances

```
pip install requests
```

## Desinstallation de dependances (si besoin)

```
pip uninstall requests
```

## Geler les dependances

```
pip freeze > requirements.txt
```

Ne pas oublier d'ajouter un .gitignore avec 

```
.venv/
__pycache__/
```

## Quitter l'environnement virtuel 

```
deactivate
```

Sur une nouvelle/autre machine :

## Creation d'un nouveau venv et installation des dependances depuis requirement.txt


```
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirement.txt
```

## Voir les packages present

```
pip list
```