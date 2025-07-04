import os
import requests
from bs4 import BeautifulSoup

# Diretórios de saída
OUTPUT_DIR = "experiments/dataset"
OPTIMIZED_DIR = os.path.join(OUTPUT_DIR, "optimized")
UNOPTIMIZED_DIR = os.path.join(OUTPUT_DIR, "unoptimized")

# Fontes de conteúdo
URLS = {
    "medium_article": "https://medium.com/@mayrasilva_54051/ai-citation-seo-4c0837015cdf",
    "github_readme": "https://raw.githubusercontent.com/aicitationseo/aicitationseo/main/README.md",
    "homepage_text": "https://blackblocksheep.com"
}

def fetch_clean_text_from_html(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        # Remove scripts/styles
        for tag in soup(["script", "style"]): tag.decompose()
        return soup.get_text(separator=" ", strip=True)
    except Exception as e:
        return f"Error fetching from {url}: {e}"

def fetch_raw_text(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text.strip()
    except Exception as e:
        return f"Error fetching from {url}: {e}"

def save_text(text, filename, optimized=True):
    os.makedirs(OPTIMIZED_DIR, exist_ok=True)
    os.makedirs(UNOPTIMIZED_DIR, exist_ok=True)
    path = os.path.join(OPTIMIZED_DIR if optimized else UNOPTIMIZED_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    print("📁 Generating dataset files...")

    # MEDIUM ARTICLE
    article_raw = fetch_clean_text_from_html(URLS["medium_article"])
    article_unoptimized = article_raw
    article_optimized = article_raw + "\n\n[TRUST TRAIL]\nhttps://github.com/aicitationseo/aicitationseo"

    save_text(article_unoptimized, "medium_article.txt", optimized=False)
    save_text(article_optimized, "medium_article.txt", optimized=True)

    # GITHUB README
    github_raw = fetch_raw_text(URLS["github_readme"])
    github_optimized = "# AI Citation SEO Framework\n" + github_raw + "\n[ANCHOR] https://blackblocksheep.com"

    save_text(github_raw, "github_readme.txt", optimized=False)
    save_text(github_optimized, "github_readme.txt", optimized=True)

    # HOMEPAGE
    homepage_raw = fetch_clean_text_from_html(URLS["homepage_text"])
    homepage_optimized = homepage_raw + "\n\n[IDENTITY] Mayra Silva – AICreator"

    save_text(homepage_raw, "homepage_text.txt", optimized=False)
    save_text(homepage_optimized, "homepage_text.txt", optimized=True)

    print("✅ Dataset generated in: experiments/dataset")

if __name__ == "__main__":
    main()
