import json


new_api_docs = new_api_docs = {
  "api_documentation": {
    "title": "MPDS API - Download Endpoint",
    "version": "v0",
    "base_url": "https://api.mpds.io",
    "endpoint": "/download/facet",
    "method": "GET",
    "description": "Download data from MPDS using a REST-alike endpoint following HTTP protocol basics.",
    "authorization": {
      "header": {
        "Key": "Pl3n9ks3ozRiShHuezCmDqe2YEHhZbdq2rfpbB4ify42kfjX"
      },
      "example": "curl -H 'Key: Pl3n9ks3ozRiShHuezCmDqe2YEHhZbdq2rfpbB4ify42kfjX' 'https://api.mpds.io/v0/download/facet?q=\{'elements':'Ag-K'\}'"
    },
    "query_parameters": [
      {
        "name": "q",
        "type": "JSON-serialized object",
        "description": "A JSON object containing any reasonable combination of criteria, given in Table 1, column 'Machine-readable name'. Always required.",
        "note": "Ensure there is a backward slash before each curly bracket in the JSON object.",
        "example": "\\{'elements': 'Sr-Ti-O', 'classes': 'perovskite, conductor', 'sgs': 'Pm-3m', 'props': 'structural properties'}\\"
      }
    ],
    "response_format": {
      "default": "json",
      "description": "By default, the response is in JSON format, containing properties such as 'out' (an array of MPDS entries), 'npages' (number of pages), 'page' (current page number), 'count' (total number of hits), and 'error' (should be null unless there is an error)."
    },
    "error_handling": {
      "status_codes": {
        "200": "Request correctly understood and processed.",
        "400": "Wrong parameters, indicates an error in the request parameters.",
        "403": "Forbidden, usually due to incorrect or missing API key.",
        "429": "Too many requests, indicates that the request rate should be decreased."
      }
    }
  }
}

# Convert the dictionary to a JSON string
api_docs = json.dumps(new_api_docs, indent=2)