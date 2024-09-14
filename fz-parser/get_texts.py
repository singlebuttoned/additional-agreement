from bs4 import BeautifulSoup

from source import html

# Extract texts from all divs and save them to raw_texts.txt
soup = BeautifulSoup(html, 'html.parser')
with open('raw_texts.txt', 'w', encoding='utf-8') as f:
    for div in soup.find_all('div'):
        text = div.get_text().strip()
        f.write(text + '\n')

print('Texts extracted and saved to raw_texts.txt')
print('First 100 rows:')
print('=' * 50)
with open('raw_texts.txt', 'r', encoding='utf-8') as f:
    for i in range(100):
        print(f.readline().strip())
print('=' * 50)