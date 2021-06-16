report.pdf: refs.bib report.tex	report
	latexmk -pdf

report: project.sh
	bash ./project.sh

clean:
	latexmk -c

