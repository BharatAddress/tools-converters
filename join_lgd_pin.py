#!/usr/bin/env python3
"""
Join a dataset with an LGD-to-PIN crosswalk and report PIN validity for each feature.

Crosswalk CSV columns expected: ulb_lgd,pin

Usage:
  python join_lgd_pin.py input.geojson crosswalk.csv output.geojson
"""
import csv
import json
from pathlib import Path
import click


@click.command()
@click.argument("input_path", type=click.Path(exists=True, path_type=Path))
@click.argument("crosswalk_csv", type=click.Path(exists=True, path_type=Path))
@click.argument("output_path", type=click.Path(path_type=Path))
def main(input_path: Path, crosswalk_csv: Path, output_path: Path):
    with input_path.open() as f:
        data = json.load(f)

    valid_pins = {}
    with crosswalk_csv.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            ulb = row.get("ulb_lgd")
            pin = row.get("pin")
            if ulb and pin:
                valid_pins.setdefault(ulb, set()).add(pin)

    for feat in data.get("features", []):
        p = feat.get("properties", {})
        ulb = p.get("ulb_lgd")
        pin = p.get("pin")
        is_valid = (pin in valid_pins.get(ulb, set())) if (ulb and pin) else False
        p["pin_valid_for_ulb"] = bool(is_valid)

    with output_path.open("w") as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
