import json
import requests
import argparse

def fetch_jsonld_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if '<script type="application/ld+json">' in response.text:
            start = response.text.index('<script type="application/ld+json">') + len('<script type="application/ld+json">')
            end = response.text.index('</script>', start)
            json_text = response.text[start:end].strip()
            return json.loads(json_text)
        else:
            raise ValueError("No JSON-LD script tag found.")
    except Exception as e:
        print(f"Error fetching JSON-LD: {e}")
        return None

def validate_trust_trails(data):
    errors = []
    trails = data.get("trustTrails", [])
    for trail in trails:
        url = trail.get("url")
        if url:
            try:
                r = requests.head(url, allow_redirects=True, timeout=5)
                if r.status_code >= 400:
                    errors.append(f"Broken URL in trustTrails: {url} (status code {r.status_code})")
            except Exception as e:
                errors.append(f"Error accessing trustTrail URL {url}: {e}")
    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate JSON-LD and Trust Trails")
    parser.add_argument('--url', type=str, required=True, help='URL of the site containing JSON-LD')
    args = parser.parse_args()

    print(f"Fetching JSON-LD from: {args.url}")
    data = fetch_jsonld_from_url(args.url)
    if not data:
        print("Failed to extract JSON-LD.")
        return

    print("Validating trustTrails URLs...")
    errors = validate_trust_trails(data)
    if not errors:
        print("✅ All trust trail URLs are valid.")
    else:
        print("❌ Found issues:")
        for err in errors:
            print(f" - {err}")

if __name__ == "__main__":
    main()
