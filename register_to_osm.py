#!/usr/bin/env python3
"""
Convert Bharat Address Register features into OSM-style tags in properties.

Usage:
  python register_to_osm.py input.geojson output.geojson
"""
import json
from pathlib import Path
import click


@click.command()
@click.argument("input_path", type=click.Path(exists=True, path_type=Path))
@click.argument("output_path", type=click.Path(path_type=Path))
def main(input_path: Path, output_path: Path):
    with input_path.open() as f:
        data = json.load(f)

    out = {"type": "FeatureCollection", "features": []}
    for feat in data.get("features", []):
        p = feat.get("properties", {})
        props = {
            "addr:street": p.get("street_name"),
            "addr:housenumber": p.get("house_number"),
            "addr:postcode": p.get("pin"),
            "addr:city": p.get("city"),
            "addr:state": p.get("state"),
        }
        out["features"].append({
            "type": "Feature",
            "properties": props,
            "geometry": feat.get("geometry"),
        })

    with output_path.open("w") as f:
        json.dump(out, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
