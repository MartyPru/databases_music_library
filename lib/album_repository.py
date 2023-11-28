from lib.album import * 

class AlbumRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM albums;')
        albums = []
        for row in rows:
            album = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(album)
        return albums

    def find(self, artist_id):
        matching_result = self.connection.execute('SELECT * FROM albums WHERE id = %s;', [artist_id])[0]
        matching_object = Album(matching_result['id'], matching_result['title'], matching_result['release_year'], matching_result['artist_id'])
        return matching_object
    
    def create(self, album):
        self.connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)",
                                [album.title, album.release_year, album.artist_id])
        
    def delete(self, album_id):
        self.connection.execute("DELETE FROM albums WHERE id = %s", [album_id])