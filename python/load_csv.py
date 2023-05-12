import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column


engine = create_engine("iris+emb:///")

conn = engine.connect()

metadata = MetaData()

people = Table('people', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

metadata.create_all(engine)  # Creates the table

df = pd.read_csv('/home/irisowner/dev/data/people.csv')

df.to_sql('people', con=engine, if_exists='append', index=False)
