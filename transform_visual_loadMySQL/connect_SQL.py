

import pandas as pd
from sqlalchemy import create_engine

# Connection string
connection_string = 'mysql+mysqlconnector://root:#4t#42#294MySQL641#@localhost/new_db'

# Create the engine object
engine = create_engine(connection_string)

# Establish a connection
conn = engine.connect()

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('items.csv')

# Write the DataFrame to the database table
df.to_sql('neweggcard', con=engine, if_exists='append', index=False)

# Close the connection
engine.dispose()
