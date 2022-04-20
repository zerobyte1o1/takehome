import os
import pytest


pytest.main(['-s','test_cal','--alluredir','./result/xml','--clean-alluredir'])
#启用本机环境allure运行
os.system('/opt/homebrew/Cellar/allure/2.17.3/bin/allure\
           generate \
           --clean ./result/xml/ \
           -o ./result/html/')
