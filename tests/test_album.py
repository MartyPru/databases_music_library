from lib.album import *
"""
When initiated with title, release_year, artist_id
Has attributes for each of those values
"""
def test_initial_attributes():
    album = Album(1, 'Voyage', 2021, 2)
    assert album.title == 'Voyage'
    assert album.release_year == 2021
    assert album.artist_id == 2


"""
When two albums with same information are created
They are equal
"""
def test_equality():
    album_1 = Album(1, 'Voyage', 2021, 2)
    album_2 = Album(1, 'Voyage', 2021, 2)
    assert album_1 == album_2

"""
When formatted into a string
Shows easy-to-read string
"""
def test_str_formatting():
    album_1 = Album(1, 'Voyage', 2021, 2)
    assert str(album_1) == 'Album(Voyage, 2021, 2)'