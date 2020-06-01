# spotify-top50-popular-song-analysis

This is the final project for stats101a spring20 from UCLA taught by professor [Robert Gould](http://www.stat.ucla.edu/~rgould/Home/About_Me.html) and TA Xinzhou Ge
The dataset we will be using can be found at [processed_dataset.csv](https://github.com/dchen236/spotify-top50-popular-song-analysis/blob/master/data/processed_dataset.csv). 

We adapted the [dataset from kaggle)[https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year] containing top spotify songs from 2010 to 2019 and added additional attribuets such as artist gender and lyrics reading ease scroe. 

# Team Member
- Danni Chen
- Yufeng Zhang

# Table of content

- [STATS101A-Final-Project](#spotify-top50-popular-song-analysis)
- [Team Memember](#team-member)
- [Data Codebook ](#data-codebook)
  * [CSV files](#CSV-files)
   * [Attributes](#Attributes)
- [Code Usage](#Code-Usage)
  * [Install dependency](#install-dependency)
  * [Run script](#Run-script)
- [Resources](#Resources)

# Data Codebook 

### CSV files

- [processed_dataset.csv](https://github.com/dchen236/spotify-top50-popular-song-analysis/blob/master/data/processed_dataset.csv): we restricted our analysis on songs after 2016, we collected additional attribuets: lyrics.ease.score and artist.gender using external source [Singer's Gender](https://www.kaggle.com/rkibria/singersgender). We restricted our analysis on songs with artist gender available. The finalized dataset processed_dataset.csv contains 126 songs.

### Attributes
There are 16 attribuets 

- title: title of the song
- artist: artist name
- top genre: genre of the song
- year: the year when the songs is at top50 list
- bpm: beat per minutes 
- nrgy: energy of the song, higher means more energetic
- dnce: dancibility, higher means easier to dance to the song
- dB: loundness of the song, the higher the lounder
- live: liveness of the song, higher means the song is likely to be a live recording
- val: valence of the song, higer means positive mood for the song. 
- dur: duration of the songs in seconds
- acous: acousticness of the song, higher value means the song is more acoustic 
- spch: speechness of the song, the higher the value, the more spoken word the song contains
- pop: popularity of the song
- artist.gender: gender of the artist
- lyrics.ease.score: lyrics reading ease score (obtained from [textstat](https://pypi.org/project/textstat/) flesch_reading_ease), the original dataset doesn't have song lyrics, we used genius api to collect the lyrics.(the code is available at data_collection.py) 

Attribuets bpm, nrgy, dncb, dB, live, val, dur, acous, spch and pop is defined by Spotify, details are available at [Spotify for Developers](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/) 

# Code Usage

### Install dependency:

```
pip instal pandas 
pip install lyricsgenius
pip install pylast
pip install textstat
```

### Run script
The data_collection.py can collect artist.bio and song lyrics
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
