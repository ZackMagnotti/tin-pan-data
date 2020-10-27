import sqlite3
import pandas as pd

def get(save=False):
  conn = sqlite3.connect('data/billboard-200.db')

  albums_table = pd.read_sql_query('select * from albums', conn)[1:]

  # sanitize rank and date and create "power" datapoint
  albums_table['rank'] = pd.to_numeric(albums_table['rank'], downcast='signed')
  albums_table['power'] = 1 / albums_table['rank']
  albums_table['date'] = pd.to_datetime(albums_table['date'])

  # fill in missing artist names
  albums_table[albums_table['album']=='Silhouette'] = albums_table[albums_table['album']=='Silhouette'].replace({'':'Kenny G'})
  albums_table[albums_table['album']=='Roots Of Country Music (1965)'] = albums_table[albums_table['album']=='Roots Of Country Music (1965)'].replace({'':'Various Artists'})

  # albums: aggregated data about every album
  albums = (albums_table.groupby(['album', 'artist'])
                        .agg({'power': 'sum',
                              'rank' : ['count', 'mean'],
                              'date' : ['min', 'max'],
                              'length': 'first',
                              'track_length': 'first'})
           )

  albums.columns = ['power_rank',
                    'num_appearances',
                    'average_rank',
                    'first_appearance',
                    'last_appearance',
                    'length',
                    'track_length']
  albums = albums.reset_index()

  # artists: aggregated data about every artist
  artists = (albums_table.groupby('artist')
                        .agg({'power': 'sum',
                              'rank' : ['count', 'mean'],
                              'album': 'nunique',
                              'date' : ['min', 'max']})
            )

  artists.columns = ['power_rank',
                   'num_appearances',
                   'average_rank',
                   'num_albums',
                   'first_appearance',
                   'last_appearance']

  query = '''
  SELECT song,
        album,
        artist,
        date,
        key,
        mode,
        valence,
        tempo,
        time_signature,
        danceability,
        energy,
        liveness,
        loudness,
        acousticness,
        instrumentalness,
        speechiness
  FROM acoustic_features
  '''
  songs = pd.read_sql_query(query, conn)
  songs['date'] = pd.to_datetime(songs['date'])

  if save:
    artists.to_csv('data/artists.csv')
    albums.to_csv('data/albums.csv')
    songs.to_csv('data/songs.csv')
  
  out = (albums, 
         artists,
         songs)

  return out