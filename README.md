# musescore-dl

Download scores from musescore.com

## Setup

Requirements:

- [Python](https://www.python.org/) >= 3.10
- [Firefox](https://www.mozilla.org/firefox/)
- [geckodriver](https://github.com/mozilla/geckodriver)

And:

```console
pip install -r requirements.txt
```

## Usage

1. Navigate to [musescore.com](https://musescore.com) and locate your beloved score.
2. Copy that url.
3. `python main.py <beloved-url>`
4. After few seconds the pdf score will be saved to `scores/<title-of-the-score>.pdf`

Another interesting parameters:

- `-f`: Bring Selenium web browser to foreground.
- `-o`: Output path for the downloaded score.
- `-l`: Set loglevel.
