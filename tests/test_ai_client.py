from modules.openai_client import OpenAIClient

client = OpenAIClient()

response = client.generate(
    """
Say hello in one sentence.
"""
)

print(response)