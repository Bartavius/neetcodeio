import pytest
import sys
from pathlib import Path

# Add parent directory to path so we can import solutions
sys.path.insert(0, str(Path(__file__).parent.parent))

@pytest.fixture
def large_input():
    """Generate large inputs for performance testing."""
    return {
        "large_array": list(range(10000)),
        "large_string": "a" * 10000,
        "worst_case_array": [1] * 10000,
    }