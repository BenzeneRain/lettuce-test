from lettuce import world
from splinter.browser import Browser

world.browser = Browser('zope.testbrowser')
