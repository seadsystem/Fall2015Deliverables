import pandas as pd

df = pd.read_csv('data.csv')
df.columns = [c.lower() for c in df.columns]

from sqlalchemy import create_engine
engine = create_engine('postgresql://michael:ElCharro37@localhost:5432/test_db')

df.to_sql("fhrs", engine)
