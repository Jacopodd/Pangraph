# src/graph_statistics.py

def compute_statistics(G, bubbles):
    """
    Calcola alcune statistiche base su grafo e bolle.
    Restituisce un dizionario con statistiche di esempio.
    """
    stats = {}
    stats['num_nodes'] = G.number_of_nodes()
    stats['num_edges'] = G.number_of_edges()
    stats['num_bubbles'] = len(bubbles)

    # La 'densità di bolle' può essere definita come: 
    # numero di bolle / numero di nodi (o edges), come esempio
    stats['bubble_density'] = len(bubbles) / max(1, G.number_of_nodes())

    # In un progetto reale, potresti calcolare le frequenze alleliche 
    # se hai info su quanti campioni presentano certe varianti, etc.

    return stats
