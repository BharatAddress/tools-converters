import subprocess
from pathlib import Path


def test_osm_to_register_help():
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(["python", str(repo_root / "osm_to_register.py"), "--help"], capture_output=True, text=True)
    assert result.returncode == 0


def test_join_lgd_pin_help():
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(["python", str(repo_root / "join_lgd_pin.py"), "--help"], capture_output=True, text=True)
    assert result.returncode == 0
