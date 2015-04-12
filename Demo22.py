# -*- coding: utf-8 -*-
"""
演示Trait属性的各种功能： 初始化、验证、代理、监听、界面
"""
from enthought.traits.api import  HasTraits, Range, Int, Float
coefficient=Range(-1.0,1.0,0.0)

class Quadratic(HasTraits):
	c2=coefficient
	c1=coefficient
	c0=coefficient

class Quadratic2(HasTraits):
	c2=Range(-1.0,1.0,0.0)
	c1=Range(-1.0,1.0,0.0)
	c0=Range(-1.0,1.0,0.0)
