# engine.py
# Basic placeholder engine for the assignment.
# I sketched the idea but did not fully implement execution.

class WorkflowEngine:
    def __init__(self):
        # store graphs in memory
        self.graphs = {}

    def create_graph(self, graph):
        gid = str(len(self.graphs) + 1)
        self.graphs[gid] = graph
        return gid

    def run(self, gid, state):
        # Not fully implemented.
        # The idea was to run nodes step by step and update state.
        # I added only a placeholder return to show the approach.
        return {"message": "run not fully implemented", "state": state}, [], "1"

    def get_state(self, run_id):
        return {"message": "state tracking not implemented"}
