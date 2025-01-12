import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph for the workflow
G = nx.DiGraph()

# Add nodes representing steps in the workflow
G.add_node("Data Collection")
G.add_node("Data Cleaning")
G.add_node("Feature Engineering")
G.add_node("Model Selection")
G.add_node("Model Training")
G.add_node("Model Evaluation")
G.add_node("Deployment")

# Add edges representing the flow between steps
G.add_edges_from([
    ("Data Collection", "Data Cleaning"),
    ("Data Cleaning", "Feature Engineering"),
    ("Feature Engineering", "Model Selection"),
    ("Model Selection", "Model Training"),
    ("Model Training", "Model Evaluation"),
    ("Model Evaluation", "Deployment")
])

# Draw the graph with a specific layout
pos = nx.spring_layout(G, seed=42)  # Layout for better positioning

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=4000, node_color="skyblue", font_size=10, font_weight="bold", 
        edge_color="gray", arrowsize=20)

# Add a title to the plot
plt.title("End-to-End Workflow Diagram", fontsize=15, fontweight='bold')
plt.show()
