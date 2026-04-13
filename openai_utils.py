from openai import AzureOpenAI
from config import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_MODEL

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def get_insights(text):
    prompt = f"""
    Analyze this call transcript and provide:
    - Sentiment
    - Intent
    - Key issues
    - Conversion probability

    Transcript:
    {text}
    """

    response = client.chat.completions.create(
        model=AZURE_OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
