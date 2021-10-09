# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(13, 12, 5), 'Right', '13,12,5 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be equilateral')

    def testEquilateralTriangleC(self):
        self.assertNotEqual(classifyTriangle(3, 3, 1), 'Is not a Equilateral')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(6,6,5),'Isosceles','6,6,5 is a Isosceles triangle')
    
    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(4,6,6),'Isosceles','4,6,6 is a Isosceles triangle')

    def testIsoscelesTriangleC(self): 
        self.assertNotEqual(classifyTriangle(6,2,5),'Not an Isosceles','6,2,5 is not an Isosceles triangle')

    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(5,7,215),'InvalidInput','Input should be less than 200')

    def testInvalidTriangleB(self): 
        self.assertEqual(classifyTriangle(3,-1,2),'InvalidInput','Input cannot be negative')

    def testInvalidTriangleC(self): 
        self.assertEqual(classifyTriangle(5,0,5),'InvalidInput','Input cannot be zero')
    
    def testInvalidTriangleD(self): 
        self.assertEqual(classifyTriangle('x','y','z'),'InvalidInput','Input should be integer')

    def testInvalidTriangleE(self): 
        self.assertEqual(classifyTriangle(3.5,4,12),'InvalidInput','value must be integer only.')
    
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(7,3,6),'Scalene','7,3,6 is a Scalene triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(12,8,11),'Scalene','12,8,11 is a Scalene triangle')
    
    def testScaleneTriangleC(self): 
        self.assertNotEqual(classifyTriangle(2,2,6),'Not a Scalene,', '2,2,6 is not a  Scalene triangle')
    
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(45,20,120),'NotATriangle','45,20,120 is Not A Triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(6, 2, 1), 'NotATriangle','6,2,1 is Not A Triangle')
    
    def testNotATriangleC(self):
        self.assertNotEqual(classifyTriangle(6, 5, 4), 'Is a valid triangle which is a scalene one',)

if __name__ == '__main__' :
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

