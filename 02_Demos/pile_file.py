# # --- PILE (STACK) : LIFO = Last In, First Out ---
# # Implémentation simple avec list : push = append, pop = pop()

# pile = []  # pile vide
# print("=== PILE (stack) avec list ===")

# # Empiler (push) des éléments
# pile.append("a")   # top -> a
# pile.append("b")   # top -> b
# pile.append("c")   # top -> c
# print("Après push a, b, c :", pile)

# # Dépiler (pop) retire le dernier élément ajouté
# top = pile.pop()   # retire "c"
# print("pop() ->", top)
# print("Pile maintenant :", pile)

# top = pile.pop()   # retire "b"
# print("pop() ->", top)
# print("Pile maintenant :", pile)

# # Il reste "a"
# print("Sommet actuel :", pile[-1])
# print()

# # --- FILE (QUEUE) : FIFO = First In, First Out ---
# # Implémentation possible avec list : enqueuer = append, dequeuer = pop(0)
# # Attention : list.pop(0) est O(n) et donc inefficace pour de gros volumes.

# file_list = []  # file vide
# print("=== FILE (queue) avec list ===")

# # Enfiler (enqueue)
# file_list.append("a")  # queue -> ["a"]
# file_list.append("b")  # queue -> ["a", "b"]
# file_list.append("c")  # queue -> ["a", "b", "c"]
# print("Après enqueue a, b, c :", file_list)

# # Défiler (dequeue) retire le premier arrivé
# front = file_list.pop(0)  # retire "a"
# print("pop(0) ->", front)
# print("File maintenant :", file_list)

# front = file_list.pop(0)  # retire "b"
# print("pop(0) ->", front)
# print("File maintenant :", file_list)

# # Il reste "c"
# print("Tête actuelle :", file_list[0])
# print()

# --- FILE (QUEUE) recommandée : deque ---
# collections.deque est optimisée pour des ajouts/retraits en tête comme en queue.
from collections import deque

file_deque = deque()
print("=== FILE (queue) avec collections.deque ===")

# Enfiler (enqueue)
file_deque.append("a")
file_deque.append("b")
file_deque.append("c")
print("Après enqueue a, b, c :", list(file_deque))

# Défiler (dequeue) efficace avec popleft()
front = file_deque.popleft()  # retire "a"
print("popleft() ->", front)
print("File maintenant :", list(file_deque))

front = file_deque.popleft()  # retire "b"
print("popleft() ->", front)
print("File maintenant :", list(file_deque))

# Il reste "c"
print("Tête actuelle :", file_deque[0])

# Remarque:
# - Pile LIFO avec list: utiliser append() et pop() (fin de liste).
# - File FIFO avec list: possible avec append() et pop(0) mais peu performant.
# - File FIFO recommandée: utiliser collections.deque avec append() et popleft().