import requests 

class Bibleapi:
    base_url = 'https://bible-api.com/'

    def __init__(self):
        self._client = requests.session()

    def get_scripture(self,book=None, chapter=None, verse_from=None, verse_to=None, translation=None, verse_numbers=True):
        if book is None:
            book = 'Genesis'
        if chapter is None:
            chapter = 1
        if verse_from is None:
            verse_from = 1

        url = self.base_url + book + ' ' + str(chapter) + ':' + str(verse_from)
        
        if verse_to is not None:
            url += '-' + str(verse_to)

        # optional query params
        payload = {'translation': translation, 'verse_numbers': verse_numbers}

        return self._make_request(url, payload)

    def _make_request(self, url, payload):
        r = self._client.get(url, params=payload)
        return r.json()


if __name__ == "__main__":
    b = Bibleapi()
    print(b.get_scripture(book='John',translation='kjv'))