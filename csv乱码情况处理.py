# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     csv乱码情况处理
   Description :
   Author :       bing
   date：          2021/7/8
-------------------------------------------------
   Change Activity:
                   2021/7/8:
-------------------------------------------------
"""
__author__ = 'bing'
# 今天扼要总结一个处理csv文件乱码问题，可能你有类似经历，用excel打开一个csv文件，中文全部显示乱码。然后，手动用notepad++打开，修改编码为utf-8并保存后，再用excel打开显示正常。

# 今天使用Python，很少代码就能将上面过程自动化。首先，导入3个模块：
import pandas as pd
import os
import chardet

def get_encoding(filename):
    """
    返回文件编码格式
    """
    with open(filename,'rb') as f:
        return chardet.detect(f.read())['encoding']

def to_utf8(filename):
    """
    保存为 to_utf-8
    """
    encoding = get_encoding(filename)
    ext = os.path.splitext(filename)
    if ext[1] =='.csv':
        if 'gb' in encoding or 'GB' in encoding:
            df = pd.read_csv(filename,engine='python',encoding='GBK')
        else:
            df = pd.read_csv(filename,engine='python',encoding='utf-8')
        df.to_excel(ext[0]+'.xlsx')
    elif ext[1]=='.xls' or ext[1] == '.xlsx':
        if 'gb' in encoding or 'GB' in encoding:
            df = pd.read_excel(filename,encoding='GBK')
        else:
            df = pd.read_excel(filename,encoding='utf-8')
        df.to_excel(filename)
    else:
        print('only support csv, xls, xlsx format')

def batch_to_utf8(path,ext_name='csv'):
    """
    path下，后缀为 ext_name的乱码文件，批量转化为可读文件
    """
    for file in os.listdir(path):
        if os.path.splitext(file)[1]=='.'+ext_name:
            to_utf8(os.path.join(path,file))

if __name__ == '__main__':
  batch_to_utf8('.') # 对当前目录下的所有csv文件保存为xlsx格式,utf-8编码的文件