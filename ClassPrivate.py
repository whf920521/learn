# coding=utf-8
# !/usr/bin/python


class JustCounter:
    __seretCount = 0
    publicCount = 0

    def count(self):
        self.__seretCount += 1
        self.publicCount += 1
        print self.__seretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter._JustCounter__seretCount
