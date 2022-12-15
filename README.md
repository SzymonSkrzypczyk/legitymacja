# Generator Legitymacji Studenckiej 
## Główna część
### Generowanie Całej Legitymacji
```python
# potrzebne importowanie
from create_full import main
# tylko na potrzebe pokazu
from create_full import SAMPLE_FRONT, SAMPLE_BACK, SAMPLE_FACE, SAMPLE_STICKER
# wywolywanie
_im = main(
        SAMPLE_FRONT,
        SAMPLE_BACK,
        SAMPLE_FACE,
        9 * [SAMPLE_STICKER],
        'col1',
        'col2',
        'col3',
        'Sample Name'
    )
# pokazanie legitymacji
_im.show()
```
### Główne Moduły 
1. create_full.py 
2. front_page.py
3. back_page.py
### Dostępne Testy
1. test_full_page.py
2. test_front_page.py
3. test_back_page.py