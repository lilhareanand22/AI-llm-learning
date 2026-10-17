from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv()

model = init_chat_model("gpt-6-luna")

# system_msg = SystemMessage("You are a helpful assistant.")
# human_msg = HumanMessage("Hello, how are you?")

# # Use with chat models
# messages = [system_msg, human_msg]


system_msg = SystemMessage("""
You are a senior Python developer with expertise in web frameworks.
Always provide code examples and explain your reasoning.
Be concise but thorough in your explanations.
""")

messages = [
    system_msg,
    HumanMessage("How do I create a REST API?")
]
response = model.invoke(messages)  # Returns AIMessage
print(response.content)
print(response.usage_metadata)

