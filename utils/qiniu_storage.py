# -*- coding: utf-8 -*-

import qiniu.config
import logging

from qiniu import Auth, put_data, etag, urlsafe_base64_encode

#需要填写你的 Access Key 和 Secret Key
access_key = 'TwSFFrCLwAUQyvATlCWIA67bcTUdWFsFLtOfO-uL'
secret_key = 'RqLgeqlsUrS2gV52TbhhTtF5uuRvSqVSjDbu3n3Y'

def storage(file_data):
    try:
        #构建鉴权对象
        q = Auth(access_key, secret_key)

        #要上传的空间
        bucket_name = 'ihome'

        token = q.upload_token(bucket_name)

        ret, info = put_data(token, None, file_data)
    except Exception as e:
        logging.error(e)
        raise e
    if 200 == info.status_code:
        return ret["key"]
    else:
        raise Exception("上传失败")


if __name__ == "__main__":
    file_name = raw_input("input file name")
    with open(file_name, "rb") as file:
        file_data = file.read()
        storage(file_data)