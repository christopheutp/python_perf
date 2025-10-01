from datetime import date

def aujourd_hui() -> str:
    return date.today().isoformat()