# import files
import streamlit as st
import pandas as pd
import plotly.express as pe
import numpy as np
import matplotlib.pyplot as plt
# Load the data files into a DataFrame

car_advertisement_df = pd.read_csv('vehicles_us.csv')
print("bh",car_advertisement_df['model_year'].unique())

# Calculate count of missing values
car_advertisement_df.isna().sum()

# Print unique / nunique entries for each column to (1) identify missed spellings, (2) identify null values
car_advertisement_df['condition'].unique()

car_advertisement_df['fuel'].unique()

car_advertisement_df['is_4wd'].nunique()

#car_advertisement_df['new_is_4wd'].unique()

unique_car_model = car_advertisement_df['model'].unique()

car_advertisement_df['transmission'].unique()

car_advertisement_df['type'].unique()

car_advertisement_df['paint_color'].unique()



# counting obvious duplicates
car_advertisement_df.duplicated().sum()

# Fix data types
# Change model_year from float to int
car_advertisement_df['model_year'] = car_advertisement_df['model_year'].astype('Int64') 

print("bhbh",car_advertisement_df['model_year'].unique())
# add errors='ignore' so it ignores null values and replacing null values with NAN

# Change date_posted from object to datetype
car_advertisement_df['date_posted'] = pd.to_datetime(car_advertisement_df['date_posted'],errors='coerce')
# errors='coerce' --> use this so it doesn't throw an error if some values are null; b/c it will not convert null values to a datetime (those would be an error)

# Change cylinders from float to int
car_advertisement_df['cylinders'] = car_advertisement_df['cylinders'].astype('Int64')

# Change odometer from from float to int
car_advertisement_df['odometer'] = car_advertisement_df['odometer'].astype('Int64')
# Pass 'int64' which saves integers in the back end, which automatically igno




#car_advertisement_df['model_year'] = car_advertisement_df['model_year'].fillna(car_advertisement_df['model_year'].median())


#car_advertisement_df['model'] = np.where(car_advertisement_df['model']== 'ford f150', 'ford f-150', car_advertisement_df['model']) # np.where parameter ==(old value, new value, print other values as-is)

car_advertisement_df['model'] = np.where(car_advertisement_df['model']== 'ford f150', 'ford f-150',np.where(car_advertisement_df['model']== 'ford f250', 'ford f-250', np.where(car_advertisement_df['model']== 'ford f-350 sd', 'ford f-150 super duty', np.where(car_advertisement_df['model']== 'ford f250 super duty', 'ford f-250 super duty', np.where(car_advertisement_df['model']== 'ford f150 supercrew cab xlt', 'ford f-150 supercrew cab xlt', np.where(car_advertisement_df['model']== 'ford f350', 'ford f-350', np.where(car_advertisement_df['model']== 'ford f350 super duty', 'ford f-350 super duty', np.where(car_advertisement_df['model']== 'ford f-250 sd', 'ford f-250 super duty', car_advertisement_df['model']))))))))


#car_advertisement_df['model'] = car_advertisement_df['model'].str.lower()      # Change to lower case





# looping over column names and replacing missing values with 'unknown'
columns_to_replace = ['paint_color'] 
for r in columns_to_replace: 
    car_advertisement_df[r].fillna('unknown', inplace=True)

# Find and replace missing values with UNK (for int64 & float)

# looping over column names and replacing missing values with 0
columns_to_replace = ['odometer', 'cylinders','model_year'] 
for r in columns_to_replace: 
    car_advertisement_df['model_year'] = car_advertisement_df[r].fillna(car_advertisement_df[r].median())

# Find and replace missing values with UNK (for int64 & float)


# Filling any remaining missing values in the specified columns with 0
columns_to_replace = ['is_4wd']
for r in columns_to_replace:
    car_advertisement_df[r].fillna(0, inplace=True)




# Enrishing our DataFrame by creating a new column with yes and no 
# Change 1.0 to 'yes' and NaN to 'no' in is_4wd
car_advertisement_df['1_new_is_4wd']=['yes' if x==1 else 'no' if x is not None else 'no' for x in  car_advertisement_df['is_4wd']]







# Create title and table

st.header('Car Advertisement Stats')
car_advertisement_df = pd.read_csv('vehicles_us.csv')
car_advertisement_df 

# Create scatter plot

st.header('Is there a relationship between the number of cylinders and price?')

st.write("""**Scatter plot** """)

fig, ax=plt.subplots()
cylinder = ax.scatter(car_advertisement_df['cylinders'], car_advertisement_df['price'])
ax.set_xlabel('cylinders')
ax.set_ylabel('price')
ax.set_title('Relationship between cylinders and price')
st.pyplot(fig)


# Create histogram of price

st.header('Show distribution of price')

st.write("""**Histogram** """)

fig, ax=plt.subplots()

columns_to_select = ['price','model_year', 'condition','cylinders', 'fuel', 'odometer', 'transmission']

selected_columns = st.selectbox('Select column for histogram', columns_to_select)

include_nan = st.checkbox('Include nan values', value=True)
filtered_data = car_advertisement_df[selected_columns] if include_nan else car_advertisement_df[selected_columns]

histogram = ax.hist(filtered_data, bins=20, color='green', alpha=0.5, edgecolor='k')

ax.set_xlabel(selected_columns)
ax.set_ylabel('Count')
ax.set_title(f'Histogram of {selected_columns}')

st.pyplot(fig)

