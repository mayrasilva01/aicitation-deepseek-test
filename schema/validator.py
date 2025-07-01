import json
import requests
from jsonschema import validate, ValidationError

# Load JSON-LD schema
with open('ai-creator-schema.jsonld', 'r') as file:
    schema_data = json.load(file)

# Basic Schema.org structure for validation (can be extended)
basic_schema = {
    "type": "object",
    "properties": {
        "@context": {"type": "array"},
        "@type": {"type": "string"},
        "name": {"type": "string"},
        "url": {"type": "string"},
        "aiAuthorityScore": {"type": "number"},
        "trustTrails": {"type": "array"},
        "semanticScaffolding": {"type": "object"}
    },
    "required": ["@context", "@type", "name", "url"]
}

try:
    validate(instance=schema_data, schema=basic_schema)
    print("✅ Schema is valid.")
except ValidationError as e:
    print("❌ Schema validation error:", e.message)
