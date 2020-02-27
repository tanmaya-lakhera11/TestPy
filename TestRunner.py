from unittest import TestSuite,TestLoader,TextTestRunner
from Tests import JUnitTest, unit2
import HtmlTestRunner

tc1 = TestLoader().loadTestsFromTestCase(unit2.unittest1)
tc2 = TestLoader().loadTestsFromTestCase(JUnitTest.unittest2)

testSuite = TestSuite([tc1,tc2])
runner = TextTestRunner(verbosity=2).run(testSuite)

