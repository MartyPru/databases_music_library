from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

# Retrieve all albums
album_repo = AlbumRepository(connection)
albums = album_repo.all()

# Print all albumss
for album in albums:
    print(album)

# Retrieve and print album with id '1'
matching_album = album_repo.find(1)
print(matching_album)
