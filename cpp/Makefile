# Makefile for LeetCode C++ Testing with Google Test

# Compiler settings
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g
LDFLAGS = -L/opt/homebrew/lib
LDLIBS = -lgtest -lgtest_main -pthread
INCLUDES = -I/opt/homebrew/include -I.

# Colors for output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
NC = \033[0m # No Color

# Default target (if no target specified)
default: help

# Find all test files
TEST_SOURCES = $(wildcard test/test_*.cpp)
TEST_TARGETS = $(patsubst test/test_%.cpp,build/test_%,$(TEST_SOURCES))

# Build directory
BUILDDIR = build

# Create build directory
$(BUILDDIR):
	@mkdir -p $(BUILDDIR)

# Generic rule to build any test
build/test_%: test/test_%.cpp | $(BUILDDIR)
	@echo "$(GREEN)Building test: $@$(NC)"
	$(CXX) $(CXXFLAGS) $(INCLUDES) $< $(LDFLAGS) $(LDLIBS) -o $@

# Build all tests
all: $(TEST_TARGETS)
	@echo "$(GREEN)All tests built successfully!$(NC)"

# Run a specific test
run-%: build/test_%
	@echo "$(YELLOW)Running test: $<$(NC)"
	@./$< --gtest_color=yes

# Run all tests
test: all
	@echo "$(YELLOW)Running all tests...$(NC)"
	@for test in $(TEST_TARGETS); do \
		echo "$(GREEN)Running $$test$(NC)"; \
		$$test --gtest_color=yes || exit 1; \
		echo ""; \
	done

# Clean build files
clean:
	@echo "$(RED)Cleaning build files...$(NC)"
	@rm -rf $(BUILDDIR)
	@echo "$(GREEN)Clean complete!$(NC)"

# List all available tests
list:
	@echo "$(YELLOW)Available tests:$(NC)"
	@for test in $(TEST_SOURCES); do \
		name=$$(basename $$test .cpp | sed 's/test_//'); \
		echo "  - $$name"; \
	done

# Help message
help:
	@echo "$(YELLOW)LeetCode C++ Testing Makefile$(NC)"
	@echo ""
	@echo "$(GREEN)Usage:$(NC)"
	@echo "  make all                - Build all tests"
	@echo "  make test               - Build and run all tests"
	@echo "  make run-<name>         - Build and run specific test"
	@echo "  make list               - List all available tests"
	@echo "  make clean              - Remove all build files"

.PHONY: all test clean list help default