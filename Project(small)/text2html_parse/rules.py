# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rules
   Description :    处理文本块的规则类，所有类均为单例模式，在程序运行时，除了Rule每个类仅创建一个实例
   Author :       bing
   date：          2021/7/16
-------------------------------------------------
   Change Activity:
                   2021/7/16:
-------------------------------------------------
"""
# 设计模式：单例模式
__author__ = 'bing'
class Rule:
    """
    所有规则类的父类
    """
    def action(self, block, handler) -> bool:
        """

        :param block:
        :param handler:
        :return:
        加标记，以下三个方法执行打印HTML标签的功能
        """
        # 打印标签头
        handler.start(self.type)
        # 打印标签text里的内容
        handler.feed(block)
        # 打印标签尾
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    """
    标题规则
    一号标题规则，HTML 文件的一级标题规则（最大字号）<h1> 标签
    """
    type = 'heading'
    def condition(self, block) -> bool:
        """
        判断文本块是否符合规则。
        :param block:
        :return: bool
        """
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    """
    标题规则
    二号标题规则，次级标题规则，继承一号标题规则类 <h2> 标签
    """
    type = 'title'

    # 这是一个浮动值
    # 首次调用该类的实例，该值为 True
    # 之后调用该类的实例，该值为 False
    first = True

    def condition(self, block):
        """
        单例模式
        :param block:
        :return:
        """
        if not self.first:
            return False
        self.first = False
        return super().condition(block)

class ListItemRule(Rule):
    """
    列表规则类
    <li> 标签
    """
    type = 'listitem'
    def condition(self, block):
        """
        判断是否符合列表项
        :param block:
        :return:
        """
        # 行首是‘-’符号 符合列表项，markdown吗
        return block[0] == '-'

    def action(self, block, handler) -> bool:
        # 打印 < li > 标签头
        handler.start(self.type)
        # 打印 <li> 标签的 text 部分，注意去掉减号
        handler.feed(block[1:].strip())
        # 打印结尾
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
    """
    列表规则,<ul>标签
    """
    type = 'list'
    inside = False

    def condition(self, block):
        # 判断代码块是否符合规则这里返回 True
        # 在 action 方法中调用父类的同名方法再次判断
        return True

    def action(self, block, handler):
        # 如果 self.inside 为 False 且父类的 condition 方法返回值为 True
        # 第一次出现符合列表项规则的文本块时，满足这两个要求
        if not self.inside and super().condition(block):
            # 打印 <ul> 标签头
            handler.start(self.type)
            # 将 inside 属性值改为 True
            self.inside = True
        # 打印一堆连续 li 标签后，出现非列表项规则的文本块
        elif self.inside and not super().condition(block):
            # 打印 <ul> 标签尾
            handler.end(self.type)
            # 再次修改 inside 属性为 False
            self.inside = False
        # 该方法只用于在合适的条件下打印 <ul> 标签
        # 永远返回 False ，以调用其它规则实例继续处理
        return False


class ParagraphRule(Rule):
    """
    段落规则，<p> 标签
    """

    type = 'paragraph'  # 文本块类型

    def condition(self, block):
        # 不符合以上各类的判断规则的代码块一律按此规则处理
        return True


# 注意这个列表中实例的顺序不能随意改动，原因参见相应类中的注释说明
rule_list = [ListRule(), ListItemRule(), TitleRule(), HeadingRule(), ParagraphRule()]