# LangGraph StateGraph — Step by Step Explanation

## What is a StateGraph?

A StateGraph is a flowchart where data flows through boxes (nodes) connected by arrows (edges).

- **State** = the shared data passing through the graph
- **Nodes** = the processing steps (do the work)
- **Edges** = the connections (define the path)
- **Conditional Edges** = smart connections (make decisions)

---

## The Code

### 1. State — Define the data shape

```python
from typing_extensions import TypedDict

class State(TypedDict):
    graph_state: str
```

- `State` is a TypedDict — it defines the **blueprint** of the data
- `graph_state: str` means there is one key called `graph_state` and it must be a string
- At runtime, `state` is just a plain Python dictionary: `{"graph_state": "..."}`

---

### 2. Nodes — Define the work

```python
def node_1(state):
    print("---Node 1---")
    return {"graph_state": state['graph_state'] + " I am"}

def node_2(state):
    print("---Node 2---")
    return {"graph_state": state['graph_state'] + " happy!"}

def node_3(state):
    print("---Node 3---")
    return {"graph_state": state['graph_state'] + " sad!"}
```

- Every node takes `state` (a dictionary) as input
- LangGraph passes the current state automatically — you don't call nodes manually
- Each node returns only the keys it changed — LangGraph merges it into the full state

---

### 3. Conditional Edge — Define the routing logic

```python
import random
from typing import Literal

def decide_mood(state) -> Literal["node_2", "node_3"]:
    user_input = state['graph_state']

    if random.random() < 0.5:
        return "node_2"
    return "node_3"
```

- Takes `state` as input
- Uses `user_input` (the current state value) inside the condition
- Returns a **string** — the name of the next node to go to
- LangGraph uses that string to find and run the next node

---

### 4. Build the Graph

```python
from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)

# Add nodes
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# Add edges
builder.add_edge(START, "node_1")           # START → node_1
builder.add_conditional_edges("node_1", decide_mood)  # node_1 → node_2 or node_3
builder.add_edge("node_2", END)             # node_2 → END
builder.add_edge("node_3", END)             # node_3 → END

graph = builder.compile()
```

---

### 5. Run the Graph

```python
result = graph.invoke({"graph_state": "Hi, this is Lakshan."})
```

---

## Dry Run — Step by Step

```
graph.invoke({"graph_state": "Hi, this is Lakshan."})
```

### Step 1 — invoke called
LangGraph takes the dictionary as initial state:
```
state = {"graph_state": "Hi, this is Lakshan."}
```

### Step 2 — START → node_1
```
builder.add_edge(START, "node_1")
```
LangGraph calls node_1 with current state.

### Step 3 — node_1 runs
```
state['graph_state'] = "Hi, this is Lakshan."
adds " I am"
returns {"graph_state": "Hi, this is Lakshan. I am"}
```
State is now:
```
{"graph_state": "Hi, this is Lakshan. I am"}
```

### Step 4 — conditional edge runs decide_mood
```
builder.add_conditional_edges("node_1", decide_mood)
```
LangGraph calls decide_mood with updated state.

### Step 5 — decide_mood returns a node name
```
user_input = "Hi, this is Lakshan. I am"
random() = 0.3  (less than 0.5)
returns "node_2"
```
LangGraph now knows to go to node_2.

### Step 6 — node_2 runs
```
state['graph_state'] = "Hi, this is Lakshan. I am"
adds " happy!"
returns {"graph_state": "Hi, this is Lakshan. I am happy!"}
```

### Step 7 — END reached
```
builder.add_edge("node_2", END)
```
Graph stops.

### Step 8 — Final result returned
```
{"graph_state": "Hi, this is Lakshan. I am happy!"}
```

---

## Flow Diagram

```
START
  ↓
node_1  →  adds " I am"
  ↓
decide_mood  →  random() < 0.5?
  ↓                    ↓
node_2              node_3
adds " happy!"      adds " sad!"
  ↓                    ↓
 END                  END
```

---

## Key Takeaways

| Concept | What it is | Why defined that way |
|---------|-----------|---------------------|
| State | Plain dictionary at runtime | TypedDict gives structure and type safety |
| Nodes | Regular functions | They take state, do work, return updated keys |
| Edges | Connections between nodes | Tell LangGraph the fixed path |
| Conditional Edges | Functions returning node name | Runtime decisions based on state |
| invoke | Starts the graph | Passes initial state dictionary |