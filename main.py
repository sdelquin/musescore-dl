from pathlib import Path

import logzero
import typer

from lib.manager import Manager
from lib.utils import init_logger

logger = init_logger()
app = typer.Typer(add_completion=False)


@app.command()
def run(
    url: str = typer.Argument(help='Score URL from musescore.com'),
    fg_browser: bool = typer.Option(
        False, '--fg-browser', '-f', help='Bring Selenium web browser to foreground.'
    ),
    score_output_path: Path = typer.Option(
        None,
        '--score-output-path',
        '-o',
        help='Path where the compiled score will be written on. If no value is given, the path will be the slugified title of the score.',
    ),
    loglevel: str = typer.Option(
        'DEBUG', '--loglevel', '-l', help='Log level (debug, info, error)'
    ),
):
    """🎵 Download scores from musescore.com"""
    logger.setLevel(getattr(logzero, loglevel.upper()))
    manager = Manager(url, not fg_browser)
    score = manager.get_score(score_output_path)
    score.save_file()


if __name__ == '__main__':
    try:
        app()
    except Exception as err:
        logger.exception(err)
