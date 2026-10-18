from langgraph.graph import StateGraph, START, END
from graph import State, node_1, node_2, node_3, decide_mood



# 1. Create the graph with State schema
builder = StateGraph(State)

# 2. Add nodes
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# 3. Add Edges
builder.add_edge(START, "node_1")        # START → node_1
builder.add_conditional_edges("node_1", decide_mood)  # node_1 → decide_mood → node_2 or node_3
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)


graph = builder.compile()
result = graph.invoke({"graph_state": "Hi, this is Lakshan."})
print(result)


"""
START
  ↓
node_1  →  adds " I am"
  ↓
decide_mood  →  random() < 0.5?
  ↓                ↓
node_2          node_3
"happy!"        "sad!"
  ↓                ↓
 END             END
"""