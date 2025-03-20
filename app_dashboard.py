import sqlite3
import os
import pandas as pd # type: ignore
import plotly.express as px
import streamlit as st # type: ignore


st.set_page_config(page_title="Analiza użytkowników", layout="wide")

db_path = os.path.join(os.getcwd(), "users_data.db")
st.title("Analiza Aktywności Użytkowników Aplikacji Mobilnej")

if not os.path.exists(db_path): 
  st.error("Plik `users_data.db` nie został znaleziony! Upewnij się, że dodałeś go do repozytorium.")
else:
  conn = sqlite3.connect(db_path)

  df = pd.read_sql("SELECT * FROM users_activity", conn)
  conn.close()

  st.write("Podgląd danych:", df.head())
  
  
  #Filtracja
  selected_country = st.selectbox("Wybierz kraj:", df["country"].unique())
  filtered_df = df[df["country"] == selected_country]
  
  fig = px.line(filtered_df, x="date", y="screen_time_min", title=f"Czas spędzony w aplikacji - {selected_country}")
  st.plotly_chart(fig)
  
  st.write("Szczegółowe dane:")
  st.dataframe(filtered_df)
