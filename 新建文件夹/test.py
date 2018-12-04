#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-18 15:03:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import time
import re

t = time.time()
print(t)
str = "00000003210Runoob01230000000" 
print(str.strip( '0' ))

a='Beautiful, is; better*than\nugly'
# 四个分隔符为：,  ;  *  \n
x= re.split(',|; |\*|\n',a)
print(x)