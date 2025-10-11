#  Pangraph – Interactive Pangenome Graph Visualizer

**Pangraph** is a bioinformatics project designed to **visualize, analyze, and export pangenome graphs** interactively.  
Built with **Python** and **Dash (Plotly)**, it enables researchers to explore genome relationships, highlight **genetic variants (bubbles)**, and export graph data in CSV format for downstream analysis.

---

##  Key Features

- **Load pangenome graphs** from `.gfa` files  
- **Interactive visualization** with clickable nodes and side panels  
- **Highlight genetic bubbles** representing SNPs, insertions, and deletions  
- **Export node data** to CSV format  

---

##  Requirements

Before starting, make sure you have installed:

- **Python 3.8+**
- **Git** (optional, for cloning the repository)

---

##  Installation & Setup

### 1️. Download the Project

**Option 1 – Clone from GitHub:**
```bash
git clone https://github.com/Jacopodd/Pangraph.git
cd Pangraph
```

**Option 2 – Download ZIP:**
1. Go to the repository page on GitHub  
2. Click **Code → Download ZIP**  
3. Extract the ZIP and open the folder in your terminal  

---

### 2️. Create a Virtual Environment

Create a virtual environment to isolate project dependencies:

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
.env\Scriptsctivate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

---

### 3️. Install Dependencies

Install all required libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4️. Run the Application

Start the app with:

```bash
python -m src.app
```

After a few seconds, open your browser and go to:

```
http://127.0.0.1:8050
```

---

##  Usage

1. **Load a GFA file**  
   Enter the path to a `.gfa` file (e.g., `data/example_1.gfa`) and click **"Load Graph"**  

2. **Explore the Graph**  
   Click on a node to view detailed information in the side panel  

3. **Highlight Bubbles**  
   Use **"Highlight Bubbles"** to display genetic variants, and **"Reset Highlights"** to restore the default view  

4. **Export Data**  
   Click **"Export to CSV"** to download node information for further analysis  

---

##  Example Files

Inside the `data/` folder, you’ll find example GFA files:

```
example_1.gfa   → Simple graph
example_10.gfa  → Complex graph with multiple variants
```

---

##  Common Issues

### 1. App doesn’t start
- Ensure the virtual environment is activated  
- Verify that Python 3.8 or higher is installed  

### 2. `ModuleNotFoundError`
- Run the installation command again:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Graph not loading
- Double-check the `.gfa` file path  
- Confirm the file exists in the specified directory  

---

##  Contributing

Contributions and pull requests are welcome!  
To contribute:
1. Fork this repository  
2. Create a new branch for your feature or fix  
3. Submit a pull request with a clear description  


---

## 📜 License

Distributed under the **MIT License**.  
