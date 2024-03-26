import fpdf

from . import utils


class Score:
    def __init__(self, output_path: str):
        self.output_path = output_path
        self.pdf = fpdf.FPDF(unit='pt')

    def add_page(self, page_url: str):
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
        self.pdf.output(self.output_path)
