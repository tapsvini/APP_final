from unittest import TestCase
from src.util.UserInputUtil import InputUtility

class TestInputUtility(TestCase):

    def test_list_int_vldtn(self):
        test_int = InputUtility.list_int_vldtn("")
        self.fail()

    def test_int_vldtn(self):
        test_int=InputUtility.int_vldtn("Testing")
        self.assertTrue()
        if test_int!=int(test_int):
            self.fail()


    def test_txt_vldtn(self):
        self.fail()

    def test_int_rng_vldtn(self):
        self.fail()
