.PHONY: setup run clean

setup:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running..."
	python script_name.py --repo-owner $(OWNER) --repo-name $(REPO) --branch $(BRANCH) --output-file $(OUTPUT)

clean:
	@echo "Cleaning up..."
	rm -f *.jsonl

help:
	@echo "Makefile commands:"
	@echo "setup    : Install dependencies"
	@echo "run      : Run the script (set OWNER, REPO, BRANCH, OUTPUT)"
	@echo "clean    : Remove generated files"
	@echo "help     : Display this help message"
