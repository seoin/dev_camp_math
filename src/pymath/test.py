import os
import sys

from PyFormula import *
from PySet import *

# source code for testing

if __name__ == '__main__':
    default = False
    if len(sys.argv) == 1:
        default = True
    elif len(sys.argv) >= 3:
        quiet = sys.argv[2] == 'q'
    else:
        quiet = False
    noisy = not quiet
    
    if default or sys.argv[1] == 'set':
        print('Testing PySet Module')
        print('---------------------')
        if noisy:
            print('Testing class PySet')
            print('Testing Pyset Constructor')
        
        a = PySet(lambda x:x%2==0)  # {x|x is even}
        b = PySet(lambda x:x in [1,2,3]) # {1,2,3}
        c = PySet(lambda x:x%2==1) # {x|x is odd}
        d = PySet(lambda x:1<x<6 and isinstance(x, int)) 
        e = PySet(lambda x:x%3==1)
        print('---------------------')
        if noisy:
            print('Testing PySet methods.')
            print('Testing PySet.__add__')
        
        assert 1 in a+b, 'Error in PySet.__add__'
        assert 2 in a+b, 'Error in PySet.__add__'
        assert 3 in a+b, 'Error in PySet.__add__'
        
        for i in range(100):
            assert i in a+c, 'Error in PySet.__add__, %d'%i
        print('---------------------')
        if noisy:
            print('Testing PySet.__sub__')
            
        assert 2 in a-c, 'Error in PySet.__sub__'
        assert 1 in b-a, 'Error in PySet.__sub__'
        assert 4 in d-b, 'Error in PySet.__sub__'
        assert 0 in a-e, 'Error in PySet.__sub__'
        assert 7 in e-a, 'Error in PySet.__sub__'
        print('---------------------')    
        if noisy:
            print('Testing PySet.__mul__')
        
        assert (2,1) in a*e, 'Error in PySet.__mul__'
        assert (2,2) in a*b, 'Error in PySet.__mul__' 
        assert (1,2) in c*b, 'Error in PySet.__mul__'
        print('---------------------')
        if noisy:
            print('Testing PySet.intersection')
            
        assert 2 in a.intersection(b), 'Error in PySet.intersection'
        assert 2 in b.intersection(a), 'Error in PySet.intersection'
        for i in range(100):
            assert i not in a.intersection(c), 'Error in PySet.intersection'
        print('---------------------')    
        if noisy:
            print('Testing PySet.cup')
        
        assert 1 in PySet.cup(a,b,c,d,), 'Error in PySet.cup'
        assert 2 in PySet.cup(a,b,c), 'Error in PySet.cup'
        assert 3 in PySet.cup(a,b), 'Error in PySet.cup'
        
        for i in range(100):
            assert i in PySet.cup(a,c), 'Error in PySet.cup, %d'%i    
        
        
        print('---------------------')    
        if noisy:
            print('Testing PyCountableSet')
        
        def integer_generator():
            i = 0
            while True:
                yield i
                i += 1
                yield -1*i
            
        PyInt = PyCountableSet(integer_generator)
        
        def rational_generator():
            # implementation of Calkin-Wilf Sequence
            from math import floor
            i = 1
            yield 0
            while True:
                yield i
                i = 1/(2*floor(i)-i+1)

        PyRational = PyCountableSet(rational_generator)
        print('---------------------')
        if noisy:
            print('Testing PyCountableSet.list_elements')    
        PyInt.list_elements()
        PyRational.list_elements()
        print('---------------------')
        if noisy:
            print('Testing PyFiniteSet')
        
        a = PyFiniteSet(1,2,3)
        b = PyFiniteSet(3,4,5,6)
        c = PyFiniteSet(1,2,3,4,5,6)
        d = PyFiniteSet(3,4,5,6)
        e = PyFiniteSet(1,2,3)
        print('---------------------')
        if noisy:
            print('Testing PyFiniteSet.__str__')
        assert str(a) == '{1, 2, 3}', 'Error in PyFiniteSet.__str__'
        assert str(b) == '{3, 4, 5, 6}', 'Error in PyFiniteSet.__str__'
        print('---------------------')
        if noisy:
            print('Testing PyFiniteSet.__add__')
        
        assert a+b == PyFiniteSet(1,2,3,4,5,6), 'Error in PyFiniteSet.__add__'
        print('---------------------')
        if noisy:
            print('Testing PyFiniteSet.__sub__')
            
        assert a-b == PyFiniteSet(1,2), 'Error in PyFiniteSet.__sub__'
        assert b-a == PyFiniteSet(4,5,6), 'Error in PyFiniteSet.__sub__'
        print('---------------------')
        if noisy:
            print('Testing PyFiniteSet.intersection')
        assert a.intersection(b) == PyFiniteSet(3)
        print('---------------------')
        if noisy:
            print('Testing PyFiniteSet.subsets')
        for elem in a.subsets():
            print(elem)
        print('---------------------')
        if noisy:
            print('Testing PyFiniteSet inclusion')
            
        assert a==e, 'Error in PyFiniteSet inclusion'
        assert a>=e, 'Error in PyFiniteSet inclusion'
        assert a<=e, 'Error in PyFiniteSet inclusion'
        assert not a>e, 'Error in PyFiniteSet inclusion'
        assert b==d, 'Error in PyFiniteSet inclusion'
        assert a<c, 'Error in PyFiniteSet inclusion'
        assert b<c, 'Error in PyFiniteSet inclusion'
        print('---------------------')
        if noisy:
            print('Testing PyOrderedSet')
        PyInt = PyOrderedSet(\
                integer_generator,
                lambda x,y:x-y)    
        
        PyRational = PyOrderedSet(\
                rational_generator, 
                lambda x,y:x-y)
    
        print('---------------------')
        if noisy:
            print('Testing PyOrderedSet.list_elements')
            
        PyInt.list_elements()
        PyRational.list_elements()
        print('---------------------')
        if noisy:
            print('Testing PyPartiallyOrderedSet')
        
        fastcampus_lectures = [\
            ('Coding 101', ('프로그래밍 유치원 캠프', '파이썬을 이용한 업무 자동화', '안드로이드 앱 개발 시작하기 CAMP')), 
            ('프로그래밍 유치원 캠프', ('왕초보의 파이썬 웹 프로그래밍',)), 
            ('파이썬을 이용한 업무 자동화', ('파이썬 완전 정복 CAMP',)), 
            ('왕초보의 파이썬 웹 프로그래밍', ('안드로이드 개발 SCHOOL(플립러닝)')),
            ('파이썬 완전 정복 CAMP', ()),
            ('안드로이드 앱 개발 시작하기 CAMP', ('안드로이드 개발 SCHOOL(플립러닝)', '안드로이드 앱 개발 프로젝트 CAMP')),
            ('안드로이드 앱 개발 프로젝트 CAMP', ()),
            ('안드로이드 개발 SCHOOL(플립러닝)', ()),]
        
        def lecture_generator():
            yield from fastcampus_lectures
            
        def cmp(l, r):
            if l[0] in r[1]:
                return False # r < l 
            elif r[0] in l[1]:
                return True # l < r
            else:
                return None
            
        lectures = PyPartiallyOrderedSet(lecture_generator, cmp)
        print('---------------------')
        if noisy:
            print('Testing PyPartiallyOrderedSet.topological_sort')
        
        for lecture in lectures.topological_sort():
            print(lecture[0])
        print('---------------------')
        print('Passed All Tests')