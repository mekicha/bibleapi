## About 
A tiny Python wrapper for [bible-api.com](https://bible-api.com), an api for grabbing bible verses and passages.

---

## Usage
```python
from bibleapi import Bibleapi

bible = Bibleapi()
scripture = bible.get_scripture(book='John', chapter=3, verse_from=16, 
    verse_to=18, translation='kjv',verse_numbers=False)

print(scripture)
```

Response:
```js
    {'reference': 'John 3:16-18', 'verses': [{'book_id': 'JHN', 'book_name': 'John', 'chapter': 3, 'verse': 16, 'text': 'For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.\n'}, {'book_id': 'JHN', 'book_name': 'John', 'chapter': 3, 'verse': 17, 'text': 'For God sent not his Son into the world to condemn the world; but that the world through him might be saved.'}, {'book_id': 'JHN', 'book_name': 'John', 'chapter': 3, 'verse': 18, 'text': 'He that believeth on him is not condemned: but he that believeth not is condemned already, because he hath not believed in the name of the only begotten Son of God.\n'}], 
    'text': 'For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.\nFor God sent not his Son into the world to condemn the world; but that the world through him might be saved. He that believeth on him is not condemned: but he that believeth not is condemned already, because he hath not believed in the name of the only begotten Son of God.\n', 'translation_id': 'kjv', 'translation_name': 'King James Version', 'translation_note': 'Public Domain'}
```
---

## Defaults
The api uses the following defaults in the case of omission.

| Param| Default value| Comments|
|--------|:------:|-------|
|book | Genesis | Book of the bible to return 
|chapter| 1 | Chapter to return
| verse_from | 1| The verse to start from
|verse_to | None | The verse to end
|translation| kjv | Translation to return.
|verse_numbers| `True`| Return verse_numbers in text if `True`.


## Available Translations
|Language|Name|Identifier|
|----|------|-------|
|Cherokee|	Cherokee New Testament|	cherokee
|English|	King James Version|	kjv
|English|	World English Bible	web| (default)
|Latin|	Clementine Latin Vulgate|	clementine
|Portuguese	|João Ferreira de Almeida|	almeida
|Romanian	|Romanian Corrected Cornilescu Version|	rccv