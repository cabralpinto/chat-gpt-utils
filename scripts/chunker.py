import sys
from functools import partialmethod
from pathlib import Path

import keyboard
from more_itertools import sliced
from pyperclip import copy
from tqdm import tqdm

tqdm.__init__ = partialmethod(
    tqdm.__init__,
    leave=False,
    bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"
)
for path in tqdm(list(Path(sys.argv[1]).iterdir())):
    text = path.read_text()
    for index, chunk in enumerate(tqdm(list(sliced(text, 3000)))):
        prefix = "Read" if index == 0 else "Continue reading"
        copy(f'{prefix} "{path.name}". Answer only with "Ok".\n\n"{chunk}"')
        keyboard.wait('enter')
