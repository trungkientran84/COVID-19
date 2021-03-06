include ./help.mk

image_repo=3778
image=$(image_repo)/covid-19:latest

launch:
	streamlit run simulator/app.py

bin/gh-md-toc:
	mkdir -p bin
	wget https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc
	chmod a+x gh-md-toc
	mv gh-md-toc bin/

.PHONY: README.md
README.md: bin/gh-md-toc
	./bin/gh-md-toc --insert README.md
	rm -f README.md.orig.* README.md.toc.*

.PHONY: covid-19
covid-19: ## Run covid-19 container
	docker run \
		--rm \
		--detach \
		--publish 8501:8501 \
		--name covid-19 \
		--volume $(shell pwd):/covid-19 \
		$(image)

.PHONY: remove-covid-19
remove-covid-19: ## Remove covid-19 container if exit
	docker rm -f covid-19

.PHONY: image
image: ## Build covid-19 image
	docker build . --tag $(image)

.PHONY: test
test:
ifneq "$(shell which pytest)" ""
	pytest --doctest-modules --verbose covid19/
else
	docker run --rm $(image) pytest --doctest-modules --verbose covid19/
endif
