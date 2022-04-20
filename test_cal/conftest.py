import pytest
from test.calculator import Calculator
from util.readfile import YamlHandle
@pytest.fixture(scope='class')
def get_cal():
    cal = Calculator()
    return cal