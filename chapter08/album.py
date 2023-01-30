'''
Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the albums dictionary. Make at least one new function call that includes the number of songs on an album.
'''

def make_album(artist_name, album_title, song_number=None):
    album = {}
    album[artist_name.title()] = album_title.title()
    if song_number:
        album['Number of Songs:'] = song_number
    print(album)

make_album('nirvana','nevermind')
make_album('green day','dookie')
make_album('counting crows','august and everything after')
make_album('weezer','pinkerton', '10')
