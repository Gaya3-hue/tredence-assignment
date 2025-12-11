# main.py
from fastapi import FastAPI
from engine import WorkflowEngine
from workflows import WORKFLOW_NODES

app = FastAPI()
engine = WorkflowEngine()

@app.post("/graph/create")
def create_graph():
    graph = {
        "start": "extract",
        "nodes": WORKFLOW_NODES,
        "edges": {
            "extract": "complexity",
            "complexity": "issues",
            "issues": "improve"
        }
    }
    gid = engine.create_graph(graph)
    return {"graph_id": gid}

@app.post("/graph/run")
def run_graph(graph_id: str, code: str):
    state = {"code": code}
    final_state, log, run_id = engine.run(graph_id, state)
    return final_state

@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    return engine.get_state(run_id)
