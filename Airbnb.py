import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(layout= "wide")
st.markdown("""
    <h1 style='text-align: center;'>AIRBNB DATA ANALYSIS</h1>
    """, unsafe_allow_html=True)
st.write("")

st.markdown(f""" <style>.stApp {{
                        background:url("https://images.contentstack.io/v3/assets/bltb428ce5d46f8efd8/blt304100c88b563ae5/5e72688401b3dc04d25c31dd/BeloRauschBG.png?crop=16:9&width=1050&height=591&auto=webp");
                        background-size: cover}}
                     </style>""", unsafe_allow_html=True)

#Uploading CSV files
df_US= pd.read_csv("/content/US_Airbnb_final.csv")
df_Brazil= pd.read_csv("/content/Brazil_Airbnb_final.csv")
df_Canada= pd.read_csv("/content/Canada_Airbnb_final.csv")
df_Hong= pd.read_csv("/content/Hong_Airbnb_final.csv")
df_Port= pd.read_csv("/content/Portugal_Airbnb_final.csv")
df_Spain= pd.read_csv("/content/Spain_Airbnb_final.csv")
df_Turkey= pd.read_csv("/content/Turkey_Airbnb_final.csv")
df_Aus= pd.read_csv("/content/AUS_Airbnb_final.csv")
df_Air= pd.read_csv("/content/Airbnb_final.csv")


# select= option_menu("Explore", ["Home", "Data Exploration"],orientation="horizontal")
select = option_menu(
    menu_title = None,
    options = ["Home","Explore Data"],
    icons =["house","bar-chart"],orientation="horizontal")
if select == "Home":
  text_content = """
    <h2 style='text-align: center; color: black;'>Welcome to my Airbnb data analysis project</h2>
    <p style='font-size: 18px; text-align: center;'>In this endeavor, we delve into the vast repository of Airbnb listings, seeking to extract meaningful insights through meticulous data analysis, cleaning, and visualization.
    At its core, our project is driven by a desire to uncover the underlying dynamics of the Airbnb marketplace. By leveraging MongoDB Atlas, a powerful cloud-based database platform, we are equipped with the tools to navigate through extensive datasets, allowing us to unlock valuable insights that lie within.
    Our objectives are multifaceted. Firstly, we aim to meticulously clean and prepare the data, ensuring its integrity and reliability for subsequent analysis. With a solid foundation laid, we then delve into the realm of interactive geospatial visualizations, where we bring the data to life through immersive maps and dynamic plots.
    Through these visualizations, we seek to discern patterns, trends, and anomalies within the Airbnb ecosystem. From pricing differentials to availability fluctuations and location-based preferences, every facet of the data is scrutinized to uncover the hidden narratives that shape the Airbnb marketplace.
    Our journey is not merely one of exploration but of discovery. As we traverse through the data, we aim not only to present findings but to glean insights that inform decision-making and drive actionable outcomes. Whether it's understanding pricing dynamics, optimizing listing strategies, or identifying emerging market trends, our analysis endeavors to empower stakeholders with the knowledge to navigate the Airbnb landscape with confidence.
    Join us as we embark on this analytical odyssey, where data becomes our compass and MongoDB Atlas our guiding light, illuminating the path to a deeper understanding of the Airbnb phenomenon.</p>
        """

  # Display the text using markdown function
  st.markdown(text_content, unsafe_allow_html=True)

def chats():
  st.write("Data Analysis in",country)
  df_1=a.groupby("property_type").agg({"price":"mean","property_type":"count"}).sort_values("price")
  prop_name=[]

  for group_name,group_data in df_1.iterrows():
    prop_name.append(group_name)
  df_1["property name"]=prop_name

  df_2=a.groupby("host_neighbourhood").agg({"price":"mean","host_neighbourhood":"count"}).sort_values("price")
  Nei_names=[]
  for grp_name,grp_data in df_2.iterrows():
    Nei_names.append(grp_name)
  df_2["Neighbourhood"]=Nei_names

  df3=a.groupby(["city", "property_type"]).size().reset_index(name='number_of_reviews')

  df4=a.groupby("room_type").size().reset_index(name='number_of_reviews')

  col1,col2=st.columns(2)
  with col1:
    fig = px.bar(df_1,x='property name', y='price',color='price',color_discrete_sequence=px.colors.diverging.BrBG,
                  title='Property Type with Average Price'
          )
    st.plotly_chart(fig, use_container_width=True)

  with col2:
    fig = px.bar(df_2,x='Neighbourhood', y='price',color='price',color_discrete_sequence=px.colors.diverging.BrBG,
                  title='Average Price with respect to Neighbourhood'
          )
    st.plotly_chart(fig, use_container_width=True)

  col1,col2=st.columns(2)
  with col1:
    fig = px.sunburst(a, path=['city', 'property_type'], values='number_of_reviews',
                    title='City and its Property Types')
    st.plotly_chart(fig, use_container_width=True)

  with col2:
    fig = px.bar(a, x='room_type', y='number_of_reviews',
             labels={'room_type': 'Room Type', 'number_of_reviews': 'Number of Reviews'},
             title='Room Type with Review')

    st.plotly_chart(fig, use_container_width=True)

if select == "Explore Data":
  
    country= st.radio("Select A Country To Analyse",["United States","Turkey","Portugal", "Canada", "Brazil","Hong Kong","Spain","Australia"], horizontal=True)

    if country == "United States":
      a=df_US
      chats()
    elif country == "Brazil":
      a=df_Brazil
      chats()
    elif country == "Canada":
      a=df_Canada
      chats()
    elif country == "Hong Kong":
      a=df_Hong
      chats()
    elif country == "Portugal":
      a=df_Port
      chats()
    elif country == "Spain":
      a=df_Spain
      chats()
    elif country == "Turkey":
      a=df_Turkey
      chats()
    elif country == "Australia":
      a=df_Aus
      chats()

    

    # fig = px.scatter_mapbox(df_US, lat="Latitudes", lon="Longitudes",
    #                       color=df_US["price"] ,size=df_US["number_of_reviews"],
    #                     color_discrete_sequence=["fuchsia"], zoom=3,width=1200,
    #                     height=900)
    # fig.update_layout(
    #     mapbox_style="open-street-map")
    # fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})
    # st.plotly_chart(fig, use_container_width=True)
