# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     关于list
   Description :
   Author :       bing
   date：          2021/7/8
-------------------------------------------------
   Change Activity:
                   2021/7/8:
-------------------------------------------------
"""
__author__ = 'bing'
# 往列表中添加元素
# extend 方法实现批量添加元素时未创建一个新的列表，而是直接添加在原列表中，这被称为in-place，就地。
# 而b=a+list对象实际是创建一个新的列表对象，所以不是就地批量添加元素。

# 但是，a+=一个列表对象，+=操作符则就会自动调用extend方法进行合并运算。
# 大家注意这些微妙的区别，不同场景选用不同的API，以此高效节省内存。

# 往列表中删除元素
# remove() 直接删除元素，若有重复，只删除第一个
# pop方法若不带参数默认删除列表最后一个元素；若带参数则删除此参数代表的索引处的元素：
# del与pop相似，删除指定索引处的元素

# 其他常用api
# `clear`,`index`,`count`,`sort`,`reverse`,`copy`
# clear 清空列表内的远古三
# index 查找列表中某个元素的索引
# count 用于统计某个元素出现的次数
# sort 用于元素排序，其中参数key定制排序规则。
a = [(3,1), (4,1), (1,3), (5,4), (9,-10)]
a.sort(key = lambda x:x[1])
# >>> a
# >>> [(9, -10), (3, 1), (4, 1), (1, 3), (5, 4)]
# reverse 反转列表

# 列表包含自身
a = [1, 3, 5]
a[1] = a
# >>> a
# >>> [1, [...], 5]

# 插入元素性能分析
# 插入元素的时间复杂度为O(n)
# 以下为cpython 源码关于列表插入的操作
static int
ins1(PyListObject *self, Py_ssize_t where, PyObject *v)
{
    assert((size_t)n + 1 < PY_SSIZE_T_MAX);
    if (list_resize(self, n+1) < 0)
        return -1;

    if (where < 0) {
        where += n;
        if (where < 0)
            where = 0;
    }
    if (where > n)
        where = n;
    items = self->ob_item;
    //依次移动插入位置后的所有元素
    // O(n) 时间复杂度
    for (i = n; --i >= where; )
        items[i+1] = items[i];
    Py_INCREF(v);
    items[where] = v;
    return 0;
}
# 列表可变性
# 可变的对象是不可hash的，不可hash的对象不能被映射，因此不能被用作字典的key
# 但是，有时我们确实需要列表对象作为键，这怎么办？
# 可以将列表转化为元祖！，元祖是可哈希的，所以能作为字典的键。

# 在使用for循环遍历删除对应元素的时，会有个bug
d = [2, 1, 3, 1, 1, 3]# 如果要删除的元素是1
# 因为有两个1相邻，删除完一个之后，for循环会继续向后走，但是后面的（未删除的1）就取代了已删除1的位置，
# 就这样，跳过了一个1
#