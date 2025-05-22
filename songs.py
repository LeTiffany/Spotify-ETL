import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

# AWS connection information
mysql_address  = 'myista322server.cx0guk6y0nea.us-east-1.rds.amazonaws.com'
mysql_username='tiffanyle'
mysql_password='Beardownista322'
mysql_database = 'myista322dbs'

# Gets connector and cursor
def get_conn_cur():
    cnx = mysql.connector.connect(user=mysql_username, password=mysql_password,
          host=mysql_address,
          database=mysql_database, port='3306')
    return (cnx, cnx.cursor())

# Runs queries
def run_query(query_string):
  conn, cur = get_conn_cur()  # Gets connection and cursor
  cur.execute(query_string)  # Executes string
  my_data = cur.fetchall()  # Fetches query data
  result_df = pd.DataFrame(my_data, columns=cur.column_names)
  cur.close()
  conn.close()
  return result_df

st.title('Song Popularity and Music Metrics')

st.text('Welcome to the dataset for the top songs in the nation!\
    The dataset provides great insights into contemporary music patterns\
    and popularity, drawing from the Spotify database and the Million Song Dataset.\
    Interative visualizations are provided for exploration of the\
    dataset in more detail.')

year = st.slider("Let's do the timewarp! Slide to a song release year!", min_value = 1960, max_value = 2010, value = 2010)

q = """SELECT COUNT(song_id) as songs, genre
    FROM song_identifiers
    WHERE year = %s
    GROUP BY genre""" % year

genre_counts = run_query(q)

st.subheader('Number of Most Popular Songs by Genre in %s' % year)

st.bar_chart(data = genre_counts, x = 'genre', y = 'songs', x_label = 'Genre', y_label = 'Number of Songs')

most_common = genre_counts.max()['genre']

st.text('The most common genre in ' + str(year) + ' was ' + str(most_common) + "!")

mode = st.selectbox('Select a mode:', ['Major', 'Minor'])

if mode == 'Major':
  q = """SELECT song_key, COUNT(song_id) as counts
      FROM song_elements
      WHERE mode = 1
      GROUP BY song_key;"""
else:
  q = """SELECT song_key, COUNT(song_id) as counts
      FROM song_elements
      WHERE mode = 0
      GROUP BY song_key;"""
      
key_counts = run_query(q)

st.subheader('Number of Songs by Key in the %s Scale' % mode)

st.bar_chart(data = key_counts, x = 'song_key', y = 'counts', x_label = 'Key', y_label = 'Number of Songs')

st.text('Keys (0-10), start at C Major and end at B Major. Each key has at least one song for each key,\
  indicating that many songs include both modes.')

explicit = st.checkbox("Include explicit songs?")

if explicit:
  q = """SELECT year, AVG(duration) as duration FROM song_identifiers
      JOIN song_measures ON song_identifiers.song_id = song_measures.song_id
      WHERE year > 1960
      GROUP BY year"""
else:
  q = """SELECT year, AVG(duration) as duration FROM song_identifiers
      JOIN song_measures ON song_identifiers.song_id = song_measures.song_id
      WHERE song_identifiers.song_id IN (SELECT song_id from song_elements WHERE explicit = FALSE)
      AND year > 1960
      GROUP BY year"""
      
duration_avg = run_query(q)

st.subheader('Song Duration vs. Year')

st.line_chart(data = duration_avg, x = 'year', y = 'duration', x_label = 'Year', y_label = 'Average Duration', width = 1000)

st.text('On avergage, songs with explicit content have a slightly shorter duration.')

st.text('Contemporary music is incredibly diverse in its subject matter and structure.\
  The dataset provides fascinating insight into this variety. Thanks for tuning in!')