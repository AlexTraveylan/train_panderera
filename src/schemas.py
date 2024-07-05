import pandera as pa

schema = pa.DataFrameSchema(
    {
        "pen_uuid": pa.Column(int, checks=pa.Check.greater_than(0)),
        "name": pa.Column(str),
        "sexe": pa.Column(str, pa.Check.isin(["M", "F"])),
    }
)
