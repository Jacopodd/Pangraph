import networkx as nx
import re

def parse_gfa(file_path):
    """
    Legge un file GFA e restituisce un grafo NetworkX.
    """
    G = nx.DiGraph()  # Usa grafo diretto

    with open(file_path, 'r') as f:
        for line in f:
            print(f"Linea letta: {line.strip()}")  # Debug: stampa la riga letta
            # Ignora righe vuote o commenti
            if not line.strip() or line.startswith('#'):
                continue

            # Normalizza spazi multipli in un unico separatore
            line = re.sub(r'\s+', '\t', line.strip())
            parts = line.split('\t')

            if parts[0] == 'S':  # Nodo (segmento)
                if len(parts) < 3:
                    print(f"Formato errato per nodo: {line.strip()}")
                    continue
                segment_id = parts[1]
                sequence = parts[2]
                print(f"Aggiunto nodo: {segment_id}, sequenza: {sequence}")
                G.add_node(segment_id, sequence=sequence)

            elif parts[0] == 'L':  # Arco (link)
                if len(parts) < 6:
                    print(f"Formato errato per link: {line.strip()}")
                    continue
                source = parts[1]
                target = parts[3]
                overlap = parts[5]
                print(f"Aggiunto arco: {source} -> {target}, overlap: {overlap}")
                G.add_edge(source, target, overlap=overlap)

            else:
                print(f"Riga ignorata: {line.strip()}")
                continue

    return G
