
# Project4

**Render:**

I encountered a situation where the rendering platform is requesting my personal credit card information, which I perceive as a potential violation of data privacy. I have submitted a support ticket to address this concern, and I am hopeful that they will provide alternative options.

In the meanwhile, I would appreciate any recommendations for alternative deployment platforms that prioritize data security and do not require personal credit card information or accept the project. That would be highly appreciated.




**Data Loading:**
Loaded a dataset 'vehicles_us.csv' into a Pandas DataFrame named car_advertisement_df.

**Data Cleaning:**
Calculated and print the count of missing values in the DataFrame. Handled missing values in specific columns, convert data types, and fix errors in the 'model' column using the NumPy library.
Aslo, replaced all missing values in certain columns with 'unknown' or mean or median.

**Data Enrichment:**
Created a new column ('1_new_is_4wd') based on the values in the 'is_4wd' column, marking 'yes' for 1 and 'no' for other values.


**Visualization/ App :**
Using Streamlit, created a header and display the original DataFrame.
Created a scatter plot to explore the relationship between the number of cylinders and the price.
Created a histogram to visualize the distribution of selected columns (e.g., price, model year, condition, cylinders, fuel, odometer, transmission).


**User Interaction:**
Used Streamlit to allow the End-user to select a column for the histogram and choose whether to include NaN values.






