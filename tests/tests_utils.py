from utils.utils import Utils

from unittest import TestCase

class Testutils(TestCase):

    def setUp(self):
        self.util = Utils()
        

    def test_utils_method_add_raise_ValueError_when_given_argument_is_not_Integer(self):
        pass

    def test_utils_method_add_will_return_the_sum_of_input_arguments(self):
        sum = self.util.add(1, 2)

        self.assertEqual(sum, 3)



    def test_subtract_raises_ValueError_when_given_argument_is_not_Integer(self):
        with self.assertRaises(ValueError):
            self.util.subtract(1, 'test')

    def test_subtract_returns_difference_of_input_arguments(self):
        difference = self.util.subtract(3, 2)
        self.assertEqual(difference, 1)

    def test_multiply_raises_ValueError_when_given_argument_is_not_Integer(self):
        with self.assertRaises(ValueError):
            self.util.multiply(2, 'test')

    def test_multiply_returns_product_of_input_arguments(self):
        product = self.util.multiply(3, 2)
        self.assertEqual(product, 6)

    def test_divide_raises_ValueError_when_given_argument_is_not_Integer(self):
        with self.assertRaises(ValueError):
            self.util.divide(1, 'test')

    def test_divide_raises_ValueError_when_divisor_is_zero(self):
        with self.assertRaises(ValueError):
            self.util.divide(1, 0)

    def test_divide_returns_quotient_of_input_arguments(self):
        quotient = self.util.divide(6, 2)
        self.assertEqual(quotient, 3)
        