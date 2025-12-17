from langgraph.graph import START, END, StateGraph
from src.Blog_Generator.llms.groq_llm import GroqLLM
from src.Blog_Generator.state.blog_state import BlogState
from src.Blog_Generator.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm 
        self.graph = StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate a Blog based on topic.
        """

        # nodes
        self.blog_node_obj = BlogNode(llm=self.llm)
        self.graph.add_node("title_creator", self.blog_node_obj.title_creator)
        self.graph.add_node("content_generator", self.blog_node_obj.content_generator)

        # Edges
        self.graph.set_entry_point("title_creator")
        self.graph.add_edge("title_creator", "content_generator")
        self.graph.set_finish_point("content_generator")

        return self.graph
    
    def setup_graph(self, usecase):
        if usecase == "topic":
            graph = self.build_topic_graph()

        return graph.compile()