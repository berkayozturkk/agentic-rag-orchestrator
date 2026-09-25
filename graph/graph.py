from node_constants import RETRIEVE,GENERATE,WEBSEARCH,GRADE_DOCUMENTS
from nodes import generate,grade_documents,web_search,retrieve
from chains.router import question_router,RouteQuery
from state import GraphState
from chains.hallucination_grader import hallucination_grader
from chains.hallucination_grader import hallucination_grader
from chains.answer_grader import answer_grader
from langgraph.graph import END,StateGraph
from dotenv import load_dotenv

load_dotenv()

workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)

app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")

