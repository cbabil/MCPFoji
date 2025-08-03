# Makefile for MCPFoji
.PHONY: help install clean run dev test venv-create venv-activate

# Variables
VENV_NAME := venv
VENV_DIR := $(VENV_NAME)
PYTHON := python3
PIP := $(VENV_DIR)/bin/pip
PYTHON_VENV := $(VENV_DIR)/bin/python
SRC_DIR := src
MAIN_FILE := $(SRC_DIR)/main.py

# Colors for output
RED := \033[31m
GREEN := \033[32m
YELLOW := \033[33m
BLUE := \033[34m
RESET := \033[0m

# Default target
help: ## Show this help message
	@echo "$(BLUE)MCPFoji - Available targets:$(RESET)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(RESET) %s\n", $$1, $$2}'

# Check if virtual environment exists
check-venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "$(YELLOW)Virtual environment not found. Creating...$(RESET)"; \
		$(MAKE) venv-create; \
	fi

# Create virtual environment
venv-create: ## Create a new virtual environment
	@echo "$(BLUE)Creating virtual environment...$(RESET)"
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "$(GREEN)Virtual environment created successfully!$(RESET)"

# Install dependencies
install: check-venv ## Install dependencies in virtual environment
	@echo "$(BLUE)Installing dependencies...$(RESET)"
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)Dependencies installed successfully!$(RESET)"

# Setup development environment
setup: venv-create install ## Setup complete development environment
	@echo "$(GREEN)Development environment setup complete!$(RESET)"
	@echo "$(YELLOW)To activate the virtual environment manually, run:$(RESET)"
	@echo "  source $(VENV_DIR)/bin/activate"

# Run the application
run: check-venv ## Run the application with default arguments
	@echo "$(BLUE)Starting MCPFoji application...$(RESET)"
	$(PYTHON_VENV) $(MAIN_FILE)

# Run with custom arguments (use like: make run-with ARGS="--host 0.0.0.0 --port 8080")
run-with: check-venv ## Run the application with custom arguments (use ARGS="...")
	@echo "$(BLUE)Starting MCPFoji application with args: $(ARGS)$(RESET)"
	$(PYTHON_VENV) $(MAIN_FILE) $(ARGS)

# Development mode (with more verbose output)
dev: check-venv ## Run in development mode
	@echo "$(BLUE)Starting MCPFoji in development mode...$(RESET)"
	$(PYTHON_VENV) $(MAIN_FILE) --transport stdio

# Clean virtual environment
clean: ## Remove virtual environment and cached files
	@echo "$(YELLOW)Cleaning up...$(RESET)"
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "$(GREEN)Cleanup complete!$(RESET)"

# Reinstall everything
reinstall: clean setup ## Clean and reinstall everything
	@echo "$(GREEN)Reinstallation complete!$(RESET)"

# Show virtual environment status
status: ## Show virtual environment and dependency status
	@echo "$(BLUE)Virtual Environment Status:$(RESET)"
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "  $(GREEN)✓$(RESET) Virtual environment exists"; \
		echo "  $(BLUE)Python version:$(RESET) $$($(PYTHON_VENV) --version)"; \
		echo "  $(BLUE)Pip version:$(RESET) $$($(PIP) --version)"; \
		echo "  $(BLUE)Installed packages:$(RESET)"; \
		$(PIP) list; \
	else \
		echo "  $(RED)✗$(RESET) Virtual environment not found"; \
		echo "  Run '$(GREEN)make setup$(RESET)' to create it"; \
	fi

# Show application help
app-help: check-venv ## Show application help/usage
	@echo "$(BLUE)MCPFoji Application Help:$(RESET)"
	$(PYTHON_VENV) $(MAIN_FILE) --help

# Test if the application can start (quick validation)
test: check-venv ## Test if the application can start
	@echo "$(BLUE)Testing application startup...$(RESET)"
	@if $(PYTHON_VENV) -c "import sys; sys.path.append('$(SRC_DIR)'); from main import main; print('✓ Application imports successfully')"; then \
		echo "$(GREEN)✓ Application test passed!$(RESET)"; \
	else \
		echo "$(RED)✗ Application test failed!$(RESET)"; \
		exit 1; \
	fi

# Install in development mode (editable install)
dev-install: check-venv ## Install in development mode
	@echo "$(BLUE)Installing in development mode...$(RESET)"
	$(PIP) install -e .
	@echo "$(GREEN)Development installation complete!$(RESET)"
