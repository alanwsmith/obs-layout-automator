#!/usr/bin/env python3

import sys
import unittest
from io import StringIO

class MyClass():
    def is_true(self):
        return True

    def process(self, **kwargs):
        step1 = kwargs['width'] + kwargs['left'] + kwargs['right']
        step2 = step1 / kwargs['source_x']
        # scale = kwargs['width']  / (kwargs['source_x'] + kwargs['left'])
        # scale = (kwargs['source_x'] + kwargs['left']) / kwargs['width']
        scale = step2
        height = int(kwargs['source_y'] * scale)
        value = {
                "width": kwargs['width'],
                "height": height,
                "scale": scale
                }

        


        # step1 = kwargs["width"] + kwargs["left"]
        # step2 = step1 / kwargs['source_x']
        # width = step2 * kwargs["width"]
        # height = int(kwargs['source_y'] / kwargs['source_x'] * width)
        # value = {
        #         "width": width,
        #         "height": height 
        #     }


        if kwargs["rotation"] == 90:
            step0 = kwargs["source_x"] + kwargs["left"]
            # step1 = kwargs["source_x"] / kwargs["source_y"]
            # step1 = kwargs["source_x"] / step0
            step1 =  step0 / kwargs["source_y"] 
            step2 = step1 * kwargs["width"]
            new_value = kwargs["source_x"] / kwargs["source_y"] * kwargs["width"]
            value = {
                "height": kwargs['width'],
                "width": int(step2) ,
                "scale": step1
            }

        return value


class ClassTest(unittest.TestCase):
    
    def setUp(self):
        global mc
        mc = MyClass()

    def test_baseline(self):
        result = mc.process(
                source_x=1920, 
                source_y=1080, 
                width=1920,
                rotation=0, 
                left=0, 
                right=0, 
                top=0, 
                bottom=0,
                )
        self.assertEqual(result['width'], 1920)
        self.assertEqual(result['height'], 1080)
        self.assertEqual(result['scale'], 1.0)

    def test_verify_basic_scale(self):
        result = mc.process(
                source_x=2000, 
                source_y=1000, 
                width=1000,
                rotation=0, 
                left=0, 
                right=0, 
                top=0, 
                bottom=0,
                )
        self.assertEqual(result['width'], 1000)
        self.assertEqual(result['height'], 500)
        self.assertEqual(result['scale'], 0.5)

    def test_left_crop_no_rotation(self):
        result = mc.process(
                source_x=1000, 
                source_y=1000, 
                width=1000,
                rotation=0, 
                left=100, 
                right=0, 
                top=0, 
                bottom=0,
                )
        self.assertEqual(result['width'], 1000)
        self.assertEqual(result['scale'], 1.1)
        self.assertEqual(result['height'], 1100)

    def test_left_and_right_crop_no_rotation(self):
        result = mc.process(
                source_x=1000, 
                source_y=1000, 
                width=1000,
                rotation=0, 
                left=100, 
                right=100, 
                top=0, 
                bottom=0,
                )
        self.assertEqual(result['width'], 1000)
        self.assertEqual(result['scale'], 1.2)
        self.assertEqual(result['height'], 1200)


    def test_rotation_baseline(self):
        result = mc.process(
                source_x=1920, 
                source_y=1080, 
                width=1920,
                rotation=90, 
                left=0, 
                right=0, 
                top=0, 
                bottom=0,
                )
        self.assertEqual(result['width'], 3413)
        self.assertEqual(result['height'], 1920)
        self.assertEqual(result['scale'], 1.7777777777777777)

    def test_left_crop_with_rotation(self):
        result = mc.process(
                source_x=1000, 
                source_y=1000, 
                width=1000,
                rotation=90, 
                left=100, 
                right=0, 
                top=0, 
                bottom=0,
                )
        self.assertEqual(result['width'], 1100)
        self.assertEqual(result['scale'], 1.1)
        self.assertEqual(result['height'], 1000)


    # def test_left_crop_normal(self):
    #     result = mc.process(
    #             source_x=1000, 
    #             source_y=1000, 
    #             width=1000,
    #             rotation=0, 
    #             left=200, 
    #             right=0, 
    #             top=0, 
    #             bottom=0,
    #             )
    #     self.assertEqual(result['width'], 1000)
    #     # self.assertEqual(result['height'], 1200)




    # def test_2(self):
    #     result = mc.process(
    #             source_x=1920, 
    #             source_y=1080, 
    #             width=1920,
    #             rotation=90, 
    #             left=0, 
    #             right=0, 
    #             top=0, 
    #             bottom=0,
    #             )
    #     self.assertEqual(result['height'], 1920)
    #     self.assertEqual(result['width'], 3413)
    

    # def test_3(self):
    #     result = mc.process(
    #             source_x=1000, 
    #             source_y=800, 
    #             width=1000,
    #             rotation=0, 
    #             left=200, 
    #             right=0, 
    #             top=0, 
    #             bottom=0,
    #             )
    #     self.assertEqual(result['width'], 1000)
    #     # self.assertEqual(result['height'], 960)

    # def test_4(self):
    #     result = mc.process(
    #             source_x=1000, 
    #             source_y=1000, 
    #             width=1000,
    #             rotation=0, 
    #             left=200, 
    #             right=0, 
    #             top=0, 
    #             bottom=0,
    #             )
    #     self.assertEqual(result['width'], 1000)
    #     # self.assertEqual(result['height'], 1230)






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


