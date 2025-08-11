from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name : str

def compliment_agent(state: AgentState) -> AgentState:
    """Simple node that adds a compliment message to the state"""
    state['name'] = state["name"] + ", you're doing an amazing job learning LangGraph!"
    return state

graph = StateGraph(AgentState)

graph.add_node("compliment", compliment_agent)

graph.set_entry_point("compliment")
graph.set_finish_point("compliment")

app = graph.compile()

result = app.invoke({"name": "Bob"})

result["name"]

print(result["name"])