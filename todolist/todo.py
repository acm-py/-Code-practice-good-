# 来自代码之丑的练习
# target:实现一个todolist的代办清单，基于命令行工具
# 基于面向对象的语法
import argparse
import getpass
import hashlib
import json
import os
from typing import Dict


class ToDo():

    def __init__(self):
        pass

    
    def _read_config(self) -> str:
        """读取配置文件
        """
        # 拼接文件名
        file_name = os.path.join(os.path.expanduser('~'), '.todo-config')
        try:
            with open(file_name, 'r') as f:
                content = f.read()
                if content[-32:] != hashlib.md5(bytes(content[:-32], encoding='utf8')).hexdigest():
                    raise IOError("配置文件错误路径错误")
                
            return content[:-32]
        except (FileNotFoundError, IOError) as e:
            raise IOError("配置文件非法")
    
    def _parse_conifg(self) -> Dict:
        """解析配置文件
        """
        try:
            data = json.loads(self._read_config())
        except (IOError, json.decoder.JSONDecodeError):
            tmp = {
                "active_user": None,
                "users": {},
            }
            print("根据配置文件完成初始化")
            data = tmp
        return data

    def _write_config(self, data):
        """将用户自定义的写入配置文件
        """
        file_name = os.path.join(os.path.expanduser('~'), '.todo-config')
        try:
            with open(file_name, 'w') as f:
                f.write(data + hashlib.md5(bytes(data, encoding='utf8')).hexdigest())
        except PermissionError as e:
            raise IOError("你对%s文件没有操作权限" % file_name)
    
    def pack_write_config(self, data):
        try:
            self._write_config(json.dumps(data))
        except IOError as e:
            raise(e)
    
    def _read_data(self):
        """从文件中读取todolist事项 
        """
        filename = os.path.join(os.path.expanduser('~'), '.todo-data')
        try:
            with open(filename, 'r') as f:
                content = f.read()
                if content[-32:] != hashlib.md5(bytes(content[:-32], encoding='utf8')).hexdigest():
                    raise IOError("数据文件不合法")
            return content[:-32]
        except (FileNotFoundError, IOError) as e:
            raise IOError("数据文件不合法")

    def _parse_data(self):
        """解析用户数据文件
        """
        try:
            data = json.loads(self._read_data())
        except (IOError, json.decoder.JSONDecodeError):
            tmp = {

            }
            print("初始化数据文件")
            data = tmp
        return data
    
    def _write_data(self, data):
        """ 将用户数据写入数据文件中
        """
        file_name = os.path.join(os.path.expanduser('~'), '.todo-data')
        try:
            with open(file_name) as f:
                f.write(data + hashlib.md5(bytes(data, encoding='utf8')).hexdigest())
        except PermissionError as e:
            raise IOError("该%s文件权限不足" % file_name)
    
    def pack_write_data(self, data):
        try:
            self._write_data(data)
        except IOError as e:
            print(str(e))
    
    def _import_user_data(self):
        """导入用户数据
        """
        pass




