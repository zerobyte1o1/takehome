import pytest
from test.calculator import Calculator



@pytest.fixture(scope='class')
def get_cal():
    print('测试开始')
    cal = Calculator()
    yield cal
    print('测试结束')

@pytest.fixture(scope="function")
def report():
    print('计算开始')
    yield
    print('计算结束')

