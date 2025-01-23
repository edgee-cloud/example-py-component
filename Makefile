.PHONY: all
MAKEFLAGS += --silent

all: help

help:
	@grep -E '^[a-zA-Z1-9\._-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| sed -e "s/^Makefile://" -e "s///" \
		| awk 'BEGIN { FS = ":.*?## " }; { printf "\033[36m%-30s\033[0m %s\n", $$1, $$2 }'
edgee_world:
	# grab python reqs
	uv sync
	# generate bindings from wit
	uv run componentize-py --wit-path wit/ bindings edgee_world

setup: edgee_world ## setup development environment

build: setup ## build component
	uv run componentize-py --wit-path wit/ --world data-collection componentize dc-component -o dc-component.wasm

clean: ## clean build artifacts
	rm -rf dc-component.wasm
	rm -rf edgee_world
	rm -rf __pycache__
