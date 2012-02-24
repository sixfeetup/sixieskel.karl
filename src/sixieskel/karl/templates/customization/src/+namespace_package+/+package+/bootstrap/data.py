from zope.interface import implements
from karl.bootstrap.interfaces import IInitialOfficeData
from karl.bootstrap.data import DefaultInitialData


class SampleInitialData(DefaultInitialData):
    pass


class SampleInitialOfficeData(object):
    implements(IInitialOfficeData)
