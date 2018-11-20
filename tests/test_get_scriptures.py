from pytest import fixture 

from bibleapi import Bibleapi 


@fixture
def response_keys():
    return ['reference', 'verses', 'text']


def test_get_scripture(response_keys):

    bible = Bibleapi()
    response = bible.get_scripture(book='John')
    assert isinstance(response, dict)
    assert set(response_keys).issubset(response.keys())