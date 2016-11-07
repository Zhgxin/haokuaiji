# -*- coding:utf-8 -*-
import urllib2,hashlib,json,unittest

class download():
    def __init__(self):
        self.Cookie = 'JSESSIONID=9B6DCD7A3DA062B2232CF07CC49D2A08; tipGuide_tip_wechart=tipGuide_tip_wechart; guide_4=2.0.3; guide_3=2.0.3; hkj-live=0.0.16; pageGuide_FapiaoList=yes; CLI_BD_ID=e94b4dac-91c4-39c9-8d89-928ad231b71e; CLI_LONG_BD_ID=fb53bae3-f151-c3d1-e5a7-9f8245bb8a6d; Hm_lvt_5b937da9ec91718e91eecfb2d9a3086e=1478486746,1478486798,1478495982,1478503724; Hm_lpvt_5b937da9ec91718e91eecfb2d9a3086e=1478503724; __VCAP_ID__=994897af32c0055838863e10dcd1a66262014a3ba58fa906842dea0d3d1d6111'
    #读取页面
    def request(self,method,url,data):
        try:
            request = urllib2.Request(url)
            request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36')
            request.add_header('Cookie',self.Cookie)
            request.add_header("Content-Type",'application/json')
            request.get_method = lambda:method
            response = urllib2.urlopen(request,data).read()
            return response
        except urllib2.URLError,e:
            return e.reason


if __name__ == '__main__':
    url = 'http://u5ag81hrz7cs.chanapp.com/chanjet/accounting/restlet/v2/web/invoice/InvoiceList?ACCOUNTBOOK=100010&period=201611&invoiceType=1&inInvoiceFilter=0&_dc=1477983680508'
    test = download()
    reslut = test.request('GET',url,data=None)
    print reslut
