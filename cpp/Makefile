# Makefile for LeetCode C++ Testing with Google Test

# Compiler settings
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g
LDFLAGS = -L/opt/homebrew/lib
LDLIBS = -lgtest -lgtest_main -pthread
INCLUDES = -I/opt/homebrew/include -I.

# Coverage flags (detect compiler)
ifeq ($(shell $(CXX) --version | grep -c "clang"),1)
    # Clang/LLVM coverage flags
    COVERAGE_FLAGS = -fprofile-instr-generate -fcoverage-mapping
    COVERAGE_LDFLAGS = -fprofile-instr-generate
    COVERAGE_TOOL = llvm-cov
else
    # GCC coverage flags
    COVERAGE_FLAGS = -fprofile-arcs -ftest-coverage
    COVERAGE_LDFLAGS = -lgcov
    COVERAGE_TOOL = gcov
endif

# Colors for output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
NC = \033[0m # No Color

# Default target (if no target specified)
default: help

# Find all test files
TEST_SOURCES = $(wildcard test/test_*.cpp)
TEST_TARGETS = $(patsubst test/test_%.cpp,build/test_%,$(TEST_SOURCES))
COVERAGE_TARGETS = $(patsubst test/test_%.cpp,build/coverage_%,$(TEST_SOURCES))

# Build directory
BUILDDIR = build
COVERAGEDIR = coverage

# Create build directories
$(BUILDDIR):
	@mkdir -p $(BUILDDIR)

$(COVERAGEDIR):
	@mkdir -p $(COVERAGEDIR)

# Generic rule to build any test
build/test_%: test/test_%.cpp solutions/%.cpp | $(BUILDDIR)
	@echo "$(GREEN)Building test: $@$(NC)"
	$(CXX) $(CXXFLAGS) $(INCLUDES) $^ $(LDFLAGS) $(LDLIBS) -o $@

# Generic rule to build any test with coverage
build/coverage_%: test/test_%.cpp solutions/%.cpp | $(BUILDDIR)
	@echo "$(GREEN)Building test with coverage: $@$(NC)"
	$(CXX) $(CXXFLAGS) $(COVERAGE_FLAGS) $(INCLUDES) $^ $(LDFLAGS) $(LDLIBS) $(COVERAGE_LDFLAGS) -o $@

# Build all tests
all: $(TEST_TARGETS)
	@echo "$(GREEN)All tests built successfully!$(NC)"

# Run a specific test
run-%: build/test_%
	@echo "$(YELLOW)Running test: $<$(NC)"
	@./$< --gtest_color=yes

# Run a specific test with coverage
coverage-%: build/coverage_% | $(COVERAGEDIR)
	@echo "$(YELLOW)Running test with coverage: $*$(NC)"
ifeq ($(COVERAGE_TOOL),llvm-cov)
	@# LLVM/Clang coverage
	@rm -f build/$*.profraw
	@LLVM_PROFILE_FILE="build/$*.profraw" ./build/coverage_$* --gtest_color=yes
	@echo ""
	@echo "$(BLUE)Generating coverage report for $*...$(NC)"
	@xcrun llvm-profdata merge -sparse build/$*.profraw -o build/$*.profdata
	@xcrun llvm-cov show ./build/coverage_$* -instr-profile=build/$*.profdata solutions/$*.cpp > $(COVERAGEDIR)/$*_coverage.txt
	@xcrun llvm-cov report ./build/coverage_$* -instr-profile=build/$*.profdata solutions/$*.cpp
else
	@# GCC coverage
	@rm -f build/*.gcda
	@./build/coverage_$* --gtest_color=yes
	@echo ""
	@echo "$(BLUE)Generating coverage report for $*...$(NC)"
	@gcov -r solutions/$*.cpp -o build/ > /dev/null 2>&1
	@mv *.gcov $(COVERAGEDIR)/ 2>/dev/null || true
	@echo "$(GREEN)Coverage Summary:$(NC)"
	@grep -A 2 "File 'solutions/$*.cpp'" $(COVERAGEDIR)/$*.cpp.gcov || echo "No coverage data found"
endif
	@echo ""
	@echo "$(YELLOW)Detailed coverage report in: $(COVERAGEDIR)/$(NC)"

# Run all tests with coverage
coverage-all: | $(COVERAGEDIR)
	@echo "$(YELLOW)Running all tests with coverage...$(NC)"
	@# Clean previous coverage data
	@rm -f build/*.gcda build/*.gcno
	@rm -rf $(COVERAGEDIR)/*
	@# Build all tests with coverage
	@for test in $(TEST_SOURCES); do \
		name=$$(basename $$test .cpp | sed 's/test_//'); \
		echo "$(GREEN)Building coverage for $$name$(NC)"; \
		$(MAKE) -s build/coverage_$$name; \
	done
	@# Run all tests
	@for test in $(TEST_SOURCES); do \
		name=$$(basename $$test .cpp | sed 's/test_//'); \
		echo "$(GREEN)Running $$name$(NC)"; \
		./build/coverage_$$name --gtest_color=yes || exit 1; \
		echo ""; \
	done
	@# Generate coverage report
	@echo "$(BLUE)Generating coverage reports...$(NC)"
	@for src in solutions/*.cpp; do \
		gcov -r $$src -o build/ > /dev/null 2>&1; \
	done
	@mv *.gcov $(COVERAGEDIR)/ 2>/dev/null || true
	@# Generate HTML report if lcov is available
	@if command -v lcov &> /dev/null; then \
		echo "$(BLUE)Generating HTML coverage report...$(NC)"; \
		lcov --capture --directory build --output-file $(COVERAGEDIR)/coverage.info --no-external > /dev/null 2>&1; \
		genhtml $(COVERAGEDIR)/coverage.info --output-directory $(COVERAGEDIR)/html > /dev/null 2>&1; \
		echo "$(GREEN)HTML coverage report generated: $(COVERAGEDIR)/html/index.html$(NC)"; \
	fi

# Generate HTML coverage report using lcov
coverage-html: coverage-all
	@if command -v lcov &> /dev/null; then \
		echo "$(BLUE)Opening HTML coverage report...$(NC)"; \
		open $(COVERAGEDIR)/html/index.html 2>/dev/null || xdg-open $(COVERAGEDIR)/html/index.html 2>/dev/null || echo "Please open $(COVERAGEDIR)/html/index.html manually"; \
	else \
		echo "$(RED)lcov not found. Install it to generate HTML reports:$(NC)"; \
		echo "  macOS: brew install lcov"; \
		echo "  Ubuntu: sudo apt-get install lcov"; \
	fi

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
	@rm -rf $(COVERAGEDIR)
	@rm -f *.gcov *.gcda *.gcno
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
	@echo "  make coverage-<name>    - Run specific test with coverage"
	@echo "  make coverage-all       - Run all tests with coverage"
	@echo "  make coverage-html      - Generate and open HTML coverage report"
	@echo "  make list               - List all available tests"
	@echo "  make clean              - Remove all build files"
	@echo ""
	@echo "$(BLUE)Coverage Reports:$(NC)"
	@echo "  Text reports: coverage/*.gcov"
	@echo "  HTML reports: coverage/html/index.html (requires lcov)"

.PHONY: all test clean list help default coverage-all coverage-html