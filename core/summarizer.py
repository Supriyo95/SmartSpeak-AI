from openai import OpenAI
from core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

# Summarize the scraped content using OpenAI's GPT model
def summarize_content_with_openai(content):
    prompt = (
        f"Summarize the following content scraped in 2-3 lines from {content['url']}.\n"
        f"Titles: {content['titles']}\n"
        f"Paragraphs: {content['paragraphs']}\n"
        f"Links: {content['links']}\n"
        f"CEO: {content.get('ceo', 'Not Found')}\n"
        f"Email: {content.get('email', 'Not Found')}\n"
        f"Phone: {content.get('phone', 'Not Found')}\n"
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content
