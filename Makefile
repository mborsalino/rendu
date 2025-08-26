.PHONY: build clean doc

tag:
ifndef RENDU_VERSION
	@echo no version specified && false
endif
	git tag $(RENDU_VERSION_TAG)

build: clean
	python3 -m build
	mv dist build
	mv  ./rendu.egg-info build/

doc:
	pdoc ./rendu/htmldeck.py -o ./build/doc/pdoc --docformat numpy --no-show-source --no-include-undocumented
ifdef RENDU_VERSION
	mv ./build/doc/pdoc/rendu/htmldeck.html ./build/doc/podc/rendu/htmldeck_$(RENDU_VERSION_TAG).html 
endif

release: tag build doc
	python3 -m twine upload build/rendu-*.tar.gz build/rendu-*.whl

clean:
	rm -rf ./build
