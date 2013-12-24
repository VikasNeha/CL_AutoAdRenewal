from Utilities.myLogger import logger
from PageEvents.clEvents import CLEvents
import config
import subprocess
import sys


def renewAllAds():
    #========= LOOP THROUGH ALL ACCOUNTS =============#
    for currAccount in config.Accounts:
        # noinspection PyBroadException
        try:
            renewAdsForCurrentAccount(currAccount)
        except:
            logger.exception(sys.exc_info())


def renewAdsForCurrentAccount(currAccount):
    #========== Setup Firefox with proxy ============
    cle = CLEvents(currAccount)
    # noinspection PyBroadException
    try:
        subprocess.Popen(config.get_main_dir() + "/Resources/Proxy_Auth.exe " + currAccount.ProxyUsername + " " + currAccount.ProxyPassword)

        #======== OPEN CL LOGIN PAGE ========#
        cle.navigate(config.baseURL)
        #======== LOGIN TO CL ========#
        loginToCL(cle, currAccount)
        #======== LOGIN TO CL ========#
        cle.clickActive()

        cle.clickFirstRenewButton(currAccount.CL_Username)
        cle.renewAds(currAccount.CL_Username)

        # for ad in config.RenewedAds:
        #     print ad.Account, ad.AdLink

    except:
        logger.exception(sys.exc_info())
        if cle:
            cle.destroy()
        raise
    finally:
        if cle:
            cle.destroy()


def loginToCL(cle, currAccount):
    # noinspection PyBroadException
    try:
        cle.loginToCL(currAccount.CL_Username, currAccount.CL_Password)
    except:
        currAccount.result = False
        currAccount.resultComment = str(sys.exc_info())
        raise