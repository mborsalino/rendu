.PHONY: build clean

build: clean
	python -m build
	mv dist build
	mv  ./rendu.egg-info build/

clean:
	rm -rf ./build
