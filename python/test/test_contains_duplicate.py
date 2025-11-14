import pytest
from contains_duplicate import ContainsDuplicate

class TestContainsDuplicate:
    """
    Test cases for Contains Duplicate problem. This was a generated
    file using AI so that I can use it as a template for my future tests
    """
    
    @pytest.fixture
    def solution(self):
        return ContainsDuplicate()
    
    def test_basic_cases(self, solution):
        """Test basic examples."""
        # Example 1: nums = [1,2,3,1] -> true
        assert solution.contains_duplicate([1,2,3,1]) == True
        
        # Example 2: nums = [1,2,3,4] -> false
        assert solution.contains_duplicate([1,2,3,4]) == False
        
        # Example 3: nums = [1,1,1,3,3,4,3,2,4,2] -> true
        assert solution.contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True
    
    def test_edge_cases(self, solution):
        """Test edge cases."""
        # Empty array
        assert solution.contains_duplicate([]) == False
        
        # Single element
        assert solution.contains_duplicate([1]) == False
        
        # Two elements - same
        assert solution.contains_duplicate([1,1]) == True
        
        # Two elements - different
        assert solution.contains_duplicate([1,2]) == False
        
        # All elements same
        assert solution.contains_duplicate([5,5,5,5,5]) == True
        
        # Negative numbers
        assert solution.contains_duplicate([-1,-1,-2,-3]) == True
        assert solution.contains_duplicate([-1,-2,-3,-4]) == False
    
    @pytest.mark.parametrize("nums,expected", [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True),
        ([], False),
        ([1], False),
        ([0,0], True),
        ([-1,-2,-3], False),
        ([1,2,3,4,5,6,7,8,9,10], False),
        ([10,9,8,7,6,5,4,3,2,1,1], True),
    ])
    def test_multiple_cases(self, solution, nums, expected):
        """Test multiple cases with parametrize."""
        assert solution.contains_duplicate(nums) == expected
    
    @pytest.mark.array
    @pytest.mark.slow
    def test_performance_worst_case(self, solution):
        """Test with large input - worst case (no duplicates)."""
        # Maximum constraint: 10^5 unique elements
        nums = list(range(100000))
        assert solution.contains_duplicate(nums) == False
    
    @pytest.mark.array
    @pytest.mark.slow
    def test_performance_best_case(self, solution):
        """Test with large input - best case (immediate duplicate)."""
        nums = [1, 1] + list(range(2, 100000))
        assert solution.contains_duplicate(nums) == True
    
    @pytest.mark.benchmark
    def test_benchmark(self, benchmark, solution):
        """Benchmark the solution."""
        nums = [1,2,3,4,5,6,7,8,9,10]
        result = benchmark(solution.contains_duplicate, nums)
        assert result == False