import sys
from Utilities.myLogger import logger
from Main import inputContent
from Main import RenewAllAds


def main():
    # noinspection PyBroadException
    try:
        readAllInput()
        RenewAllAds.renewAllAds()
    except:
        logger.exception(sys.exc_info())
    finally:
        inputContent.writeResults()
        return 1


def readAllInput():
    inputContent.readInput()