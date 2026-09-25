from graph.chains.generation import generation_chain
from graph.state import GraphState
from typing import Any,Dict

def generate(state:GraphState) -> Dict[str,Any]:
    print("-----Generate----")
    question = state["question"]
    document = state["documents"]

    generation = generation_chain.invoke(
        {"context":document, "question":question}
    )

    return {"question":question, "documents":document, "generation":generation}
