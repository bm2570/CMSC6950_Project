report.pdf: refs.bib output report.tex	
	latexmk -pdf

output: project.sh
	./project.sh
