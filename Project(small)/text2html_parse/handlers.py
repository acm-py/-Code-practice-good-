# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     handlers
   Description :    HTML 文本处理类，用于打印各种HTML标签
   Author :       bing
   date：          2021/7/16
-------------------------------------------------
   Change Activity:
                   2021/7/16:
-------------------------------------------------
"""
__author__ = 'bing'
# 采用了反射的设计思想
# Python 内置方法 gerattr 用于返回一个对象的属性值。
# 举例来说，getattr(x, 'foo', None) 就相当于是 x.foo，而如果没有这个属性值 foo，则返回我们设定的默认值 None。
class Handler:
    """
    处理程序父类
    """
    def callback(self, prefix, name, *args):
        """
        :param prefix:
        :param name:
        :param args:
        :return:
        """
        # 获取处理方法，getattr接受三个参数
        # 1、 Python对象
        # 2、 属性字符串
        # 3、 默认值
        # 返回值为Python对象的属性值，如果没有此属性值，返回第三个参数
        # 反射机制
        method = getattr(self, prefix + name, None)
        # 调用处理方法，将其返回值作为当前函数的返回值
        if callable(method):
            return method(*args)

    def start(self, name):
        """

        :param name:
        :return:
        """
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    # 参数 name 的值为过滤器名字，是字符串
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                result = match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    """
    HTML 处理程序，给文本块加相应的 HTML 标记
    """
    # 以下各个方法分别在符合条件时被调用，打印标签或标签的 text 值
    def start_document(self):
        print('<html><head><title>ShiYanLou</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p style="color: #444;">')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2 style="color: #68BE5D;">')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul style="color: #363736;">')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1 style="color: #1ABC9C;">')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return ('<em>%s</em>' % match.group(1))

    def sub_url(self, match):
        s = ('<a target="_blank" style="text-decoration: none;'
             'color: #BC1A4B;" href="{}">{}</a>')
        return s.format(match.group(1), match.group(1))

    def sub_mail(self, match):
        s = ('<a style="text-decoration: none;color: #BC1A4B;" '
             'href="mailto:{}">{}</a>')
        return s.format(match.group(1), match.group(1))

    def feed(self, data):
        print(data)