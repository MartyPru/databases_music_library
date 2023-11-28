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

    def find(self, id):
        matching_result = self.connection.execute(f'SELECT * FROM albums WHERE id = {id};')[0]
        matching_object = Album(matching_result['id'], matching_result['title'], matching_result['release_year'], matching_result['artist_id'])
        return matching_object