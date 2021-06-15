report.pdf: refs.bib report.tex	
	latexmk -pdf

output: project.sh
	bash ./project.sh

