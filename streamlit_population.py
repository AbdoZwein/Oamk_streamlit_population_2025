import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df_visu = pd.read_csv('./OAMK_Data_Analytics/population_country_columns.csv')
#title of the dashboard
st.title('Population of Countries Over the Years')
# multiselect box for all columns except year (ie. countries)
columns = st.multiselect('Countries', df_visu.columns[1:])
# line chart for the selected countries
st.line_chart(df_visu, x='year', y=columns, y_label='Population', x_label='Year', height=500, width=700)

# streamlit can handle matplotlib and plotly graphics
columns = st.multiselect('Countries', df_visu.columns[1:], key = 'bar_selector')
fig, ax = plt.subplots(figsize=(10,6))
bottom_line = 0
for country in columns:
    plt.bar(df_visu['year'], df_visu[country]/1000000, bottom = bottom_line, width=4, label=country)
    bottom_line += df_visu[country]/1000000

plt.title('Population of Selected Countries Over the Years')
plt.xlabel('Year')
plt.ylabel('Population in millions')
plt.legend(loc='upper left')
plt.grid()
st.pyplot(fig) # display the matplotlib figure in streamlit