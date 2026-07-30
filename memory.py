from langchain.messages import HumanMessage , AIMessage

class ConversationalMemory:

    def __init__(self):
        self.chat_history = []

    def add_human_message(self , message :str):
        self.chat_history.append(HumanMessage(content= message))

    def add_ai_message(self , message : str):
        self.chat_history.append(AIMessage(content= message))

    def get_chat_history(self):
        """Return the current conversation history"""
        return self.chat_history

    def clear_history(self):
        self.chat_history.clear()