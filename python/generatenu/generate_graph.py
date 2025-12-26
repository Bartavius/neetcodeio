import json
from pyvis.network import Network

# Load data
with open("./generate_test.json", "r") as f:
    data = json.load(f)

sensors = data["sensors"]
risks = data["risks"]
targets = set(data["targetSensors"])

# Create interactive network
net = Network(
    height="800px",
    width="100%",
    directed=True,
    bgcolor="#ffffff",
    font_color="black"
)

net.toggle_physics(True)

# Add nodes
for sensor in sensors:
    node_id = sensor["id"]

    if node_id in targets:
        color = "red"
        size = 30
    else:
        color = "lightblue"
        size = 18

    net.add_node(
        node_id,
        label=str(node_id),
        color=color,
        size=size
    )

# Add edges
for edge in risks:
    net.add_edge(
        edge["fromSensor"],
        edge["toSensor"],
        label=str(edge["risk"]),
        title=f"risk = {edge['risk']}"
    )

# Physics settings (important for untangling)
net.set_options("""
{
  "physics": {
    "enabled": true,
    "stabilization": true,
    "barnesHut": {
      "gravitationalConstant": -30000,
      "springLength": 120,
      "springConstant": 0.04
    }
  }
}
""")

# Write and open
net.write_html("sensor_graph.html", notebook=False)
print("Open sensor_graph.html in your browser")

