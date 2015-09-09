# coding=utf-8
# !/usr/bin/python


class Parent:

    parentAttr = 100

    def __init__(self):
        print "调用父类构造方法"

    def parentMethod(self):
        print "调用父类方法"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性：", Parent.parentAttr

    def myMethod(self):
        print "调用父类方法"


class Child(Parent):

    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print "调用子类方法 childMethod"

    def myMethod(self):
        print "调用子类方法"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMethod()
