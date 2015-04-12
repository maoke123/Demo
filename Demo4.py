from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
fig=plt.figure()
line1=Line2D([0,1],[0,1],tranform=fig.transFigure,figure=fig,color="r")
#line2=Line2D([0,1],[1,0],tranform=fig.transFigure,figure=fig,color="g")
#fig.lines.extend([line1,line2])
fig.show()