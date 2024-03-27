from prettyconf import config

PRIVACY_ACCEPT_XPATH = config(
    'PRIVACY_ACCEPT_XPATH', default='/html/body/div[1]/div/div/div/div[2]/div/button[2]'
)
SCORE_PAGES_SELECTOR = config('SCORE_PAGES_SELECTOR', default='div#jmuse-scroller-component>div')
SELENIUM_TIMEOUT = config('SELENIUM_TIMEOUT', default='10', cast=int)  # seconds
DEFAULT_SCORE_FILENAME = config('DEFAULT_SCORE_FILENAME', default='score.pdf')
