from pathlib import Path

import pandas as pd

from src.models import Schema
from src.schemas import schema
from src.settings import DATA_FOLDER


def get_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)


def get_validated_data(data: pd.DataFrame) -> pd.DataFrame:
    validated_df = schema(data)
    return validated_df


def get_valided_with_model(data: pd.DataFrame) -> pd.DataFrame:
    validated_df = Schema.validate(data)
    return validated_df


if __name__ == "__main__":
    file_path = DATA_FOLDER / "data.csv"
    data = get_data(file_path)
    validated_df = get_validated_data(data)
    validated_df_model = get_valided_with_model(data)
    pen_uuids = validated_df_model[Schema.name]

    # print(validated_df.head())
    # print(validated_df_model.head())
    print(pen_uuids)
