from bs4 import BeautifulSoup
import json
import re
from source import html

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')


# Function to extract article number
def extract_article(text):
    match = re.search(r'Статья\s(\d+)', text)
    return int(match.group(1)) if match else None


# Function to extract paragraph numbers and content
def extract_paragraphs(soup):
    paragraphs = []
    current_paragraph_number = None
    for div in soup.find_all('div'):
        text = div.get_text()

        # Try to extract a paragraph number
        para_match = re.match(r'(\d+\.?\d*)\)', text)
        if para_match:
            current_paragraph_number = para_match.group(1)
            content = re.sub(r'\(.*?\)', '', text).strip()  # Remove any notes inside brackets
            paragraphs.append({
                "paragraphNumber": current_paragraph_number,
                "content": content,
            })

    return paragraphs


# Final function to extract all data
def extract_data(soup):
    result = []
    for div in soup.find_all('div'):
        text = div.get_text()

        # Extract article number
        article_number = extract_article(text)
        if article_number:
            # Extract paragraphs under this article
            paragraphs = extract_paragraphs(soup)
            result.append({
                "articleNumber": article_number,
                "paragraphs": paragraphs
            })

    return result


# Run the parser
parsed_data = extract_data(soup)

# Print output as JSON
print(json.dumps(parsed_data, ensure_ascii=False, indent=4))
