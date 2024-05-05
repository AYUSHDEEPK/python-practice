import pytest
from exercise import emp
class testemp:
    def setup(self):
        '''make an employee to use in tests'''
        self.eric=emp("ayush","kumar",1000000)
    def test_default_raise(self):
        '''it will test the defalt that it work properly right or not.'''
        self.eric.give_raise(400000)
        assert 1400000 in emp.give_raise()
clas=testemp()
clas.test_default_raise()==1400000
