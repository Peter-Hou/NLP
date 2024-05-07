
# The documentation follows https://wiki.crystallography.net/RESTful_API/

import json

cod_api_docs = {
    "base_url": "https://www.crystallography.net/cod/result",
    "endpoint": "/search",
    "method": "GET",
    "description": "Search for crystallographic data entries based on a variety of parameters.",
    "parameters": {
        "id": {
            "description": "A string containing one or more COD IDs, separated by a comma or a new line. Use '%' as a wildcard to specify a range of IDs.",
            "type": "string",
            "required": False
        },
        "smarts": {
            "description": "A substructure query in SMILES arbitrary target specification.",
            "type": "string",
            "required": False
        },
        "text": {
            "description": "A keyword search across the entry metadata, including bibliographic information and names of compounds.",
            "type": "string",
            "required": False
        },
        "format": {
            "description": "The format of the results.",
            #"type": "enum",
            #"options": ["html", "csv", "json", "lst", "urls", "zip"],
            "type": "string",
            "value": "json",
            "required": True
        },
        "count": {
            "description": "The number of entries to return that match the search criteria.",
            "type": "integer",
            "required": False
        },
        "formula": {
            "description": "The empirical chemical formula of the crystal. Symbols must follow Hill notation and be separated by spaces.",
            "type": "string",
            "required": False
        },
        "el1": {
            "description": "Up to eight chemical element symbols that must appear in the chemical formula.",
            "type": "string",
            "required": False
        },
        "nel1": {
            "description": "Up to four chemical element symbols that must not appear in the chemical formula.",
            "type": "string",
            "required": False
        },
        "strictmin": {
            "description": "The minimum number of distinct chemical elements required in the chemical formula.",
            "type": "integer",
            "required": False
        },
        "spacegroup": {
            "description": "The Hermann-Mauguin or superspace group symbol of the crystal.",
            "type": "string",
            "required": False
        },
        "amin": {
            "description": "The minimum value of the lattice parameter 'a'.",
            "type": "float",
            "required": False
        },
        "journal": {
            "description": "The name of the journal in which the crystal structure was published.",
            "type": "string",
            "required": False
        },
        "year": {
            "description": "The year of publication of the crystal structure.",
            "type": "integer",
            "required": False
        },
        "doi": {
            "description": "The DOI linking to the online publication of the crystal structure.",
            "type": "string",
            "required": False
        },
        "has_fobs": {
            "description": "Flag denoting that entries must have associated X-ray reflection files (Fobs or Iobs).",
            "type": "boolean",
            "required": False
        },
        "include_duplicates": {
            "description": "Flag denoting whether to include entries marked as duplicates.",
            "type": "boolean",
            "required": False
        }
    },
    "response": {
        "description": "Depending on the 'format' parameter, returns HTML, CSV, JSON, list of IDs, URLs to CIF files, or a ZIP archive of CIF files. An HTML error message is returned if the result limit for ZIP is exceeded.",
        "content_type": "varies"
    }
}

# Convert the dictionary to a JSON string
cod_api_docs = json.dumps(cod_api_docs, indent=2)