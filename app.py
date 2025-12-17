import uvicorn
from fastapi import FastAPI, Request 
from src.Blog_Generator.graphs.graph_builder import GraphBuilder
from src.Blog_Generator.llms.groq_llm import GroqLLM
import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

app = FastAPI()

## API creation

# post
@app.post("/blogs")
async def create_blogs(request:Request):
    data = await request.json()
    topic = data.get("topic", "")

    # get llm object
    groqllm = GroqLLM()
    llm = groqllm.get_llm()

    # get the graph
    graph_builder = GraphBuilder(llm=llm)
    if topic:
        graph = graph_builder.setup_graph(usecase = "topic")
        state = graph.invoke({"topic": topic})

    return {"data": state}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True )
