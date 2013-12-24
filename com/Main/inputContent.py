from Utilities.myLogger import logger

from xlrd import open_workbook
from xlwt import easyxf, Formula, Workbook

import config

inputFile = config.inputXLSPath
outputFile = config.outputXLSPath


class Account:
    ProxyAddress = None
    ProxyPort = None
    ProxyUsername = None
    ProxyPassword = None
    CL_Username = None
    CL_Password = None
    result = None
    resultComment = None


class RenewedAd:
    Account = None
    AdLink = None


def readInput():
    book = open_workbook(config.inputXLSPath)
    sheet = book.sheet_by_name('Accounts')
    config.Accounts = []

    for row in range(sheet.nrows):
        if row == 0:
            continue
        currAccount = Account()
        for col in range(sheet.ncols):
            value = str(sheet.cell(row, col).value)
            if col == 0:
                currAccount.ProxyAddress = value
            elif col == 1:
                currAccount.ProxyPort = value
            elif col == 2:
                currAccount.ProxyUsername = value
            elif col == 3:
                currAccount.ProxyPassword = value
            elif col == 4:
                currAccount.CL_Username = value
            elif col == 5:
                currAccount.CL_Password = value
        config.Accounts.append(currAccount)


def writeResults():
    wb = Workbook()
    ws = wb.add_sheet(sheetname='Ads Results')
    headerStyle = easyxf('font: bold True')
    ws.write(0, 0, "Account", headerStyle)
    ws.write(0, 1, "Ad Link", headerStyle)

    hyperlinkStyle = easyxf('font: underline single, colour dark_blue')

    max_width_col0 = 0
    max_width_col1 = 0
    i = 1

    for currentAd in config.RenewedAds:
        ws.write(i, 0, currentAd.Account)
        if max_width_col0 < len(currentAd.Account):
            max_width_col0 = len(currentAd.Account)

        link = 'HYPERLINK("' + currentAd.AdLink + '";"' + currentAd.AdLink + '")'
        ws.write(i, 1, Formula(link), hyperlinkStyle)
        if max_width_col1 < len(currentAd.AdLink):
            max_width_col1 = len(currentAd.AdLink)

        ws.col(0).width = 256 * (max_width_col0+5)
        ws.col(1).width = 256 * (max_width_col1+5)

        wb.save(config.outputXLSPath)
        i += 1


