.PHONY: all

all:
	volare enable -l sky130_fd_sc_hs --pdk sky130
	make -f test.mk clean
	make -f test.mk

clean:
	rm results.xml || true
