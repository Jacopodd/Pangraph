# src/__init__.py

# Importa i moduli principali del package per comodità
from .graph_loader import parse_gfa
from .graph_processor import identify_bubbles, classify_variants
from .graph_statistics import compute_statistics
from .app import run_app

# Specifica cosa viene esportato quando si importa il package
__all__ = [
    "parse_gfa",
    "identify_bubbles",
    "classify_variants",
    "compute_statistics",
    "run_app",
]

import sys
if "src.app" in sys.modules:
    del sys.modules["src.app"]