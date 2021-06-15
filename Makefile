report.pdf: refs.bib report.tex	report
	latexmk -pdf

report: project.sh
	bash ./project.sh

clean: 
	rm *.dat
	rm *.txt
	rm *.aux
	rm *.fdb_latexmk
	rm *.fls
	rm *.blg
	rm *.bbl
