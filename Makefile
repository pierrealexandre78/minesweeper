.PHONY: tests
tests :
	@echo "Running tests...";\
	export PYTHONPATH=.;\
	echo $(PYTHONPATH);\
	black src/*;\
	pylint src/*;\
	pytest -v