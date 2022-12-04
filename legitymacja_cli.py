from typing import List
import typer
from create_full import main

app = typer.Typer(name='Generator Legitymacji Studenckiej')


@app.command('generate')
def generate(front_image: str,
             back_image: str,
             face_photo: str,
             stickers: List[str] = typer.Option([]),
             released: str = '',
             album: str = '',
             pesel: str = '',
             name: str = '',
             save: str = None):
    """Generates A Student's ID
    """
    main(front_image,
         back_image,
         face_photo,
         stickers,
         released,
         album,
         pesel,
         name,
         save)


if __name__ == '__main__':
    app()
