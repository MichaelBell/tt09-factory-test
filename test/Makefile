.PHONY: all

all:
	python setup.py
	make -f test.mk clean
	make -f test.mk

clean:
	rm results.xml || true
