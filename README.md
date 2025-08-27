![CI](https://github.com/BharatAddress/tools-converters/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/BharatAddress/tools-converters/actions/workflows/codeql.yml/badge.svg)

# Bharat Address Converters

Format bridges and joins for the Bharat Address schema.

Tools:
- `osm_to_register.py`: Map OSM `addr:*` tags into the register schema
- `register_to_osm.py`: Export register features into OSM-style tags
- `join_lgd_pin.py`: Attach LGD identifiers and validate declared PIN ranges using a crosswalk CSV

Install:
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
