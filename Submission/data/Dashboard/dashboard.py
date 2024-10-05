import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

day_df = pd.read_csv('Final_day.csv')
hour_df = pd.read_csv('Final_hour.csv')

st.title('Bike Rental Dashboard') 

st.subheader('Overview of Day Dataset')
st.write("First 5 rows of day_df:")
st.dataframe(day_df.head())

st.subheader('Overview of Hour Dataset')
st.write("First 5 rows of hour_df:")
st.dataframe(hour_df.head())

st.subheader('Total Bike Rentals by Weekday')
rentals_by_weekday = day_df.groupby('weekday')['cnt'].sum().reset_index()

fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.barplot(x='weekday', y='cnt', data=rentals_by_weekday, palette='coolwarm', ax=ax1)
ax1.set_title('Total Bike Rentals per Weekday')
ax1.set_xlabel('Weekday')
ax1.set_ylabel('Total Rentals')
plt.xticks(rotation=45)
st.pyplot(fig1)


st.subheader('Average Bike Rentals by Weather Condition')
avg_rentals_by_weather = day_df.groupby('weathersit')['cnt'].mean().reset_index()


fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.barplot(x='weathersit', y='cnt', data=avg_rentals_by_weather, palette='coolwarm', ax=ax2)
ax2.set_title('Average Bike Rentals per Weather Condition')
ax2.set_xlabel('Weather Situation')
ax2.set_ylabel('Average Rentals')
st.pyplot(fig2)