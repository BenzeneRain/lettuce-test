# -*- coding: utf-8 -*-
from lettuce import step
from lettuce import world

@step(u'Given I am on the root URI')
def given_i_am_on_the_root_uri(step):
    url = "http://localhost:8888/"
    world.browser.visit(url)

@step(u'Then I should see "([^"]*)"')
def then_i_should_see_group1(step, group1):
    assert True, world.browser.is_text_present("Hello, world!")

