report.pdf: refs.bib report.tex	report
	latexmk -pdf
	latexmk -c

report: project.sh
	bash ./project.sh

