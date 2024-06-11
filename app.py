import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache
def load_data():
    try:
        dataframe = pd.read_csv("Zomato data.csv")
        return dataframe
    except FileNotFoundError:
        st.error("Error: Could not find the data file. Please make sure the file exists and try again.")
        return None

dataframe = load_data()

if dataframe is not None:
    st.write(dataframe.head())

    def handleRate(value):
        value=str(value).split('/')
        value=value[0];
        return float(value)

    dataframe['rate']=dataframe['rate'].apply(handleRate)

    st.write(dataframe.head())
    st.write(dataframe.info())

    st.subheader("Count Plot of 'listed_in(type)'")
    sns.countplot(x=dataframe['listed_in(type)'])
    plt.xlabel("Type of restaurant")
    st.pyplot()

    st.subheader("Votes vs Type of Restaurant")
    grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data})
    plt.plot(result, c="green", marker="o")
    plt.xlabel("Type of restaurant", c="red", size=20)
    plt.ylabel("Votes", c="red", size=20)
    st.pyplot()

    max_votes = dataframe['votes'].max()
    restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
    st.write("Restaurant(s) with the maximum votes:")
    st.write(restaurant_with_max_votes)

    st.subheader("Count Plot of 'online_order'")
    sns.countplot(x=dataframe['online_order'])
    st.pyplot()

    st.subheader("Histogram of Ratings Distribution")
    plt.hist(dataframe['rate'], bins=5)
    plt.title("Ratings Distribution")
    st.pyplot()

    st.subheader("Boxplot of Ratings vs Online Order")
    plt.figure(figsize=(6, 6))
    sns.boxplot(x='online_order', y='rate', data=dataframe)
    st.pyplot()

    st.subheader("Heatmap")
    pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
    plt.title("Heatmap")
    plt.xlabel("Online Order")
    plt.ylabel("Listed In (Type)")
    st.pyplot()
