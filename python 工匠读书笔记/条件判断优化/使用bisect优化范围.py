def rank(score):
    rating_num = float(score)
    if rating_num >= 8.5:
        return "S"
    elif rating_num >=8:
        return "A"
    elif rating_num >= 7:
        return "B"
    elif rating_num >= 6:
        return "C"
    else:
        return "D"


# 可以像下面按照这样优化
# 我们可以发现，存在明显有序的分界点.
breakpoints = (6, 7, 8, 8.5)
# 接下来要做的就是通过rating 确定他在breakpoint中的位置

# 而这个时候就可以想到二分查找了，二分查找可以查找到最接近的最左边位置，也可以是最接近的最右边的位置。
import bisect
# note: must sorted
# 用来做二分查找的容器必须是已经排好序的
breakpoints = [10, 20, 30]

bisect.bisect(breakpoints, 1) # 0
bisect.bisect(breakpoints, 35) # 3
import random

# 所以上面的函数可以改进为
def rank2(score):
    rating_num = float(score)
    breakpoints = (6, 7, 8, 8.5)
    grade = ('D', 'C', 'B', 'A', 'S')
    index = bisect.bisect(breakpoints, rating_num)
    return grade[index]


def get_sorted_movies(movies, sorting_type):
    if sorting_type == 'name':
        sorted_movies = sorted(movies, key=lambda movie: movie.name.lower())    
    elif sorting_type == 'rating':        
        sorted_movies = sorted(            
            movies, key=lambda movie: float(movie.rating), reverse=True        
        )    
    elif sorting_type == 'year':        
        sorted_movies = sorted(     
            movies, key=lambda movie: movie.year, reverse=True
        )    
    elif sorting_type == 'random':
        sorted_movies = sorted(movies, key=lambda movie: random.random())
    else:        
        raise RuntimeError(f'Unknown sorting type: {sorting_type}')    
    return sorted_movies

# 上面这段代码同样可以修改成下面这种
sorting_algos = {    
    # sorting_type: (key_func, reverse)    
    'name': (lambda movie: movie.name.lower(), False),
    'rating': (lambda movie: float(movie.rating), True),   
    'year': (lambda movie: movie.year, True),    
    'random': (lambda movie: random.random(), False),
}


def get_sorted_movies(movies, sorting_type):    
    """对电影列表进行排序并返回    
    :param movies: Movie 对象列表    
    :param sorting_type: 排序选项，可选值        
    name（名称）、rating（评分）、year（年份）、random（随机乱序）    
    """    
    sorting_algos = {        
        
        # sorting_type: (key_func, reverse)        
        'name': (lambda movie: movie.name.lower(), False),        
        'rating': (lambda movie: float(movie.rating), True),        
        'year': (lambda movie: movie.year, True),        
        'random': (lambda movie: random.random(), False),    
        }
        
    try:        
        key_func, reverse = sorting_algos[sorting_type]    
    except KeyError:        
        raise RuntimeError(f'Unknown sorting type: {sorting_type}')    
    sorted_movies = sorted(movies, key=key_func, reverse=reverse)    
    return sorted_movies


# 竭尽所能，避免分支嵌套