import unittest
import pandas as pd
import pd_ts

class TestSalesDataFrameCalc(unittest.TestCase):

    def test_foo(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_foo2(self):
        self.assertEqual(1+1, 2)

    def test_weekly(self):
        # setup: input testadat
        dti = pd.bdate_range("2021-08-10", "2022-08-05")
        sdf = pd.DataFrame({'date': dti, 'sales': range(len(dti))})

        # call
        result = pd_ts.getPeriodSalesData(sdf, 'W', 'week')

        # assert: ellenőrzés
        print(result.tail(20))
        self.assertEqual(len(result), 259)
        self.assertEqual(len(result.loc[(result['date'] == '2022-08-01') & (result['prev_weekly_sales_max'] == 253)]), 1)

    def test_quarterly(self):
        # setup: input testadat
        dti = pd.bdate_range("2021-08-10", "2022-08-05")
        sdf = pd.DataFrame({'date': dti, 'sales': range(len(dti))})

        # call
        result = pd_ts.getPeriodSalesData(sdf, 'Q', 'quarter')

        # assert: ellenőrzés
        print(result.tail(20))
        self.assertEqual(len(result), 259)
        self.assertEqual(len(result.loc[(result['date'] == '2022-08-01') & (result['prev_quarterly_sales_max'] == 232)]), 1)

if __name__ == '__main__':
    unittest.main()
