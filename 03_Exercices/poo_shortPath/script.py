from short_path import short_path

class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []
    
    def add_node(self, node) :
        self.nodes.append(node)

    def add_edge(self, edge) :
        self.edges.append(edge)

class Node:
    def __init__(self, name):
        self.name = name
        self.in_edges = []
        self.out_edges = []

class Edge:
    def __init__(self, tail, head) -> None:
        self.tail = tail
        tail.out_edges.append(self)
        self.head = head
        head.in_edges.append(self)

class Travel(Edge) :
    def __init__(self, tail, head, price, time, conveyance) -> None:
        super().__init__(tail, head)
        self.price = price
        self.time = time
        self.conveyance = conveyance

if __name__ == '__main__':
    travel_graph = Graph()

    lyon = Node("Lyon")
    paris = Node("Paris")
    lille = Node("Lille")
    strasbourg = Node("Strasbourg")
    travel_graph.add_node(lyon)
    travel_graph.add_node(paris)
    travel_graph.add_node(lille)
    travel_graph.add_node(strasbourg)

    lyon_paris = Travel(lyon, paris, 100, 120, "Train")
    lyon_strasbourg = Travel(lyon, strasbourg, 50, 160, "Train")
    paris_lille1 = Travel(paris, lille, 60, 60, "Train")
    paris_lille2 = Travel(paris, lille, 10, 100, "Bus")
    strasbourg_lille = Travel(strasbourg, lille, 20, 180, "Bus")
    travel_graph.add_edge(lyon_paris)
    travel_graph.add_edge(lyon_strasbourg)
    travel_graph.add_edge(paris_lille1)
    travel_graph.add_edge(paris_lille2)
    travel_graph.add_edge(strasbourg_lille)

    (path_edges, path_weight) = short_path(lyon, lille, lambda edge: edge.time)
    time_hours = path_weight//60
    time_minutes = path_weight%60
    print(f"\nLe chemin le plus rapide entre Lyon et Lille dure {time_hours:02}h{time_minutes:02} et emprunte ces trajets :\n")

    for travel in path_edges :
        print(f"\t- {travel.tail.name:<15} -> {travel.head.name:<15}  [{travel.conveyance} | {travel.time:3} mins | {travel.price:3} €]")

    (path_edges, path_weight) = short_path(lyon, lille, lambda edge: edge.price)
    print(f"\nLe chemin le plus couteux entre Lyon et Lille coute {path_weight:.2f} € et emprunte ces trajets :\n")
    for travel in path_edges :
        print(f"\t- {travel.tail.name:<15} -> {travel.head.name:<15}  [{travel.conveyance} | {travel.time:3} mins | {travel.price:3} €]")

