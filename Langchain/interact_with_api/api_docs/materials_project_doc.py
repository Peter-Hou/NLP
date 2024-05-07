import json

material_api_docs = {
  "base_url": "https://api.materialsproject.org/materials/core/",
  "endpoints": [
    {
      "method": "GET",
      "description": "Query materials using various filters.",
      "parameters": {
        "material_ids": {
          "type": "string",
          "description": "Comma-separated list of material_id values to query on",
          "required": False
        },
        "formula": {
          "type": "string",
          "description": "Query by formula including anonymized formula or by including wild cards. A comma delimited string list of anonymous formulas or regular formulas can also be provided.",
          "required": False
        },
        "elements": {
          "type": "string",
          "description": "Query by elements in the material composition as a comma-separated list",
          "required": False
        },
        "deprecated": {
          "type": "boolean",
          "description": "Whether the material is marked as deprecated",
          "default": "false",
          "required": False
        },
        "_per_page": {
          "type": "integer",
          "description": "Number of entries to show per page (takes precedent over _limit and _skip). Limited to 1000.",
          "default": "100",
          "required": False
        },
        "_skip": {
          "type": "integer",
          "description": "Number of entries to skip in the search.",
          "default": "0",
          "required": False
        },
        "_limit": {
          "type": "integer",
          "description": "Max number of entries to return in a single query. Limited to 1000.",
          "default": "100",
          "required": False
        },
        "_all_fields": {
          "type": "boolean",
          "description": "Include all fields",
          "default": "false",
          "required": False
        },
        "license": {
          "type": "string",
          "description": "Query by license. Either commercial or non-commercial CC-BY",
          "default": "BY-C",
          "required": False
        }
      }
    }
  ]
}

# Convert the dictionary to a JSON string
material_api_docs = json.dumps(material_api_docs, indent=2)