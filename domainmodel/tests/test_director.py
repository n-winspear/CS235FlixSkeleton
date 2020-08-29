import pytest
from CS235FlixSkeleton.domainmodel.director import Director


@pytest.fixture
def director():
    return Director("Taika Waititi", '+6421856498', 45, 't.waititi@gmail.com', 1, 'https://www.imdb.com/name/nm0169806/')


def test_init():
    director = Director("")
    assert director.director_full_name == None
    director = Director(23)
    assert director.director_full_name == None
    director = Director("Taika Waititi")
    assert director.director_full_name == "Taika Waititi"
    assert director.director_first_name == "Taika"
    assert director.director_last_name == "Waititi"
    assert director.director_age == None
    assert director.director_IMDB == None
    assert director.director_gender == None
    assert director.director_email_address == None
    assert director.director_phone_number == None


def test_director_name(director):
    assert director.director_full_name == "Taika Waititi"
    assert director.director_first_name == "Taika"
    assert director.director_last_name == "Waititi"
    director.director_full_name = "Nathan Winspear"
    assert director.director_full_name == "Nathan Winspear"
    assert director.director_first_name == "Nathan"
    assert director.director_last_name == "Winspear"


def test_phone_number(director):
    assert director.director_phone_number == '+6421856498'
    director.director_phone_number = '+6421636362'
    assert director.director_phone_number == '+6421636362'


def test_age(director):
    assert director.director_age == 45
    director.director_age = 65
    assert director.director_age == 65


def test_email_address(director):
    assert director.director_email_address == 't.waititi@gmail.com'
    director.director_email_address = 'n.winspear1@gmail.com'
    assert director.director_email_address == 'n.winspear1@gmail.com'


def test_gender(director):
    assert director.director_gender == 1
    director.director_gender = 3
    assert director.director_gender == 3


def test_IMDB(director):
    assert director.director_IMDB == 'https://www.imdb.com/name/nm0169806/'
    director.director_IMDB = 'https://google.com'
    assert director.director_IMDB == 'https://google.com'


def test_eq(director):
    director2 = Director('Taika Waititi')
    assert director == director2


def test_lt(director):
    director2 = Director('Zinadine Zidane')
    assert director.director_full_name < director2.director_full_name


def test_repr(director):
    assert repr(director) == "<Director Taika Waititi>"
