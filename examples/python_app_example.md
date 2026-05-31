# Few-Shot Example: Python Data / Automation Repository

## Repository Traits

This repository may include:

- Python scripts
- CLI flags
- CSV inputs
- spreadsheet inputs/outputs
- output folders
- virtual environments
- tests
- generated reports

## Example Prompt

```text
Fix the category totals not matching the sales data.
```

## Correct Interpretation

```text
csv category totals sales data parser aggregation date filter report output
```

## Example Route

```json
{
  "route_name": "csv_category_analytics",
  "description": "Fixes or extends CSV category aggregation and reporting logic.",
  "match_terms": [
    "category",
    "sales data",
    "totals",
    "csv",
    "aggregation"
  ],
  "negative_match_terms": [],
  "task_terms": "csv category totals sales data parser aggregation date filter report output",
  "recommended_scope": "python-analytics",
  "include_paths": [
    "src",
    "tests",
    "README.md"
  ],
  "avoid_paths": [
    ".venv",
    "__pycache__",
    "output",
    "dist"
  ],
  "related_systems": [
    "csv parser",
    "report generator"
  ],
  "validation_commands": [
    "python -m pytest"
  ],
  "known_pitfalls": [
    "Do not assume CSV date formats; inspect parser behavior.",
    "Preserve full scripts if the user expects full file updates.",
    "Do not overwrite generated output templates unless required."
  ],
  "confidence": 0.8
}
```
