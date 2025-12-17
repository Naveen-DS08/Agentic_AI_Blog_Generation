from src.Blog_Generator.state.blog_state import BlogState


class BlogNode:
    "A class to represent Blog node"
    def __init__(self, llm):
        self.llm = llm
        # self.state= state

    def title_creator(self, state:BlogState):
        "Create a title for a Blog"
        if "topic" in state and state["topic"]:
            sys_msg = """
                    You are an expert in creating an 'title' of the blog for the 
                    user specified {topic}. Use Markdown formating. 
                    The title shoud be creative and SEO friendly. 
                    Generate a blog title for the ({topic}
                    """            
            prompt = sys_msg.format(topic= state["topic"])

            response = self.llm.invoke(prompt)

            return {"blog":{"title":response.content}}
        
    def content_generator(self, state:BlogState):
        "Generate an content for an Blog"
        if "title" in state["blog"] and state["blog"]["title"]:
            sys_msg = """
                        You are an expert blog content writer. Use Markdown formatting.
                        Generate an detailed blog content with detailed breakdown for the {topic} 
                        for the title name as {title}
                    """
            prompt = sys_msg.format(topic = state["topic"], title = state["blog"]["title"])
            response = self.llm.invoke(prompt)
            return {"blog": {"title":state["blog"]["title"], "content": response.content}}