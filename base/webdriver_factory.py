import os
from selenium import webdriver

from utilities import global_config_reader


class WebDriverSetup:
    browser_env_details = None
    path_details = None
    driver = None

    def __init__(self):
        self.browser_env_details = global_config_reader.getglobaldata("browser_data")
        self.path_details = global_config_reader.getglobaldata("path_data")

    def start_browser(self):
        if self.browser_env_details["browser"].upper() == "CHROME":
            from selenium.webdriver.chrome.service import Service
            s = Service(os.pardir + self.path_details["browser_driver_path"] + "\\chromedriver.exe")
            opt = webdriver.ChromeOptions()
            # opt.add_argument("--headless")  # To launch the browser in headless mode
            opt.add_argument('--disable-infobars')
            opt.add_argument('--no-sandbox')
            opt.add_argument('--disable-extensions')
            opt.add_argument('--disable-dev-shm-usage')
            opt.add_experimental_option("detach", True) # This will keep the browser open after the test run
            self.driver = webdriver.Chrome(service=s, options=opt)

        elif self.browser_env_details["browser"].upper() == "FIREFOX":
            from selenium.webdriver.firefox.service import Service
            s = Service(os.pardir + self.path_details["browser_driver_path"] + "\\geckodriver.exe")
            self.driver = webdriver.Firefox(service=s)
        elif self.browser_env_details["browser"].upper() == "EDGE":
            from selenium.webdriver.edge.service import Service
            s = Service(os.pardir + self.path_details["browser_driver_path"] + "\\msedgedriver.exe")
            self.driver = webdriver.Edge(service=s)
        else:
            print("Invalid Browser")

    def set_browser_settings(self):
        self.driver.implicitly_wait(self.browser_env_details["implicit_wait_time"])
        self.driver.maximize_window()

    def launch_application(self):
        self.start_browser()
        self.set_browser_settings()
        print(self.browser_env_details["browser"] + " browser started successfully!!!")
        self.driver.get(self.browser_env_details["app_url"])
        print("URL '" + self.browser_env_details["app_url"] + "' launched successfully")
        return self.driver
