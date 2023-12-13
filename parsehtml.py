from bs4 import BeautifulSoup
import re

def remove_html_tags(input_text):
    # Use BeautifulSoup to parse HTML and extract text
    soup = BeautifulSoup(input_text, 'html.parser')
    text_content = soup.get_text()

    # Remove extra whitespaces and newlines
    text_content = text_content.strip()

    return text_content

if __name__ == "__main__":
    # Example usage:
    html_file = "./bs.html"
    with open(html_file, "r+", encoding="utf-8") as mfile:
        lines = mfile.readlines()
    html_content = " ".join(lines);
    result = remove_html_tags(html_content)
    result.replace("\t", "")
    result.replace("                                         ","")
    results = result.split("learn more")

    outcomes = [line.strip() for line in results if line.strip()]
    outcomes = [outcome.lower() for outcome in outcomes if outcome and outcome.lower() not in ("facebook","like")]
    with open("RESULT.txt", "w+", encoding="utf-8") as outcome:
        for out in outcomes:
            outcome.write(out)