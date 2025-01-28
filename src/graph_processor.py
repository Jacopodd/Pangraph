# src/graph_processor.py

import networkx as nx

def identify_bubbles(G):
    """
    Identifica le bolle nel grafo. Una bolla è una regione con più percorsi alternativi
    che convergono di nuovo su un nodo comune.
    """
    bubbles = {}
    bubble_count = 0

    for node in G.nodes():
        successors = list(G.successors(node))
        if len(successors) > 1:
            # Controlla se i successori convergono su uno stesso nodo
            for succ1 in successors:
                for succ2 in successors:
                    if succ1 != succ2 and set(G.successors(succ1)) & set(G.successors(succ2)):
                        bubble_count += 1
                        bubbles[f"bubble_{bubble_count}"] = {
                            'nodes': [node, succ1, succ2],
                            'type': 'SNP',  # Placeholder per tipo di variante
                        }
    return bubbles


def classify_variants(bubbles):
    color_palette = ['#FF5733', '#33FF57', '#3357FF', '#F4D03F', '#8E44AD']
    color_map = {}
    for i, bubble_id in enumerate(bubbles.keys()):
        color_map[bubble_id] = color_palette[i % len(color_palette)]
    return color_map
