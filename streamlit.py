import streamlit as st

url = ' https://drive.google.com/drive/folders/1gNl3vReXZBquEp-EeYWjLcNJmTYTpo1Z'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)

