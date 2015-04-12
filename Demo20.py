#coding=utf-8
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
font=FontProperties(fname=r"C:\Windows\Fonts\SIMYOU.ttf",size=14)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))

plt.xlabel(u'性别',fontproperties=font)
plt.ylabel(u'人数',fontproperties=font)

plt.title(u"性别比例分析",fontproperties=font)
plt.xticks((0,1),(u'男',u'女'),fontproperties=font)
rect = plt.bar(left = (0,1),height = (1,0.5),width = 0.35,align="center")

plt.legend((rect,),(u"图例",))
#plt.legend(u"图例",fontproperties=font)
autolabel(rect)

plt.show()