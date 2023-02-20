#!/usr/bin/env python3

import sys
import unittest
from io import StringIO

class MyClass():
    def is_true(self):
        return True

    def process(self, **kwargs):
        value = {
                "width": 1920,
                "height": 1080 
            }

        if kwargs["rotation"] == 90:
            new_value = kwargs["scene_x"] / kwargs["scene_y"] * kwargs["width"]
            value = {
                "height": kwargs['width'],
                "width": int(new_value) 
            }

        return value


class ClassTest(unittest.TestCase):
    
    def setUp(self):
        global mc
        mc = MyClass()

    def test_1(self):
        result = mc.process(
                scene_x=1920, 
                scene_y=1080, 
                width=1920,
                rotation=0, 
                left=0, 
                right=0, 
                top=0, 
                bottom=0,
                )
        self.assertEqual(result['width'], 1920)
        self.assertEqual(result['height'], 1080)

    def test_2(self):
        result = mc.process(
                scene_x=1920, 
                scene_y=1080, 
                width=1920,
                rotation=90, 
                left=0, 
                right=0, 
                top=0, 
                bottom=0,
                )
        self.assertEqual(result['height'], 1920)
        self.assertEqual(result['width'], 3413)
    


if __name__ == '__main__':

    def run_tests():
        capture_stream = StringIO()
        suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
        results = unittest.TextTestRunner(stream=capture_stream, failfast=True).run(suite)

        if len(results.failures) or len(results.errors):
            print("\033[31m")
            print("ERROR: Failed Test Run - Execution halted.")
            print(capture_stream.getvalue())
            print("\033[m")
            sys.exit()
        else:
            print("\033[32m")
            print(capture_stream.getvalue())
            print("\033[m")

    def run_main():
        print("Yeah, it worked!")

    run_tests()
    run_main()


