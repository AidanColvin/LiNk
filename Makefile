# --- Configuration ---
# Python interpreter (use python3 for Linux/Mac/Codespaces)
PYTHON = python3
MAIN_SCRIPT = main.py
LOGIC_SCRIPT = connection_generator.py
DATA_FILE = master_category_bank.json
TEST_DIR = tests

# --- Color Codes for Terminal Output ---
BLUE = \033[1;34m
GREEN = \033[1;32m
RED = \033[1;31m
RESET = \033[0m

.PHONY: run test check clean help

# Default target
help:
	@echo "$(BLUE)Connections Project Management:$(RESET)"
	@echo "  $(GREEN)make run$(RESET)    - Launch the Connections Game"
	@echo "  $(GREEN)make test$(RESET)   - Run the 50-test suite (Headless compatible)"
	@echo "  $(GREEN)make check$(RESET)  - Verify project files and dependencies"
	@echo "  $(GREEN)make clean$(RESET)  - Remove temporary Python files"

# Run the game
run: check
	@echo "$(BLUE)Starting Game...$(RESET)"
	$(PYTHON) $(MAIN_SCRIPT)

# Run the 50-test suite
# Note: 'xvfb-run' allows UI tests to run in GitHub Codespaces without a monitor
test: check
	@echo "$(BLUE)Running 50-test suite...$(RESET)"
	@if command -v xvfb-run > /dev/null; then \
		xvfb-run $(PYTHON) -m unittest discover $(TEST_DIR); \
	else \
		$(PYTHON) -m unittest discover $(TEST_DIR); \
	fi

# Verify File Integrity
check:
	@echo "$(BLUE)Verifying project structure...$(RESET)"
	@if [ ! -f $(MAIN_SCRIPT) ]; then echo "$(RED)Error: $(MAIN_SCRIPT) missing$(RESET)"; exit 1; fi
	@if [ ! -f $(LOGIC_SCRIPT) ]; then echo "$(RED)Error: $(LOGIC_SCRIPT) missing$(RESET)"; exit 1; fi
	@if [ ! -f $(DATA_FILE) ]; then echo "$(RED)Error: $(DATA_FILE) missing$(RESET)"; exit 1; fi
	@if [ ! -d $(TEST_DIR) ]; then echo "$(RED)Error: $(TEST_DIR) directory missing$(RESET)"; exit 1; fi
	@echo "$(GREEN)Integrity Check Passed.$(RESET)"

# Cleanup temporary files
clean:
	@echo "$(BLUE)Cleaning workspace...$(RESET)"
	rm -rf __pycache__
	rm -rf $(TEST_DIR)/__pycache__
	rm -rf *.pyc
	@echo "$(GREEN)Cleanup complete.$(RESET)"