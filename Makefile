.PHONY: build clean

build: clean
	python3 -m build
	mv dist build
	mv  ./rendu.egg-info build/

upload: build
	python3 -m twine upload build/rendu-*.tar.gz build/rendu-*.whl

clean:
	rm -rf ./build
