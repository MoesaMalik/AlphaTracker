from __future__ import annotations

from pathlib import Path
import csv
from typing import List, Dict, Any, Optional


def _try_number(value: str) -> Any:
	"""Try to convert a string to int or float, otherwise return original string."""
	try:
		return int(value)
	except ValueError:
		pass
	try:
		return float(value)
	except ValueError:
		return value


def parse_csv(path: Path | str) -> List[Dict[str, Any]]:
	"""Parse a CSV file and return a list of dictionaries with basic type inference.

	Empty strings become None. Numeric strings are converted to int/float when possible.
	"""
	path = Path(path)
	rows: List[Dict[str, Any]] = []
	with path.open(newline="", encoding="utf-8") as fh:
		reader = csv.DictReader(fh)
		for raw in reader:
			parsed: Dict[str, Any] = {}
			for k, v in raw.items():
				if v is None:
					parsed[k] = None
					continue
				v = v.strip()
				if v == "":
					parsed[k] = None
				else:
					parsed[k] = _try_number(v)
			rows.append(parsed)
	return rows


def parse_closed_trades(csv_path: Optional[Path | str] = None) -> List[Dict[str, Any]]:
	"""Convenience wrapper to parse the default `data/closed_trades.csv` file in the repo.

	If `csv_path` is provided it will be used instead.
	"""
	if csv_path is None:
		repo_root = Path(__file__).resolve().parents[1]
		csv_path = repo_root / "data" / "closed_trades.csv"
	return parse_csv(csv_path)


if __name__ == "__main__":
	default = Path(__file__).resolve().parents[1] / "data" / "closed_trades.csv"
	if not default.exists():
		print(f"No default CSV found at: {default}")
	else:
		rows = parse_closed_trades(default)
		print(f"Loaded {len(rows)} rows from {default}")
		for i, r in enumerate(rows[:5], start=1):
			print(f"{i}: {r}")

