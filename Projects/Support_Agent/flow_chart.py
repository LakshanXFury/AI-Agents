from dotenv import load_dotenv
load_dotenv(override=True)

from graph.build_graph import graph

# Generate graph image
png_bytes = graph.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png_bytes)

print("Graph image saved as graph.png")