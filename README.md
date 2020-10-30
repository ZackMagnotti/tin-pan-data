# Tin Pan Data Analysis

Owner: Zack Magnotti
Email: zack@magnotti.net

This is an exploratory data analysis project aimed at a data set containing information on all of the billboard top 200 albums, and the songs in those albums, from 1/5/1963 to 1/19/2019.

The data for this project is too big to upload to github but can be found at https://components.one/datasets/billboard-200.

The documentation for Spotify EchoNest data can be found in the docs folder, or at https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/.

# Figures

![Vibe of Popular Music over time](images/vibe_full_timeseries.png)

![Vibe of Popular Music by Decade](images/vibe_by_decade.png)

# Hypothesis Testing

## Increase in "Speechiness" after the Rise of Rap and Hip-Hop

Hypothesis: The the average "speechiness" of music trends upward over time after 1985, as rap music was invented and popularized

![Equation](images/equations_speechiness.png)

### Results

```
Successfully rejected null hypothesis 
 p = 0.014
 T = 2.5
```

## Relationship Between Valence, Danceability, and Energy

Hypothesis: The relationship between danceability and energy is consistent over time, but both of thier relationships with valence (measure of positiveness) have drifted apart

![Equation](images/equations_VDE.png)

### Results

```
Successfully rejected null hypothesis on 
 [valence vs danceability] : p = 0.0

Failed to reject null hypothesis on 
 [danceability vs energy] : p = 0.8525

Successfully rejected null hypothesis on 
 [energy vs valence] : p = 0.0069
```
