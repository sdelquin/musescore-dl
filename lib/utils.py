import mimetypes
import tempfile
from http import HTTPStatus
from pathlib import Path

import logzero
import requests
from logzero import logger

import settings


def download_file(url: str) -> Path:
    logger.debug(f'🌐 Downloading {url}')
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        content_type = response.headers.get('Content-Type')
        extension = mimetypes.guess_extension(content_type)
        with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as temp_file:
            temp_file.write(response.content)
            return Path(temp_file.name)
    raise ValueError('something wrong')


def init_logger():
    logformat = (
        '%(asctime)s '
        '%(color)s'
        '[%(levelname)-8s] '
        '%(end_color)s '
        '%(message)s '
        '%(color)s'
        '(%(filename)s:%(lineno)d)'
        '%(end_color)s'
    )

    console_formatter = logzero.LogFormatter(fmt=logformat)
    file_formatter = logzero.LogFormatter(fmt=logformat, color=False)
    logzero.setup_default_logger(formatter=console_formatter)
    logzero.logfile(
        settings.LOGFILE,
        maxBytes=settings.LOGFILE_SIZE,
        backupCount=settings.LOGFILE_BACKUP_COUNT,
        formatter=file_formatter,
    )
    return logzero.logger
