from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent
PROJECT_NAME = PROJECT_DIR.name

PRIVACY_ACCEPT_XPATH = config(
    'PRIVACY_ACCEPT_XPATH', default='/html/body/div[1]/div/div/div/div[2]/div/button[2]'
)
SCORE_PAGES_SELECTOR = config('SCORE_PAGES_SELECTOR', default='div#jmuse-scroller-component>div')
SELENIUM_TIMEOUT = config('SELENIUM_TIMEOUT', default='10', cast=int)  # seconds
DEFAULT_SCORE_FILENAME = config('DEFAULT_SCORE_FILENAME', default='score.pdf')

LOGFILE = config('LOGFILE', default=PROJECT_DIR / (PROJECT_NAME + '.log'), cast=Path)
LOGFILE_SIZE = config('LOGFILE_SIZE', cast=float, default=1e6)
LOGFILE_BACKUP_COUNT = config('LOGFILE_BACKUP_COUNT', cast=int, default=3)

SCORE_OUTPUT_DIR = config('SCORE_OUTPUT_DIR', default=PROJECT_DIR / 'scores', cast=Path)
