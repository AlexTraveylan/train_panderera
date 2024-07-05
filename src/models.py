import pandera as pa


class Schema(pa.DataFrameModel):
    pen_uuid: int = pa.Field(gt=0)
    name: str
    sexe: str = pa.Field(str_matches="^[MF]$", nullable=True)
