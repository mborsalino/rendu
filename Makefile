.PHONY: build clean doc

tag:
ifndef RENDU_VERSION
	@echo no version specified && false
endif
	git tag v_$(RENDU_VERSION)

build: clean
	python3 -m build
	mv dist build
	mv  ./rendu.egg-info build/

doc:
	pdoc ./rendu/htmldeck.py -o ./build/doc --docformat numpy --no-show-source --no-include-undocumented

release: tag build doc
	python3 -m twine upload build/rendu-*.tar.gz build/rendu-*.whl

clean:
	rm -rf ./build
