from setuptools import setup, find_packages

setup(
    name="pangenome_visualizer",  # Nome del pacchetto
    version="0.1.0",             # Versione iniziale
    description="Visualizzatore interattivo per grafi pangenomici",  # Descrizione
    author="Tuo Nome",           # Inserisci il tuo nome
    author_email="tuo@email.com",  # Inserisci la tua email
    url="https://github.com/tuo-repo/pangenome_visualizer",  # Inserisci il link al tuo repo
    packages=find_packages(where="src"),  # Cerca i package nella directory 'src'
    package_dir={"": "src"},     # Indica che i moduli si trovano in 'src'
    include_package_data=True,   # Include eventuali dati aggiuntivi nel pacchetto
    install_requires=[           # Dipendenze necessarie
        "dash>=2.9.3",
        "dash-cytoscape>=0.3.0",
        "pandas>=2.0.3",
        "networkx>=3.1"
    ],
    entry_points={               # Punto di ingresso per eseguire l'app
        "console_scripts": [
            "pangenome_visualizer=src.main:run_app",
        ],
    },
    classifiers=[                # Metadati utili per PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",     # Versione minima di Python
)
