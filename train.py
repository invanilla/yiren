#-*- coding:utf-8 -*-
import unittest,time,HTMLTestRunner
from ddt import ddt,data

@ddt
class MyTestCase(unittest.TestCase):

    @data(1,2,3)
    def test_something(self,value):
        self.assertEqual(value, 2)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    loder = unittest.TestLoader()
    suite=loder.loadTestsFromTestCase(MyTestCase)
    #报告--H5报告
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    with open("./report_%s.html" % now,"wb+") as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=3,title="测试报告")
        runner.run(suite)