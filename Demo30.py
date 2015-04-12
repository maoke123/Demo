#coding=utf-8
from enthought.traits.api import BaseInt
class OddInt(BaseInt):
	default_value=1

	info_text='an odd integer'

	def validate(self,object,name,value):
		#检验是否为奇数
		value=super(OddInt,self).validate(object,name,value)#判断是否为整数
		if(value%2)==1:
			return value
		self.error(Object,name,value)