from bs4 import BeautifulSoup
import re
import csv
from source import html

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')


# Function to extract paragraph numbers and content with correct nesting
def extract_paragraphs(soup):
    paragraphs = []
    current_main_number = None

    divs = soup.find_all('div')
    for div in divs:
        text = div.get_text().strip()

        if text.startswith('(') or "утратил" in text.lower():
            continue

        # Main level (e.g., "1", "1.1", etc.)
        main_match = re.match(r'^(\d+\.) ', text)
        # Sub level (e.g., "1)", "1.1)", etc.)
        sub_match = re.match(r'^[0-9.]+\) ', text)

        if main_match:
            # This is a new main paragraph (e.g., "1.", "1.2.")
            current_main_number = main_match.group(1).strip()
            content = re.sub(r'^\d+\.', '', text).strip()
            paragraphs.append({
                "paragraphNumber": current_main_number,
                "content": content
            })

        elif sub_match:
            # This is a sub-paragraph (e.g., "1)", "1.1)")
            current_sub_number = sub_match.group(0).strip()
            content = re.sub(r'^[0-9.]+\)', '', text).strip()
            paragraphs.append({
                "paragraphNumber": f"{current_main_number} {current_sub_number}",
                "content": content
            })

    return paragraphs


# Function to write the parsed data to CSV
def write_to_csv(parsed_data, filename='output.csv'):
    # clean up
    open(filename, 'w').close()

    # write the data
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["ParagraphNumber", "Content"])

        # Write the data
        for paragraph in parsed_data:
            writer.writerow([paragraph['paragraphNumber'], paragraph['content']])


# Run the parser and export to CSV
# parsed_data = extract_paragraphs(soup)
# write_to_csv(parsed_data)

# print(f"Data has been written to output.csv")
# print("csv content:")
# print(open('output.csv').read())

parsed_data_from_csv = []
with open('output.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        parsed_data_from_csv.append(row)

print("longest paragraph length:", max([len(row['Content']) for row in parsed_data_from_csv]))
