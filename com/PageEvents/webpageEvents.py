from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support import ui
from selenium.common.exceptions import *
import config
from Utilities.constants import IDMODE
import logging

module_logger = logging.getLogger('main.webpageEvents')


# noinspection PyBroadException
class WebpageEvents(object):

    def __init__(self, currentProxy):
        ProxyIP = currentProxy.ProxyAddress + ":" + currentProxy.ProxyPort
        proxySettings = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': ProxyIP,
            'ftpProxy': ProxyIP,
            'sslProxy': ProxyIP
        })
        if ProxyIP.strip() == ':':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Firefox(proxy=proxySettings)

    def destroy(self):
        self.driver.quit()

    def navigate(self, url):
        self.driver.get(url)

    def findElement(self, idMode, idValue):
        try:
            webElement = None
            self.waitUntilElementIsPresent(idMode, idValue)
            if idMode == IDMODE.ID:
                webElement = self.driver.find_element_by_id(idValue)
            elif idMode == IDMODE.CLASS:
                webElement = self.driver.find_element_by_class_name(idValue)
            elif idMode == IDMODE.PARTIAL_LINK_TEXT:
                webElement = self.driver.find_element_by_partial_link_text(idValue)
            elif idMode == IDMODE.LINK_TEXT:
                webElement = self.driver.find_element_by_link_text(idValue)
            return webElement
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            raise

    def waitUntilElementIsPresent(self, idMode, idValue):
        try:
            wait = ui.WebDriverWait(self.driver, config.webElementTimeOut)
            if idMode == IDMODE.ID:
                wait.until(lambda driver: self.driver.find_element_by_id(idValue))
            elif idMode == IDMODE.CLASS:
                wait.until(lambda driver: self.driver.find_element_by_class_name(idValue))
            elif idMode == IDMODE.PARTIAL_LINK_TEXT:
                wait.until(lambda driver: self.driver.find_element_by_partial_link_text(idValue))
            elif idMode == IDMODE.LINK_TEXT:
                wait.until(lambda driver: self.driver.find_element_by_link_text(idValue))
        except:
            raise

    def getElementText(self, idMode, idValue):
        try:
            return self.findElement(idMode, idValue).text
        except:
            raise

    def clickPartialLink(self, idValue):
        try:
            self.findElement(IDMODE.PARTIAL_LINK_TEXT, idValue).click()
        except:
            raise

    def takeScreenshot(self, fileName):
        try:
            self.driver.get_screenshot_as_file(fileName)
        except:
            return

    def enterText(self, idMode, idValue, text):
        textbox = self.findElement(idMode, idValue)
        textbox.clear()
        textbox.send_keys(text)

    def clickButton(self, buttonText):
        allButtons = self.driver.find_elements_by_tag_name('button')
        buttonFound = False
        for currButton in allButtons:
            if currButton.text == buttonText:
                currButton.click()
                buttonFound = True
                break
        if not buttonFound:
            raise Exception('Problem in finding and clicking button: ' + buttonText)

    def assertLinkPresent(self, linkText):
        try:
            self.waitUntilElementIsPresent(IDMODE.LINK_TEXT, linkText)
        except:
            raise