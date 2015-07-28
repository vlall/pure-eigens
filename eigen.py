import numpy as np
from bokeh.plotting import figure, HBox, output_file, show, VBox
from bokeh.models import Range1d
from bokeh.models import HoverTool
# Center your matrix

def center(v):
	x = 0
	y = 0
	for i in v:
		x+=i[0]
		y+=i[1]
	# What average?
	meanX = np.mean(x)
	meanY = np.mean(y)
	centV = []
	for i in v:
		newPoint = ((i[0]-meanX), (i[1]-meanY))
		centV.append(newPoint)
	return centV

def col_v(v):
	x = []
	y = []
	for i in v:
		x.append(i[0])
		y.append(i[1])
	return (x,y)

def graph(v):
	vectors = col_v(v)
	x = vectors[0]
	y = vectors[1]
	# Output to static HTML file
	output_file("lines.html", title="line plot example")
	hover = HoverTool(
	    tooltips = [
	        ("index", "$index"),
	        ("(x,y)", "($x, $y)"),
		]
	)
	TOOLS='box_zoom,box_select,crosshair,resize,reset'
	p = figure(plot_width=600,plot_height=400,tools=[hover, TOOLS])

	p.circle(x, y, size=20)
	# Show the results
	show(p)

def cov_Matrix(m):
	vectors = col_v(m)
	x = vectors[0]
	y = vectors[1]
	n = len(x)
	summation = 0
	for i, valx in enumerate(x):
		prod = float(valx*y[i])
		summation+=prod
	cov = summation/n-1
	return cov

def main():
	v = [(-1,2), (-1,1), (1,-2),(4,2), (2,2), (-2,0), (-3,-2), (2,0)]
	graph(v)
	print v
	centerVec = center(v)
	summation = cov_Matrix(centerVec)
	print centerVec
	print summation
main()
