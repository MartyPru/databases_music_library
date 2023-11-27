class Album():
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    


# alternative implementation
#         vvvvvvvv

# from dataclasses import dataclass

# @dataclass
# class Album:
#     id: int
#     title: str
#     release_year: int
#     artist_id: int

# instances of class will be equal if all attributes have same values
# when printed will look like:
    # Album(id=1, title='Voyage', release_year=2021, artist_id=2)
# more concise, but less flexible than regular classes

