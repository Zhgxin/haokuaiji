# -*- coding:utf-8 -*-
import urllib2,hashlib,json,unittest
from html_Download import download

class control():
    def __init__(self):
        self.request = download()
        self.beasUrl ='http://u5ag81hrz7cs.chanapp.com/'

    #获取进项发票数量
    def getaccountbookId(self):
        beasUrl = self.beasUrl
        accountbookDict = []
        #url = beasUrl + 'chanjet/accounting/restlet/v2/web/accountbook/FindAll'
        url = 'http://u5ag81hrz7cs.chanapp.com/chanjet/accounting/restlet/v2/web/invoice/InvoiceList?ACCOUNTBOOK=100010&period=201611&invoiceType=1&inInvoiceFilter=0&_dc=1477983680508'
        #return url
        reslut = json.loads(self.request.request("GET", url, data=None))
        if "resultObj" in str(reslut):
            num = reslut["resultObj"]["data"]["allvoucherRowresultList"]
            return len(num)
        else:
            return None

    def creatInvoice(self):
        creatUrl = 'http://u5ag81hrz7cs.chanapp.com/chanjet/accounting/restlet/v2/web/invoice/SaveInvoice?ACCOUNTBOOK=100010'
        Date = {"invoice":'{"invoiceNo":"11713","invoiceDate":"2016-10-31T16:00:00.000Z","invoiceType":1,"type":"001","taxCode":"11732","moneyAmounts":100,"taxAmounts":1,"childBORowSets":{"InvoiceDetail":[]},"provider":"11722"}'}
        creatDate = json.dumps(Date)
        creatRresult = self.request.request("POST",creatUrl,creatDate)
        return  creatRresult



if __name__ == '__main__':
    test = control()
    print test.creatInvoice()