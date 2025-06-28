from openai import OpenAI

from src.utils import load_dotenv

load_dotenv(".env")

server_url = "http://127.0.0.1:8000/mcp/"

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "facebook_business_mcp",
            "server_url": server_url,
            "require_approval": "never",
        },
    ],
    input="check the health of the facebook business mcp server",
)

print(resp.output_text)
