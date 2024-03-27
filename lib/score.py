from pathlib import Path

import fpdf
from logzero import logger

from . import utils


class Score:
    def __init__(self, output_path: str):
        logger.info('🧱 Building Score')
        self.output_path = Path(output_path)
        self.pdf = fpdf.FPDF(unit='pt')

    def add_page(self, page_url: str):
        logger.info('➕ Adding page to final score')
        page_path = utils.download_file(page_url)
        match page_path.suffix:
            case '.svg':
                svg = fpdf.svg.SVGObject.from_file(page_path)
                self.pdf.add_page(format=(svg.width, svg.height))
                svg.draw_to_page(self.pdf)
            case '.png':
                self.pdf.add_page()
                self.pdf.image(page_path, w=self.pdf.epw, h=self.pdf.eph)

    def save_file(self):
        logger.info(f'💾 Saving score to {self.output_path}')
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.pdf.output(self.output_path)
