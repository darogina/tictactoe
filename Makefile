PYTHON_ALIAS ?= python
PYTHON_EXISTS := $(shell command -v python >/dev/null 2>&1; echo $$?)
PYTHON2_EXISTS := $(shell command -v python2 >/dev/null 2>&1; echo $$?)
PYTHON3_EXISTS := $(shell command -v python3 >/dev/null 2>&1; echo $$?)
DOCKER_EXISTS := $(shell command -v docker >/dev/null 2>&1; echo $$?)
PODMAN_EXISTS := $(shell command -v podman >/dev/null 2>&1; echo $$?)

IMAGE_NAME := tictactoe:latest

help:
	@echo "----------------------------------------------------------------------------------------------------"
	@echo "Tic-Tac-Toe"
	@echo ""
	@echo "   Commands:"
	@echo "     help:          Show help text."
	@echo "     run:           Run the game"
	@echo "     build-rpm:     Build the rpm."
	@echo "     rpm-install:   Install the built RPM"
	@echo "     rpm-uninstall: Uninstall the RPM"
	@echo "     docker-build:  Build the Docker image"
	@echo "     docker-run:    Run the Docker image"
	@echo "     podman-build:  Build the Podman image"
	@echo "     podman-run:    Run the Podman image"
	@echo "     clean:         Perform clean of the project"
	@echo ""
	@echo "----------------------------------------------------------------------------------------------------"

.PHONY: python docker podman
python:
ifeq ($(PYTHON_EXISTS), 0)
	$(eval PYTHON_ALIAS := python)
else ifeq ($(PYTHON2_EXISTS), 0)
	$(eval PYTHON_ALIAS := python2)
else ifeq ($(PYTHON3_EXISTS), 0)
	$(eval PYTHON_ALIAS := python3)
else
	$(error "Python not installed")
endif

docker:
ifeq ($(DOCKER_EXISTS), 1)
	$(error "Docker not installed")
endif

podman:
ifeq ($(PODMAN_EXISTS), 1)
	$(error "Podman not installed")
endif

run: python
	$(PYTHON_ALIAS) tictactoe.py

rpm: python
	$(PYTHON_ALIAS) setup.py bdist_rpm

rpm-install: rpm-uninstall rpm
	yum localinstall -y ./dist/tic-tac-toe-*.noarch.rpm --skip-broken

rpm-uninstall:
	yum remove -y tic-tac-toe

docker-build: docker
	docker build -t $(IMAGE_NAME) .

docker-run: docker
	docker run --rm -it $(IMAGE_NAME)

podman-build: podman
	podman build -t $(IMAGE_NAME) .

podman-run: podman
	podman run --rm -it $(IMAGE_NAME)

clean: python
	$(PYTHON_ALIAS) setup.py clean -a