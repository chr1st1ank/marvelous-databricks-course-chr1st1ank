import tomllib
from pathlib import Path

import pydantic


class Config(pydantic.BaseModel):
    data_file: str
    catalog_name: str
    schema_name: str
    table_name_prefix: str
    test_ratio: float = 0.2

    @staticmethod
    def from_toml(toml_file: Path):
        with toml_file.open("rb") as fp:
            return Config.model_validate(tomllib.load(fp))
