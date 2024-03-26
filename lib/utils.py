import mimetypes
import tempfile
from http import HTTPStatus
from pathlib import Path

import requests


def download_file(url: str) -> Path:
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        content_type = response.headers.get('Content-Type')
        extension = mimetypes.guess_extension(content_type)
        with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as temp_file:
            temp_file.write(response.content)
            return Path(temp_file.name)
    raise ValueError('something wrong')
