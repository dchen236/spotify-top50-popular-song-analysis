# spotify-top50-popular-song-analysis

This is the final project for stats101a spring20 from UCLA taught by professor [Robert Gould](http://www.stat.ucla.edu/~rgould/Home/About_Me.html) and TA Xinzhou Ge
The dataset we will be using can be found at [data/top50_with_lyrics_bio.csv](https://github.com/dchen236/spotify-top50-popular-song-analysis/blob/master/data/top50_with_lyrics_bio.csv). 

We utlized the orginal [top-50.csv](https://www.kaggle.com/leonardopena/top50spotify2019) from kaggle and collected additional attributes such as lyrics of track and artist bio summary (not included in the original dataset).


# Table of content

- [STATS101A-Final-Project](#spotify-top50-popular-song-analysis)
- [Data Codebook ](#data-codebook)
  * [CSV files](#CSV-files)
   * [Attributes](#Attributes)
- [Code Usage](#Code-Usage)
  * [Install dependency](#install-dependency)
  * [Run script](#Run-script)
- [Resources](#Resources)

# Data Codebook 

### CSV files

- top50.csv: the original csv file from [Kaggle](https://www.kaggle.com/leonardopena/top50spotify2019)

- top50_with_lyrics_bio.csv: original csv file concatenated with Track.Lyrics (lyrics of the track obtained from genius API) column and Artist.Bio column (summary of artist bio obtained from last.fm API)


### Attributes
There are 50 rows and 15 columns

The first 13 columns are the same as the original Kaggle dataset , we copied the summary of each attribute from the original page, you can get more details from [here](https://www.kaggle.com/leonardopena/top50spotify2019). The last two columns (in bold font) are collected by ourselves. 

- Track.Name: Name of the track
- Artist.Name: Name of the Artist
- Genre: the genre of the track
- Beats.Per.Minute: The tempo of the song.
- Energy: The energy of a song - the higher the value, the more energtic. song
- Danceability: The higher the value, the easier it is to dance to this song.
- Loudness..dB.: The higher the value, the louder the song.
- Liveness: The higher the value, the more likely the song is a live recording.
- Valence: The higher the value, the more positive mood for the song.
- Length: The duration of the song.
- Acousticness..: The higher the value the more acoustic the song is.
- Speechiness: The higher the value the more spoken word the song contains.
- Popularity: The higher the value the more popular the song is.
- **Track.Lyrics:** The lyrics of the song (obtained from genius api)
- **Artist.Bio**: The bio summary of the artist (obtained from last.fm api)


The attributes of a song such as beats per minute, danceability and energy etc are defined by Spotify which can be obtained from Spotify for Developers api, [learn more](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)

# Code Usage

### Install dependency:

```
pip instal pandas 
pip install lyricsgenius
pip install pylast
```

### Run script

To use this code: you need to replace the API tokens and other relevant info in the config.py file
 1. To get the artist bio summary, we will use last.fm API, you need to [register a free account](https://www.last.fm/api/) (required)
 2. To get lyrics of track, we will use [LyricsGenius api]( https://github.com/johnwmillr/LyricsGenius), to use the api, you need to [register a free account from geniu.com ]( https://genius.com/api-clients) (required)
 3. Replace API_KEY,  API_SECRET, username and password from last.fm and token from genius in config.py with your own (required)
 4. Replace the path of input spotify_top_50 csv file (optional)
 5. Replace in the path of output file with lyrics and bio_summary (optional)
 6. If you have installed the dependency and replaced your own tokens and api key, you can simply run the code with command python3 data_collection.py from terminal 
    
# Resources

- https://www.kaggle.com/leonardopena/top50spotify2019
- https://github.com/johnwmillr/LyricsGenius
- https://github.com/pylast/pylast
