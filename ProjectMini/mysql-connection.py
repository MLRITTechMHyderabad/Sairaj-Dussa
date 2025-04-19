import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, text

database = "youtube_2k25"
database_url = f"mysql+pymysql://root:root@localhost/{database}"

server_connection = create_engine("mysql+pymysql://root:root@localhost/")
with server_connection.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database}"))
    print(f"Database '{database}' is ready.")

engine = create_engine(database_url)

file = "cleaned_youtube_2025_dataset.csv"
try:
    df = pd.read_csv(file)
    if df.empty:
        print("Error: The dataset is empty! Check your file and try again.")
        exit()
    print(f"Successfully loaded dataset: {file}")
except Exception as e:
    print(f"Failed to load dataset: {e}")
    exit()

column_mapping = {col: col.strip().replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "") for col in df.columns}
df.rename(columns=column_mapping, inplace=True)

metadata = MetaData()
table_columns = []

for col in df.columns:
    dtype = df[col].dtype
    if dtype == "object":
        table_columns.append(Column(col, String(255)))  
    elif dtype == "int64":
        table_columns.append(Column(col, Integer)) 
    elif dtype == "float64":
        table_columns.append(Column(col, Float))  
    else:
        table_columns.append(Column(col, String(255)))  

youtube_dataset = Table("youtube_dataset", metadata, *table_columns)

metadata.create_all(engine)
print("Table 'youtube_dataset' has been created successfully.")

try:
    with engine.begin() as connection:
        for _, row in df.iterrows():
            row_data = row.to_dict()
            connection.execute(youtube_dataset.insert().values(**row_data))
    print("Data has been successfully inserted into the database.")
except Exception as e:
    print(f"Error while inserting data: {e}")

print("\n Sample dataset preview:")
print(df.tail())
print(f"Total rows inserted: {len(df)}")