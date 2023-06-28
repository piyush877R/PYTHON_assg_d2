from unittest import TestCase
import pandas as pd 
from all_func import Func
from loss_func import squar_error


class test(TestCase):
    def setup(self):
        
        datas1 = {"x":[1.0,2.0,3.0],"y":[5.0,6.0,7.0]}
        self.dataframe_1 = pd.DataFrame(data=datas1)

        datas2 = {"x":[1.0,2.0,3.0],"y":[7.0,8.0,9.0]}
        self.dataframe_2 = pd.DataFrame(data=datas2)

        self.func1 = Func("name")
        self.func1.dataframe = self.dataframe1

        self.func2 = Func("name")
        self.func2.dataframe = self.dataframe2

    def tear_down(self):
        pass

    def test_sqr_error(self):


        self.assertEql(squar_error(self.func1, self.func2),12.0)

       

        self.assertEql(squar_error(self.func2, self.func_1), 12.0)

     

        self.assertEql(squar_error(self.func1, self.func1), 0.0)