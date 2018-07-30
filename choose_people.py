#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import Random
r = Random()

friends = []
#friends.append("")
friends.append("a")
friends.append("b")
friends.append("c")

#1人を選ぶ
lucky_number = r.sample(xrange(len(friends)), 1)

#表示
print friends[lucky_number[0]]+"さんに決まりました"
