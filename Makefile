.PHONY: all
MAKEFLAGS += --silent

all: help

help:
	@grep -E '^[a-zA-Z1-9\._-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| sed -e "s/^Makefile://" -e "s///" \
		| awk 'BEGIN { FS = ":.*?## " }; { printf "\033[36m%-30s\033[0m %s\n", $$1, $$2 }'
edgee_world:
	uv sync
	# generate bindings from wit
	componentize-py --wit-path wit/  -w data-collection bindings edgee_world


output.wasm:
	componentize-py --wit-path wit/ --world data-collection componentize component -o output.wasm

setup: edgee_world ## setup development environment

build: setup output.wasm ## build component

clean: ## clean build artifacts
	rm -rf output.wasm
	rm -rf edgee_world
	rm -rf __pycache__
