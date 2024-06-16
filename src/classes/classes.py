import sqlalchemy

metadata = sqlalchemy.MetaData()


class_table = sqlalchemy.Table(
    "class",
    metadata,
    sqlalchemy.Column("id_class", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name_class", sqlalchemy.String(40), unique=True, index=True),
)

