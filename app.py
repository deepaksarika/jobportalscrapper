import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the Zomato data
@st.cache
def load_data():
    dataframe = pd.read_csv("Zomato data .csv")
    return dataframe

dataframe = load_data()

# Display the first few rows of the data
st.write("## Zomato Data")
st.write(dataframe.head())

# Handle the 'rate' column
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)

# Show the updated data
st.write("## Updated Data")
st.write(dataframe.head())

# Show basic information about the data
st.write("## Data Information")
st.write(dataframe.info())

# Visualization: Countplot of restaurant types
st.write("## Countplot of Restaurant Types")
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
fig, ax = plt.subplots()
ax = sns.countplot(x=dataframe['listed_in(type)'])
st.pyplot(fig)

# Visualization: Line plot of total votes per restaurant type
st.write("## Total Votes per Restaurant Type")
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)
fig, ax = plt.subplots()
ax = sns.lineplot(data=result, x=result.index, y="votes", marker="o", color="green")
st.pyplot(fig)

# Visualization: Restaurant(s) with the maximum votes
st.write("## Restaurant(s) with the Maximum Votes")
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
st.write(restaurant_with_max_votes)

# Visualization: Distribution of ratings
st.write("## Ratings Distribution")
plt.hist(dataframe['rate'], bins=5)
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
fig, ax = plt.subplots()
ax.hist(dataframe['rate'], bins=5)
st.pyplot(fig)

# Visualization: Countplot of online orders
st.write("## Countplot of Online Orders")
sns.countplot(x=dataframe['online_order'])
fig, ax = plt.subplots()
ax = sns.countplot(x=dataframe['online_order'])
st.pyplot(fig)

# Visualization: Boxplot of ratings based on online orders
st.write("## Boxplot of Ratings based on Online Orders")
plt.figure(figsize=(6, 6))
sns.boxplot(x='online_order', y='rate', data=dataframe)
fig, ax = plt.subplots(figsize=(6, 6))
ax = sns.boxplot(x='online_order', y='rate', data=dataframe)
st.pyplot(fig)

# Visualization: Heatmap of restaurant types and online orders
st.write("## Heatmap of Restaurant Types and Online Orders")
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
fig, ax = plt.subplots()
ax = sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
st.pyplot(fig)
