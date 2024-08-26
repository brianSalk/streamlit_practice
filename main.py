import os
import shutil
import subprocess
import time
from typing import List, Tuple

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



@st.cache_resource(show_spinner=False)
def get_python_version() -> str:
    try:
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        version = result.stdout.split()[1]
        return version
    except Exception as e:
        return str(e)


@st.cache_resource(show_spinner=False)
def get_chromium_version() -> str:
    try:
        result = subprocess.run(['chromium', '--version'], capture_output=True, text=True)
        version = result.stdout.split()[1]
        return version
    except Exception as e:
        return str(e)


@st.cache_resource(show_spinner=False)
def get_chromedriver_version() -> str:
    try:
        result = subprocess.run(['chromedriver', '--version'], capture_output=True, text=True)
        version = result.stdout.split()[1]
        return version
    except Exception as e:
        return str(e)




@st.cache_resource(show_spinner=False)
def get_chromedriver_path() -> str:
    return shutil.which('chromedriver')


@st.cache_resource(show_spinner=False)
def get_webdriver_options() -> Options:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument('--ignore-certificate-errors')
    return options




def get_webdriver_service() -> Service:
    service = Service(
        executable_path=get_chromedriver_path()
    )
    return service


def run_selenium():
    name = None
    html_content = None
    options = get_webdriver_options()
    service = get_webdriver_service()
    with webdriver.Chrome(options=options, service=service) as driver:
        url = "https://www.google.com/"
        try:
            driver.get(url)
            time.sleep(2)
            # Wait for the element to be rendered:
            button = WebDriverWait(driver=driver, timeout=5).until(lambda x: x.find_element(by=By.ID, value="gbqfbb"))
            text = button.get_attribute('value')
            st.write("writing: " + text)
        except Exception:
            write('selenium aint workin')

if __name__ == "__main__":
    run_selenium()
