PYTHON_ALIAS ?= python
PYTHON_EXISTS := $(shell command -v python >/dev/null 2>&1; echo $$?)
PYTHON2_EXISTS := $(shell command -v python2 >/dev/null 2>&1; echo $$?)
PYTHON3_EXISTS := $(shell command -v python3 >/dev/null 2>&1; echo $$?)

help:
	@echo "----------------------------------------------------------------------------------------------------"
	@echo "Tic-Tac-Toe"
	@echo ""
	@echo "   Commands:"
	@echo "     help:          Show help text."
	@echo "     run:           Run the game"
	@echo "     rpm:           Build the rpm."
	@echo "     install-rpm:   Install the built RPM"
	@echo "     uninstall-rpm: Uninstall the RPM"
	@echo "     clean:         Perform clean of the project"
	@echo ""
	@echo "----------------------------------------------------------------------------------------------------"

.PHONY: python
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

run: python
	$(PYTHON_ALIAS) tictactoe.py

rpm: python
	$(PYTHON_ALIAS) setup.py bdist_rpm

install-rpm: uninstall-rpm rpm
	yum localinstall -y ./dist/tic-tac-toe-*.noarch.rpm --skip-broken

uninstall-rpm:
	yum remove -y tic-tac-toe

clean: python
	$(PYTHON_ALIAS) setup.py clean -a