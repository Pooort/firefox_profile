import os
import re

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


PROJECTPATH = os.path.dirname(os.path.realpath(__file__))

geckodriver_path = os.path.join(PROJECTPATH, 'geckodriver')
profile_path = os.path.join(PROJECTPATH, 'clean_profile')

capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities["moz:firefoxOptions"] = {
    "args": ["--profile", profile_path]
}


def get_marionette_port(profile_path):
    prefs_path = os.path.join(profile_path, 'prefs.js')
    with open(prefs_path) as f:
        marionette_port = re.search('"marionette.port", (\d+?)\)', f.read()).group(1)
    return marionette_port

#url = 'https://tesera.ru'

url = 'YOUR SITE HERE'

marionette_port = get_marionette_port(profile_path)

driver = webdriver.Firefox(executable_path=geckodriver_path, capabilities=capabilities, service_args=['--marionette-port', marionette_port])
driver.get(url)
input('Waiting for login...')
driver.quit()