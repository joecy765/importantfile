
# import numpy as np
# import pandas as pd
# from datetime import datetime
# import random
# import psycopg2
# from sqlalchemy import create_engine

# # Load and clean the data
# # df = pd.read_csv('rewards_data.csv')

# df = pd.read_csv (r"RewardsData.csv")

# # Assuming 'df' is your DataFrame
# df = df.drop('Tags', axis=1)


# # Step 2: Fill the empty cell on row 438, under the zip column
# if pd.isna(df.at[437, 'Zip']):

#     df.at[437, 'Zip'] = '11011'  # Note: pandas uses 0-based indexing

# df['Zip'] = df['Zip'].astype(str).str[:5]

# # Step 3: Truncate the zip numbers to the first 5 digits
# df['Zip'] = pd.to_numeric(df['Zip'], errors='coerce')
# zip_mean = int(df['Zip'].mean())

# df['Zip'] = df['Zip'].fillna(zip_mean).astype(int)



# # Replace "Winston Salem" with the right capitalization

# df['City'] = df['City'].str.replace('Winston Salem', 'Winston-Salem')#, #case=False)
# df['City'] = df['City'].str.replace('Winston Salem', 'Winston-Salem')#,# case=False)
# df['City'] = df['City'].str.replace('Winston Salem', 'Winston-Salem')#, #case=False)


# # Step 6: Remove every abbreviation in the city column
# # This step is a bit complex without knowing the exact pattern of abbreviations. Let's assume you want to remove any word that is all uppercase or has a specific pattern.


# df['City'] = df['City'].apply(lambda x: ''if isinstance(x, str) and len(x.strip())== 1 else x)


# # Step 7: Replace state abbreviations with full state names


# state_map = {
#     'AL': 'Alabama',
#     'AK': 'Alaska',
#     'AZ': 'Arizona',
#     'AR': 'Arkansas',
#     'CA': 'California',
#     'CO': 'Colorado',
#     'CT': 'Connecticut',
#     'DE': 'Delaware',
#     'FL': 'Florida',
#     'GA': 'Georgia',
#     'HI': 'Hawaii',
#     'ID': 'Idaho',
#     'IL': 'Illinois',
#     'IN': 'Indiana',
#     'IA': 'Iowa',
#     'KS': 'Kansas',
#     'KY': 'Kentucky',
#     'LA': 'Louisiana',
#     'ME': 'Maine',
#     'MD': 'Maryland',
#     'MA': 'Massachusetts',
#     'MI': 'Michigan',
#     'MN': 'Minnesota',
#     'MS': 'Mississippi',
#     'MO': 'Missouri',
#     'MT': 'Montana',
#     'NE': 'Nebraska',
#     'NV': 'Nevada',
#     'NH': 'New Hampshire',
#     'NJ': 'New Jersey',
#     'NM': 'New Mexico',
#     'NY': 'New York',
#     'NC': 'North Carolina',
#     'ND': 'North Dakota',
#     'OH': 'Ohio',
#     'OK': 'Oklahoma',
#     'OR': 'Oregon',
#     'PA': 'Pennsylvania',
#     'RI': 'Rhode Island',
#     'SC': 'South Carolina',
#     'SD': 'South Dakota',
#     'TN': 'Tennessee',
#     'TX': 'Texas',
#     'UT': 'Utah',
#     'VT': 'Vermont',
#     'VA': 'Virginia',
#     'WA': 'Washington',
#     'WV': 'West Virginia',
#     'WI': 'Wisconsin',
#     'WY': 'Wyoming'
# }



# df['State'] = df['State'].replace(state_map)


# # Step 8: Replace empty cells in the state column

# states_ordered = sorted(state_map.values())
# empty_state_count = df['State'].isna().sum()
# # empty_state_count = df[df['State'].isna()].sum()
# state_cycle = states_ordered * (empty_state_count// len(states_ordered) + 1)
# df.loc[df ['State'].isna(), 'State'] = state_cycle[:empty_state_count]



# # Reformat the dates in the birthday column to the proper format
# def reformat_date(date_str):
#     if pd.isna(date_str):
#         return np.nan
#     try:

#         for fmt in('%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y'):
#             try:
#                 dt = datetime.strptime(str(date_str), fmt)
#                 return dt.strftime('%Y-%m-%d')
#             except ValueError:
#                 continue
#         return np.nan
#     except:
#         return np.nan


# # Step 9: Reformat dates in the birthday column
# df['Birthdate'] = df['Birthdate'].apply(reformat_date)


# # Step 10: Replace empty cells in the birthday column with random birth dates



# def random_date(start_year=1950, end_year=2005):
#     year = random.randint(start_year, end_year)
#     month =random.randint(1, 12)
#     day = random.randint(1, 28)
#     return f"{year}--{month:02d}--{day:02d}"



# df['Birthdate'] = df['Birthdate'].fillna(df['Birthdate'].apply(lambda x: random_date())) #if pd.isna(x) else x)


# # Step 11: Delete rows with zip numbers less than 5 digits

# df = df[df['Zip'] >= 5]


# # Step 12: Populate empty cells in the city column with "Thomasville"

# df['City'] = df['City'].fillna('Thomasville')


# # Define your database credentials
# username = 'postgres'
# password = 'josesnat2020'
# host = 'localhost'
# database = 'my_database'


# # Create a connection to the PostgreSQL database
# conn_string =  f"postgresql://postgres:talent123@localhost/rewards_data"

# conn_string = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"


# try: 
    
# # Create a SQLAlchemy engine
#    engine = create_engine(conn_string)
#    print("Connected to PostgreSQL database!")

#     # Store the cleaned rewards data in the database
#    df.to_sql('rewards_data', con=engine, if_exists='replace', index=False)
#    print("Data loaded into PostgreSQL database!")

# except Exception as e:
#    print("Error connecting to PostgreSQL database:", str(e))