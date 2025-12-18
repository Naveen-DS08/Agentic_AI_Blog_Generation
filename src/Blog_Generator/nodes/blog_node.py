from src.Blog_Generator.state.blog_state import BlogState, Blog
from langchain_core.messages import SystemMessage, HumanMessage

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
        
    def translator(self, state:BlogState):
        "Translate the content to the specified language."
        sys_msg = """
                Translate the following content into {current_language}.
                - Maintain the original tone, style and formating.
                - Adapt cultural reference and idioms to be appropriate for {current_language}.
                ########    
                ORIGINAL CONTENT:
                ########
                {blog_content}
                ########
                """
        prompt = sys_msg.format(current_language= state["current_language"], blog_content = state["blog"]["content"])
        message = [HumanMessage(prompt)]
        translated_content = self.llm.with_structured_output(Blog).invoke(message)

        return {"blog":{"translated_blog": translated_content.content}}
    
    def route_language(self, state: BlogState):
        return {"current_language": state["current_language"]}
    
    def route_decision(self, state:BlogState):
        "Route the content to respective translator function."
        if state["current_language"] == "tamil":
            return "tamil"
        elif state["current_language"] == "french":
            return "french"
        else: 
            return state["current_language"]
