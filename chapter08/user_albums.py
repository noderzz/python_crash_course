'''
Start with your program from Exercise 8-7. Write a while loop that allows users to enter an albums artist and title. Once you have that information, call make_album() with the users input and print the dictionary thats created. Be sure to include a quit value in the while loop.
'''
def make_album(artist_name, album_title, song_number=None):
    album = {}
    album[artist_name.title()] = album_title.title()
    if song_number:
        album['Number of Songs:'] = int(song_number)
    print(album)

while True:
    print("\nPlease enter album information:")
    print('Enter "q" at anytime to quit.\n')

    artist_name = input("Enter artist name: ")
    if artist_name.lower() in ['q','quit']:
        break

    album_title = input("Enter album name: ")
    if album_title.lower() in ['q','quit']:
        break

    song_number = input("Enter number of songs in album (OPTIONAL): ")
    if song_number.lower() in ['q','quit']:
        break

    make_album(artist_name, album_title, song_number)