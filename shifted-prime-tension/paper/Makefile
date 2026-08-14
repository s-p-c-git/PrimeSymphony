# Build the paper. Requires TeX Live (latexmk + pdflatex).
MAIN = main

.PHONY: all clean arxiv

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex $(wildcard figures/*.png)
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

# Strip build artifacts (also covered by .gitignore).
clean:
	latexmk -C
	rm -f $(MAIN).bbl $(MAIN).out

# Produce a clean arXiv upload tarball (source + figures only).
arxiv: all clean
	tar czf arxiv-submission.tar.gz $(MAIN).tex figures/
