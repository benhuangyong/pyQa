# -*- coding:utf-8 -*-
from .WebElement import *

import pdb
class RadioButtonElement(WebElement):
    def __init__(self, element_type, locator):
        WebElement.__init__(self, element_type, locator)