g=newGraph().activeLayer()
g.setAntialiasing(True)
g.setCanvasFrame(1)
g.drawAxesBackbones(False)
g.setTitle("Transparent filled curves")
g.setTitleFont(QFont("Arial",10,False))
for i in range(0, 4):
	g.setAxisTitle(i, " ")
	g.setMajorTicksType(i, Layer.In)
	g.setMinorTicksType(i, Layer.In)

c = g.addFunction("sin(x)", 0, 2*pi, 100)
c.setTitle("sin(x)")
c.setPen(Qt.red)
c.setBrush(QColor(255, 0, 0, 100))

c = g.addFunction("cos(x)", 0, 2*pi, 100)
c.setTitle("cos(x)")
c.setPen(Qt.green)
c.setBrush(QColor(0, 255, 0, 100))

g.legend().setFrameStyle(0)