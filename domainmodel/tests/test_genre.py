import pytest
from CS235FlixSkeleton.domainmodel.genre import Genre


@pytest.fixture
def genre():
    return Genre('Comedy')


def test_init():
    genre = Genre("")
    assert genre.genre_name == None
    genre = Genre(23)
    assert genre.genre_name == None
    genre = Genre("Comedy")
    assert genre.genre_name == 'Comedy'


def test_genre_name(genre):
    genre.genre_name == 'Comedy'
    genre.genre_name = 'Horror'
    genre.genre_name == 'Horror'


def test_eq(genre):
    genre2 = Genre('Comedy')
    assert genre == genre2


def test_lt(genre):
    genre2 = Genre('Horror')
    assert genre.genre_name < genre2.genre_name


def test_repr(genre):
    assert repr(genre) == "<Genre Comedy>"
