![CI](https://github.com/BharatAddress/tools-converters/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/BharatAddress/tools-converters/actions/workflows/codeql.yml/badge.svg)

# Bharat Address Converters

Format bridges and joins for the Bharat Address schema.

## Tools
- `osm_to_register.py`: map OSM `addr:*` tags into the register schema.
- `register_to_osm.py`: export register features into OSM-style tags.
- `join_lgd_pin.py`: attach LGD identifiers and validate PIN ranges using a crosswalk CSV.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python osm_to_register.py --help
```

## Usage examples
```bash
# OSM -> Bharat Address register
python osm_to_register.py input.geojson output.geojson --ulb 294690 --state Karnataka --city Bengaluru

# Register -> OSM-style tags
python register_to_osm.py input.geojson output.geojson

# Join LGD + PIN crosswalk
python join_lgd_pin.py input.geojson crosswalk.csv output.geojson
```

## When to use
- Use `osm_to_register.py` when ingesting OSM-tagged data.
- Use `register_to_osm.py` when exporting back to OSM-style tags.
- Use `join_lgd_pin.py` to validate LGD and PIN consistency.

## Repo layout
- `*.py`: conversion scripts.
- `requirements.txt`: Python dependencies.

## Who should use this
- Data teams converting between OSM and Bharat Address.
- Integrators normalizing address datasets.

## Contributor Guide
- Central guidelines: https://github.com/BharatAddress/.github/blob/main/AGENTS.md
