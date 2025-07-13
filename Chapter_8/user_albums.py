"""
Start with your program from album.py. Write a while loop that allows
users to enter an album's artist and title. Once you have that
information, call make_album() with the user's input and print the 
dictionary that's created. Be sure to include a quit value in the while
loop.
"""

def make_album(artist_name, album_title, tracks=''):
    """Return a dictionary of information about a album."""
    album = {"Artist Name": artist_name, "Album Title": album_title}
    if tracks:
        album['tracks'] = tracks
    return album 

while True:
    print("Please list out an music album with the artist name, album title, and number of tracks (if possible): ")
    print("Enter '!' at any time to quit.")

    music_artist = input("Please enter the music artist: ")
    if music_artist == "!":
        break

    album_name = input("Please enter the album title: ")
    if album_name == "!":
        break

    num_tracks = input("Please enter the number of tracks: ")
    if num_tracks == "!":
        break
    if num_tracks == "":
        album1 = make_album(music_artist, album_name)
    else:
        album1 = make_album(music_artist, album_name, num_tracks)

    print(album1)