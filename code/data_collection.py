import lyricsgenius
import pylast
import pandas as pd
import config as cfg


def genius_api_authentication():
    genius = lyricsgenius.Genius(cfg.GENIUS_TOKEN)
    return genius

def last_fm_api_authentication():
    API_KEY = cfg.LAST_FM_API_KEY
    API_SECRET = cfg.LAST_FM_API_SECRET
    username = cfg.LAST_FM_username
    password_hash = pylast.md5(cfg.LAST_FM_password)
    lastfm_network = pylast.LastFMNetwork(api_key=API_KEY,
                                          api_secret=API_SECRET,
                                          username=username,
                                          password_hash=password_hash)
    return lastfm_network

if __name__ == "__main__":
    df = pd.read_csv(cfg.input_csv_path, encoding="latin1")
    genius = genius_api_authentication()
    lastfm_network = last_fm_api_authentication()
    song_lyrics = []
    artist_bio = []
    for song_name, artist_name in zip(df['Track.Name'], df['Artist.Name']):
        print(song_name, artist_name)
        song = genius.search_song(song_name, artist_name)
        artist = lastfm_network.get_artist(artist_name)
        try:
            song_lyrics.append(song.lyrics)
        except:
            song_lyrics.append("")
        try:
            bio_content = artist.get_bio_summary(language="en")
            artist_bio.append(bio_content)
        except:
            artist_bio.append("")
    df['Track.Lyrics'] = song_lyrics
    df['Artist.Bio'] = artist_bio
    df.to_csv(cfg.output_csv_path, index = False)
