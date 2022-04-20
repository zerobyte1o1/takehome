import pytest
import allure
from util.readfile import YamlHandle



class TestCalculator:

    @allure.feature('测试项目')
    @allure.story('加法测试')
    @pytest.mark.p0
    @pytest.mark.parametrize('case', YamlHandle('./data/use_case.yaml').get_data('add'))
    def test_add(self, get_cal,report, case):
        allure.dynamic.title(case['title'])
        res = get_cal.add(case['data']['a'], case['data']['b'])
        pytest.assume(case['msg']['res'] == res)

    @allure.feature('测试项目')
    @allure.story('减法测试')
    @pytest.mark.p1
    @pytest.mark.parametrize('case', YamlHandle('./data/use_case.yaml').get_data('div'))
    def test_div(self, get_cal, report, case):
        allure.dynamic.title(case['title'])
        res = get_cal.div(case['data']['a'], case['data']['b'])
        pytest.assume(case['msg']['res'] == res)
