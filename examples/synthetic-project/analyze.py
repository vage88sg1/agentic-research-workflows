"""Synthetic demonstration only. Run from this directory using Python 3.10+."""
import csv
import json
from pathlib import Path
from statistics import mean

with Path('observations.csv').open() as stream:
    values = [float(row['value']) for row in csv.DictReader(stream)]
Path('results.json').write_text(json.dumps({'n': len(values), 'mean': mean(values)}, indent=2) + '\n')
