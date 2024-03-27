import re

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from slugify import slugify

import settings

from .score import Score


class Handler:
    def __init__(self, score_url: str, headless: bool = True):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        self.actions = ActionChains(self.driver)
        self.driver.get(score_url)
        self._accept_privacy()

    def _accept_privacy(self) -> None:
        url = settings.PRIVACY_ACCEPT_XPATH
        timeout = settings.SELENIUM_TIMEOUT
        privacy_agree_button = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, url))
        )
        privacy_agree_button.click()

    def _get_score_title(self) -> str:
        title = self.driver.find_element(By.TAG_NAME, 'title')
        if title_text := title.get_attribute('innerText'):
            if m := re.search(r'(^.*) Sheet', title_text.strip()):
                return m.group(1)
        return ''

    def get_score(self, score_path=None) -> Score:
        score_path = (
            score_path
            or f'{slugify(self._get_score_title())}.pdf'
            or settings.DEFAULT_SCORE_FILENAME
        )
        score = Score(score_path)
        css_selector = settings.SCORE_PAGES_SELECTOR
        for div in self.driver.find_elements(By.CSS_SELECTOR, css_selector):
            if div.get_attribute('class'):
                self.driver.execute_script('arguments[0].scrollIntoView();', div)
                self.actions.move_to_element(div).perform()
                img = div.find_element(By.TAG_NAME, 'img')
                if score_page_url := img.get_attribute('src'):
                    score.add_page(score_page_url)
            else:
                break
        return score

    def __del__(self):
        self.driver.quit()
