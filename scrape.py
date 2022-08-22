import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

# page configuration
st.set_page_config(
     page_title="Image Scraper",
     page_icon=":zap:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )


st.markdown("<h1 style='text-align: center;'>Image Scraper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword=st.text_input("Enter your Keyword")
    search=st.form_submit_button("Search")

placeholder = st.empty()
if keyword:
    page= requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'lxml')
    output = soup.find_all("div", class_="ripi6", )
    col1,col2 = placeholder.columns(2)

    for index,out in enumerate(output):
        figures=out.find_all("figure")
        for i in range(2):
            img= figures[i].find("img",class_='YVj9w')
            list=img["srcset"].split("?")
            anchor=figures[i].find("a", class_='rEAWd')

            if i==0:
                col1.image(list[0])
                btn = col1.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])
            else:
                col2.image(list[0])
                btn = col2.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])
 