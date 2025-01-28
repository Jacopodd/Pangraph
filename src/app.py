# src/app.py

import dash
from dash import html, dcc, Input, Output, State
import dash_cytoscape as cyto
import networkx as nx

from .graph_loader import parse_gfa
from .graph_processor import identify_bubbles, classify_variants
from .graph_statistics import compute_statistics

# Carichiamo i componenti di dash_cytoscape
cyto.load_extra_layouts()

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Layout dell'app
from dash import dcc
app.layout = html.Div(
    children=[
        html.H1(
            "PanGraph",
            style={"textAlign": "center", "marginBottom": "20px"},
        ),

        # Input per il file GFA e pulsante di caricamento
        html.Div(
            style={"display": "flex", "justifyContent": "center", "marginBottom": "20px"},
            children=[
                dcc.Input(
                    id="gfa-file-input",
                    type="text",
                    placeholder="Inserisci percorso del file GFA",
                    value="data/example.gfa",
                    style={
                        "width": "60%",
                        "padding": "10px",
                        "borderRadius": "5px",
                        "border": "1px solid #ccc",
                    },
                ),
                html.Button(
                    "Carica Grafo",
                    id="load-graph-btn",
                    style={
                        "marginLeft": "10px",
                        "backgroundColor": "#007BFF",
                        "color": "#fff",
                        "padding": "10px 15px",
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                    },
                ),
            ],
        ),

        # Store per il grafo e le bolle
        dcc.Store(id="graph-data"),  # Memorizza il grafo
        dcc.Store(id="bubble-data"),  # Memorizza i dati delle bolle

        # Grafico Cytoscape e pannello laterale
        html.Div(
            style={"display": "flex", "justifyContent": "space-between", "gap": "20px"},
            children=[
                # Cytoscape per la visualizzazione del grafo
                cyto.Cytoscape(
                    id="pangenome-graph",
                    layout={"name": "cose"},
                    style={"width": "70%", "height": "600px", "border": "1px solid #ccc", "borderRadius": "10px"},
                    elements=[],
                ),

                # Pannello laterale con dettagli e statistiche
                html.Div(
                    style={
                        "width": "30%",
                        "padding": "10px",
                        "backgroundColor": "#fff",
                        "borderRadius": "10px",
                        "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
                    },
                    children=[
                        html.H3("Dettagli Nodo", style={"textAlign": "center", "color": "#007BFF"}),
                        html.Div(id="node-data-output", style={"marginTop": "20px"}),

                        html.H3("Statistiche Grafo", style={"textAlign": "center", "color": "#007BFF", "marginTop": "30px"}),
                        html.Div(id="graph-stats-output", style={"marginTop": "20px"}),

                        html.Div(
                            style={"marginTop": "30px", "textAlign": "center"},
                            children=[
                                html.Button(
                                    "Evidenzia Bubbles",
                                    id="highlight-bubbles-btn",
                                    style={
                                        "backgroundColor": "#28A745",
                                        "color": "#fff",
                                        "padding": "10px 20px",
                                        "border": "none",
                                        "borderRadius": "5px",
                                        "cursor": "pointer",
                                        "marginRight": "10px",
                                    },
                                ),
                                html.Button(
                                    "Reset Evidenziazione",
                                    id="reset-highlight-btn",
                                    style={
                                        "backgroundColor": "#DC3545",
                                        "color": "#fff",
                                        "padding": "10px 20px",
                                        "border": "none",
                                        "borderRadius": "5px",
                                        "cursor": "pointer",
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),

        # Pulsante di esportazione
        html.Div(
            style={"textAlign": "center", "marginTop": "20px"},
            children=[
                html.Button(
                    "Esporta in CSV",
                    id="export-csv-btn",
                    style={
                        "backgroundColor": "#17A2B8",
                        "color": "#fff",
                        "padding": "10px 20px",
                        "border": "none",
                        "borderRadius": "5px",
                        "cursor": "pointer",
                    },
                ),
                dcc.Download(id="download-dataframe-csv"),
            ],
        ),
    ]
)



# CALLBACK 1: Caricamento e costruzione del grafo
from networkx.readwrite import json_graph

@app.callback(
    Output('pangenome-graph', 'elements'),
    Output('graph-stats-output', 'children'),
    Output('graph-data', 'data'),  # Store per il grafo
    Output('bubble-data', 'data'),  # Store per le bolle
    Input('load-graph-btn', 'n_clicks'),
    State('gfa-file-input', 'value'),
    prevent_initial_call=True
)
def load_graph(n_clicks, file_path):
    if not file_path:
        return [], "Nessun file GFA specificato.", None, None

    # Carichiamo il grafo
    G = parse_gfa(file_path)

    # Identifichiamo bolle
    bubbles = identify_bubbles(G)

    # Statistiche
    stats = compute_statistics(G, bubbles)

    # Convertiamo G in elements per cytoscape
    nodes = []
    edges = []
    for node in G.nodes(data=True):
        node_id = node[0]
        label = node[0]  # semplice label con l'ID
        nodes.append({
            'data': {'id': node_id, 'label': label},
            'classes': ''  # useremo classi per evidenziare
        })

    for edge in G.edges(data=True):
        source = edge[0]
        target = edge[1]
        edges.append({
            'data': {
                'source': source,
                'target': target
            },
            'classes': ''
        })

    # Statistiche di esempio
    stats_text = f"""
    Numero Nodi: {stats['num_nodes']} \n
    Numero Archi: {stats['num_edges']} \n
    Numero Bubbles: {stats['num_bubbles']} \n
    Densità Bubbles: {stats['bubble_density']:.3f}
    """

    # Convertiamo il grafo in JSON
    graph_data = json_graph.node_link_data(G)

    # Salviamo anche le bolle come JSON serializzabile
    bubble_data = {"bubbles": bubbles}

    return (nodes + edges, stats_text, graph_data, bubble_data)


# CALLBACK 2: Mostra info nodo cliccato
from networkx.readwrite import json_graph

@app.callback(
    Output('node-data-output', 'children'),
    Input('pangenome-graph', 'tapNodeData'),
    State('graph-data', 'data')  # Recuperiamo il grafo dallo Store
)
def display_node_data(data, graph_data):
    if data is None:
        return "Clicca su un nodo per vedere i dettagli."
    if graph_data is None:
        return "Il grafo non è stato caricato."

    # Ricostruisci il grafo da JSON
    G = json_graph.node_link_graph(graph_data)

    # Recupera i dati del nodo cliccato
    node_id = data['id']
    node_data = G.nodes[node_id]

    # Mostra le informazioni
    sequence = node_data.get('sequence', 'N/D')
    return html.Div([
        html.H3(f"Nodo: {node_id}"),
        html.P(f"Sequenza associata: {sequence}")
    ])


# CALLBACK 3: Evidenzia le bolle
@app.callback(
    Output('pangenome-graph', 'stylesheet'),
    Input('highlight-bubbles-btn', 'n_clicks'),
    Input('reset-highlight-btn', 'n_clicks'),
    State('bubble-data', 'data'),
    prevent_initial_call=True
)
def highlight_bubbles(n_clicks_highlight, n_clicks_reset, bubble_data):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Foglio di stile predefinito
    default_stylesheet = [
        {
            'selector': 'node',
            'style': {
                'content': 'data(label)',
                'background-color': '#0074D9',
                'color': '#fff',
                'text-valign': 'center',
                'text-halign': 'center',
            },
        },
        {
            'selector': 'edge',
            'style': {
                'line-color': '#999',
                'width': 2,
            },
        },
    ]

    # Gestione del pulsante "Evidenzia Bubbles"
    if button_id == 'highlight-bubbles-btn':
        if bubble_data is None or 'bubbles' not in bubble_data or len(bubble_data['bubbles']) == 0:
            return default_stylesheet  # Nessuna bolla da evidenziare

        bubbles = bubble_data['bubbles']
        color_map = classify_variants(bubbles)  # Mappa dei colori per le bolle

        # Evidenzia i nodi delle bolle
        style_additions = []
        for bubble_id, info in bubbles.items():
            nodes_in_bubble = info['nodes']
            bubble_color = color_map[bubble_id]
            for n_id in nodes_in_bubble:
                style_additions.append({
                    'selector': f'[id = "{n_id}"]',
                    'style': {
                        'background-color': bubble_color,
                        'border-width': '2px',
                        'border-color': '#000',
                    },
                })

        return default_stylesheet + style_additions

    # Gestione del pulsante "Reset Evidenziazione"
    elif button_id == 'reset-highlight-btn':
        return default_stylesheet


# CALLBACK 4: Esportazione in CSV
import pandas as pd

@app.callback(
    Output('download-dataframe-csv', 'data'),
    Input('export-csv-btn', 'n_clicks'),
    State('graph-data', 'data'),  # Recuperiamo il grafo dallo Store
    prevent_initial_call=True
)
def export_csv(n_clicks, graph_data):
    if graph_data is None:
        raise dash.exceptions.PreventUpdate

    # Ricostruiamo il grafo da JSON
    G = json_graph.node_link_graph(graph_data)

    # Creiamo una lista per i dati dei nodi
    nodes_data = []
    for node_id, data in G.nodes(data=True):
        nodes_data.append({
            'node_id': node_id,
            'sequence': data.get('sequence', 'N/D'),  # Default: 'N/D' se non c'è una sequenza
        })

    # Convertiamo in DataFrame
    df = pd.DataFrame(nodes_data)

    # Esportiamo come CSV
    return dcc.send_data_frame(df.to_csv, "pangenome_nodes.csv", index=False)


server = app.server  # Per eventuale deploy su servizi come Heroku

def run_app():
    app.run_server(debug=True)
