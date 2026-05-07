import subprocess
import sys
from pathlib import Path

NOTEBOOKS_DIR = Path(__file__).parent / "notebooks"

PIPELINE = [
    "data_integrity.ipynb",
    "data_chunking.ipynb",
    "data_merge_fips.ipynb",
    "geo_NaN_visuals.ipynb",
    "food_atlas_data_quality.ipynb",
    "meal_gap_data_quality.ipynb",
    "bar_graph.ipynb",
    "geo_visuals.ipynb",
    "linear_regression_model.ipynb",
]


def run_notebook(notebook: str) -> None:
    path = NOTEBOOKS_DIR / notebook
    print(f"\n--- Running: {notebook} ---")
    result = subprocess.run(
        [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout=600",
            str(path),
        ],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.returncode != 0:
        print(f"FAILED: {notebook} (exit code {result.returncode})", file=sys.stderr)
        sys.exit(result.returncode)
    print(f"OK: {notebook}")


def main() -> None:
    print(f"Running {len(PIPELINE)}-step pipeline from: {NOTEBOOKS_DIR}\n")
    for notebook in PIPELINE:
        run_notebook(notebook)
    print("\nAll steps completed successfully.")


if __name__ == "__main__":
    main()
