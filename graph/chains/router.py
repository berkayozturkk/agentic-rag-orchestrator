from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel,Field
from typing import Literal

load_dotenv()

class RouteQuery(BaseModel):
    """
        Route a user query to the most relevant datasource
    """

    datasource:Literal["vectorstore","websearch"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore",
    )

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.0)
structured_llm_router = llm.with_structured_output(RouteQuery)

system = """You are an expert at routing a user question to a vectorstore or websearch.
The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
Use the vectorstore for questions on these topics. For all else, use websearch."""

route_promt = ChatPromptTemplate.from_messages(
    [
        ("system" , system),
        ("human" , "{question}"),
    ]
)

question_router = route_promt | structured_llm_router

if __name__ == '__main__':
    print(question_router.invoke(
        {"question":"what is the memory"}
    ))