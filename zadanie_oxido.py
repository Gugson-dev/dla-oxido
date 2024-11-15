import os
from openai import OpenAI

client = OpenAI(
    api_key='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'
)

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html_content(article_text):
    messages = [
        {"role": "system", "content": (
            "You are a helpful assistant that formats articles in HTML. "
            "Please convert the following article text into HTML. "
            "Use appropriate HTML tags, add image placeholders with the tag "
            "<img src='image_placeholder.jpg' alt='description of image'>, "
            "and add captions under each image where appropriate. "
            "Only return the content that goes between <body> and </body> tags."
        )},
        {"role": "user", "content": article_text}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" or any available model
        messages=messages,
        max_tokens=2000,
        temperature=0.5
    )

    return response.choices[0].message.content.strip()

def save_html(content, file_path='artykul.html'):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    article_file_path = 'Zadanie dla JJunior AI Developera - tresc artykulu.txt'
    
    article_text = read_article(article_file_path)
    
    html_content = generate_html_content(article_text)
    
    save_html(html_content)
    print(f"Generated HTML content saved to 'artykul.html'.")

if __name__ == "__main__":
    main()
