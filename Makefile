report.pdf: refs.bib report.tex	report
	latexmk -pdf

report: project.sh
	bash ./project.sh

clean: cleanup

cleanup:
	latexmk -c

.PHONY: cleanup
.PHONY: clean
