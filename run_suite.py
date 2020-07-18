import unittest
import HTMLTestRunner
import time

dir = './'
discover = unittest.defaultTestLoader.discover(dir, pattern='test*.py')

# all_suites = unittest.TestSuite()
#
# all_suites.addTest(discover)
# unittest.main(defaultTest='all_suites', verbosity=2)
path = './report/'
now = time.strftime('%Y-%m-%d_%H_%M_%S')
report = path + now + 'report.html'
file = open(report, 'wb')
run1 = HTMLTestRunner.HTMLTestRunner(stream=file, title='微信接口测试用例', description='T12901')
run1.run(discover)
file.close()
