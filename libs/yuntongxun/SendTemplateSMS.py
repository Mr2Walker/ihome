#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import ConfigParser
import logging

#���ʺ�
accountSid= '8a216da85f008800015f16905db60a02';

#���ʺ�Token
accountToken= '3b6c5dd5f46a4a699b16dd33fb3416ed';

#Ӧ��Id
appId='8a216da85f008800015f16905f250a09';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com';

#����˿� 
serverPort='8883';

#REST�汾��
softVersion='2013-12-26';

class CCP(object):

    def __init__(self):
        self.rest = REST(serverIP, serverPort, softVersion)
        self.rest.setAccount(accountSid, accountToken)
        self.rest.setAppId(appId)

    @staticmethod
    def instance():
        if not hasattr(CCP, "_instance"):
            CCP._instance = CCP()
        return CCP._instance

    def sendTemplateSMS(self, to, datas, tempId):
        try:
            result = self.rest.sendTemplateSMS(to, datas, tempId)
        except Exception as e:
            logging.error(e)
            raise e

        if result.get("statusCode") == "000000":
            return True
        else:
            return False

ccp = CCP.instance()

if __name__ == "__main__":
    ccp = CCP.instance()
    ccp.sendTemplateSMS("13790766711", ["1234", 5], 1)