import pytest
import allure
from util.readfile import YamlHandle



class TestCalculator:

    @pytest.mark.p0
    @pytest.mark.parametrize('case', YamlHandle('./data/use_case.yaml').get_data('add'))
    def test_add(self, get_cal,report, case):
        allure.dynamic.title(case['title'])
        allure.dynamic.tag(case['tag'])
        res = get_cal.add(case['data']['a'], case['data']['b'])
        pytest.assume(case['msg']['res'] == res)

    @pytest.mark.p1
    @pytest.mark.parametrize('case', YamlHandle('./data/use_case.yaml').get_data('div'))
    def test_div(self, get_cal, report, case):
        allure.dynamic.title(case['title'])
        allure.dynamic.tag(case['tag'])
        res = get_cal.div(case['data']['a'], case['data']['b'])
        pytest.assume(case['msg']['res'] == res)
