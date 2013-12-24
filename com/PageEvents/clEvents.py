from selenium.common.exceptions import TimeoutException
from webpageEvents import WebpageEvents
from Utilities.constants import IDMODE
from Main.inputContent import RenewedAd
import sys
import config


class CLEvents(WebpageEvents):

    filterActiveURL = None

    def __init__(self, currentProxy):
        super(CLEvents, self).__init__(currentProxy)

    def destroy(self):
        super(CLEvents, self).destroy()

    def loginToCL(self, CL_Username, CL_Password):
        self.enterText(IDMODE.ID, 'inputEmailHandle', CL_Username)
        self.enterText(IDMODE.ID, 'inputPassword', CL_Password)
        self.clickButton('Log In')
        self.assertLoginSuccessful()

    def assertLoginSuccessful(self):
        try:
            self.assertLinkPresent('log out')
        except:
            raise Exception('Login Unsuccessful' + str(sys.exc_info()))

    def clickActive(self):
        legend = self.findElement(IDMODE.ID, 'searchlegend')
        selected = legend.find_element_by_tag_name('b')
        if selected.text == 'active':
            return
        else:
            activeLink = legend.find_element_by_link_text('active')
            activeLink.click()

    def renewAds(self, currAccount):
        while True:
            if not self.clickFirstRenewButton(currAccount):
                break

    def clickFirstRenewButton(self, currAccount):
        renewButtons = self.findRenewButtons()
        if renewButtons:
            if len(renewButtons) != 0:
                renewButtons[0].click()
                try:
                    manageStatus = self.findElement(IDMODE.CLASS, 'managestatus')
                    adLink = manageStatus.find_element_by_tag_name('a')
                    currentAd = RenewedAd()
                    currentAd.Account = currAccount
                    currentAd.AdLink = adLink.get_attribute('href')
                    config.RenewedAds.append(currentAd)
                except TimeoutException:
                    pass
                finally:
                    self.navigate(self.filterActiveURL)
                    return True
            else:
                return False
        else:
            return False

    def findRenewButtons(self):
        self.filterActiveURL = self.driver.current_url
        try:
            adsBox = self.findElement(IDMODE.CLASS, 'accthp_postings')
            renewButtons = adsBox.find_elements_by_xpath("//input[@class='managebtn' and @value='renew']")
            return renewButtons
        except TimeoutException:
            return None