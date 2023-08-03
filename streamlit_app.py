import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('🥣 My Parents New Healthy Diner')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑 Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

if(len(fruits_to_show))>0:
  streamlit.dataframe(fruits_to_show)
else:
  streamlit.dataframe(my_fruit_list)

# Display the table on the page.
