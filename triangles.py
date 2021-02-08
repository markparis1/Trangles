
import unittest

def classify_triangle(a: int, b: int, c: int) -> str:

    result: str = ""

    if a == b and a == c:

        result += "equilateral"

    elif a == b or a == c or b == c:

        result += "isosceles"

    elif not a == b and not a == c and not b == c:

        result += "scalene"

    if ((a ** 2) + (b ** 2)) == (c ** 2):

        result += " and right"

    return result

class TestTriangleFunction(unittest.TestCase):

    def test_classify_triangle(self):

        self.assertEqual(classify_triangle(5,5,5), "equilateral")
        self.assertFalse(classify_triangle(5,2,5) == "equilateral")
        self.assertEqual(classify_triangle(5,2,5), "isosceles")
        self.assertFalse(classify_triangle(5,2,6) == "isosceles")
        self.assertTrue(classify_triangle(5,12,13) == "scalene and right")



if __name__ == "__main__":

    print(classify_triangle(1,1,2))
    print(classify_triangle(1,2,3))
    print(classify_triangle(1,1,1))
    print(classify_triangle(5,12,13))
    
    unittest.main(exit=True)
