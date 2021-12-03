import io
from mimetypes import guess_extension
from pathlib import Path
from typing import Optional

import requests as requests

COOKIES = {
    "session": "53616c7465645f5fc92764e2e17636f5891810c8d0ccce5c710082fa9a0feaabdaf5bbab72e1adcd371867d5fc597ab9"
}
BASE_PATH = Path(__file__).parents[1]


def get_input(day_nr: int, ext: str = ".txt", target_dir: Optional[Path] = None) -> Path:
    """
    Retrieves the input from the webpage.

    :param daynr: number of the day to retrieve inputs for.
    :param target_dir: path to store the inputs in.
    :return: file
    """
    uri = f'https://adventofcode.com/2021/day/{day_nr}/input'

    if not ext.startswith("."):
        ext = f".{ext}"
    file_name = f"input{day_nr}{ext}"

    if target_dir:
        file_path = target_dir / file_name
    else:
        file_path = BASE_PATH / f"day{day_nr}" / file_name

    if not file_path.exists():
        r = requests.get(url=uri, cookies=COOKIES)
        r.raise_for_status()
        with file_path.open("wb") as fd:
            fd.write(r.content)
            fd.flush()

    return file_path


if __name__ == "__main__":
    SystemExit(get_input(2))
