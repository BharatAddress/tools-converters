#!/usr/bin/env python3
"""
Convert OSM-like features (GeoJSON with properties carrying addr:* tags)
into Bharat Address Register features (properties per address-register.schema.json).

Usage:
  python osm_to_register.py input.geojson output.geojson --ulb 294690 --state Karnataka --city Bengaluru
"""
import json
from pathlib import Path
import click


@click.command()
@click.argument("input_path", type=click.Path(exists=True, path_type=Path))
@click.argument("output_path", type=click.Path(path_type=Path))
@click.option("--ulb", "ulb_lgd", required=True, help="ULB LGD code")
@click.option("--state", required=True)
@click.option("--city", required=True)
@click.option("--strict/--lenient", default=False, help="Fail if unmapped required fields are missing")
def main(input_path: Path, output_path: Path, ulb_lgd: str, state: str, city: str, strict: bool):
    with input_path.open() as f:
        data = json.load(f)

    out = {"type": "FeatureCollection", "features": []}
    unmapped = []
    for feat in data.get("features", []):
        p = feat.get("properties", {})
        props = {
            "ulb_lgd": ulb_lgd,
            "street_name": p.get("addr:street") or p.get("street"),
            "house_number": p.get("addr:housenumber") or p.get("housenumber"),
            "locality": p.get("addr:neighbourhood") or p.get("addr:suburb") or p.get("locality") or "",
            "city": city,
            "state": state,
            "pin": p.get("addr:postcode") or p.get("pin") or "",
            "primary_digipin": p.get("digipin") or "",
        }
        if strict and (not props["street_name"] or not props["house_number"] or not props["pin"]):
            unmapped.append(props)
            continue
        out["features"].append({
            "type": "Feature",
            "properties": props,
            "geometry": feat.get("geometry"),
        })

    with output_path.open("w") as f:
        json.dump(out, f, ensure_ascii=False)
    if unmapped:
        click.echo(f"Warning: {len(unmapped)} features skipped due to unmapped required fields", err=True)
        if strict:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
