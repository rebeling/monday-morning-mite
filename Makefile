
graph:
	pycallgraph --exclude "requests.*" --max-depth 3 graphviz -- ./main.py
	open pycallgraph.png
