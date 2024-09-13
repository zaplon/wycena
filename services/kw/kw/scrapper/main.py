import json
import logging
from tempfile import mkdtemp

from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def initialise_driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
    chrome_options.add_argument(f"--data-path={mkdtemp()}")
    chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    chrome_options.add_argument("--remote-debugging-pipe")
    chrome_options.add_argument("--verbose")
    chrome_options.add_argument("--log-path=/tmp")
    chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

    service = Service(
        executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver"
    )

    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )

    return driver


class LambdaInput(BaseModel):
    kod_wydzialu: str
    numer_ksiegi: str
    cyfra_kontrolna: int


def lambda_handler(event, context):
    lambda_input = LambdaInput(**context)
    driver = initialise_driver()
    driver.get("https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW?komunikaty=true&kontakt=true&okienkoSerwisowe=false")
    driver.find_element("kodWydzialuInput").send_keys(lambda_input.kod_wydzialu)
    driver.find_element("numerKsiegiWieczystej").send_keys(lambda_input.numer_ksiegi)
    driver.find_element("cyfraKontrolna").send_keys(lambda_input.cyfra_kontrolna)
    driver.find_element("wyszukaj").click()

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

    return response
