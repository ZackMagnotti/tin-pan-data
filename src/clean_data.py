import sqlite3
import pandas as pd

song_parameters = ['tempo',
                   'key',
                   'mode',
                   'valence',
                   'danceability', 
                   'energy',
                   'liveness', 
                   'loudness', 
                   'acousticness', 
                   'instrumentalness',
                   'speechiness']

# normal parameters are the parameters
# that only range from 0 to 1
normal_parameters = ['valence',
                     'danceability', 
                     'energy',
                     'liveness', 
                     'acousticness', 
                     'instrumentalness',
                     'speechiness']

def get(save=False):
  '''
  Function to perform the basic cleaning and organization of
  the billboard-200 dataset.

    INPUT
    ---------
    save (OPTIONAL - Boolean): Boolean, if true save outputs to csv before returning


    OUTPUT
    ---------
    out ( Tuple(pd.DataFrame) ) : tuple of dataframes containing the cleaned data
  '''
  conn = sqlite3.connect('data/billboard-200.db')

  albums_raw = pd.read_sql_query('select * from albums', conn)[1:]

  # sanitize rank and date and create "power" datapoint
  albums_raw['rank'] = pd.to_numeric(albums_raw['rank'], downcast='signed')
  albums_raw['power'] = 1 / albums_raw['rank']
  albums_raw['date'] = pd.to_datetime(albums_raw['date'])

  # fill in missing artist names
  albums_raw[albums_raw['album']=='Silhouette'] = albums_raw[albums_raw['album']=='Silhouette'].replace({'':'Kenny G'})
  albums_raw[albums_raw['album']=='Roots Of Country Music (1965)'] = albums_raw[albums_raw['album']=='Roots Of Country Music (1965)'].replace({'':'Various Artists'})

  # albums: aggregated data about every album
  albums = (albums_raw.groupby(['album', 'artist'])
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
#   albums = albums.reset_index()

  # artists: aggregated data about every artist
  artists = (albums_raw.groupby('artist')
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
        duration_ms,
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

  # add colum to albums for average
  # song parameter values of the songs
  # in each album
  albums[song_parameters] = (songs.join(albums, on=['album', 'artist'])
                                  .groupby(['album', 'artist'])
                                  .mean()
                            )[song_parameters]

  if save:
    albums_raw.to_csv('data/albums_raw.csv')
    artists.to_csv('data/artists.csv')
    albums.to_csv('data/albums.csv')
    songs.to_csv('data/songs.csv')
  
  out = (albums_raw,
         albums,
         artists,
         songs)

  return out