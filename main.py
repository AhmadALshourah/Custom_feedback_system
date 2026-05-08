from dotenv import load_dotenv, find_dotenv
import sub
from langchain.chains import create_tagging_chain
from langchain_community.chat_models import ChatOpenAI

_ = load_dotenv(find_dotenv())

llm = ChatOpenAI()

schema = {
    "properties": {
        "category": {
            "type": "string", "enum": [
                "you can put the categories here"
            ], "description": "The category of the student review"
        },
        "keywords": {
            "type": "string",
            "description": "mention the keywords for the selected review category"
        },
    },
    "required": ["category", "keywords"]
}

chain = create_tagging_chain(schema, llm)
complaints = sub.get_data(0, 10)
for c in complaints:
    result = chain.run(c)
    sub.add_data([c], [result["category"]], [result["keywords"]])
    print(c)
