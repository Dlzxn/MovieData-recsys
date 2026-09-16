import pandas as pd
from pathlib import Path


def read_parquet(file_names: list[str]) -> list[pd.DataFrame]:
    return [
        pd.read_parquet(Path(__file__).resolve().parent.parent / "data" / "processed" / f"{x}.parquet")
        for x in file_names
            ]
