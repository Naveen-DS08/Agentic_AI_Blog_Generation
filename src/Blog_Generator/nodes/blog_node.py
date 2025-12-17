from src.Blog_Generator.state.blog_state import BlogState


class BlogNode:
    "A class to represent Blog node"
    def __init__(self, llm, state:BlogState):
        self.llm = llm
        self.state= state

    def title_creator(self):
        "Create a title for a Blog"
        if "topic" in self.state and self.state["topic"]:
            sys_msg = """
                    You are an expert in creating an 'title' of the blog for the 
                    user specified {topic}. Use Markdown formating. 
                    The title shoud be creative and SEO friendly. 
                    """            
            prompt = sys_msg.format(topic=self.state["topic"])

            response = self.llm.invoke(prompt)

            return {"blog":{"title":response.content}}
        
    def content_generator(self):
        "Generate an content for an Blog"
        if "title" in self.state and self.state["title"]:
            sys_msg = """
                        You are an expert blog writer. Use Markdown formatting.
                        Generate an detailed blog content for the {topic} with the title name as {title}
                    """
            prompt = sys_msg.format(topic = self.state["topic"], title = self.state["blog"]["title"])
            response = self.llm.invike(prompt)
            return {"blog": {"title":self.state["blog"]["title"], "content": response.content}}