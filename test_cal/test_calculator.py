import pytest
from util.readfile import YamlHandle
class TestCalculator:

    @pytest.mark.p0
    @pytest.mark.parametrize('data',YamlHandle('../data/use.yaml').get_data('add'))
    def test_add(self,get_cal,data):


        res = get_cal.add(1,2)
        pytest.assume()


    def test_div(self, a, b):

        return
