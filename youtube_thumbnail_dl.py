import streamlit as st

st.title("Youtube Thumbnail Downloader")

url = st.text_input('Enter a Youtube Video Complete URL')
id = url.split('=')[-1]

max_res = 'https://img.youtube.com/vi/'+id+'/maxresdefault.jpg'

st.text('Max Resolution Thubmnail - Right Click and Save it!!!')

st.image(max_res)

