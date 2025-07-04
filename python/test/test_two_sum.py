import pytest
from two_sum import TwoSum

class TestTwoSum:

    # CONSTRAINT:
    # You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
    # array is not sorted by default either
    # nums[i] + nums[j] == target and i != j
    # only integers in nums array

    @pytest.fixture
    def solution(self):
        return TwoSum()
    
    def test_basic_cases(self, solution):
        # only one solution
        assert solution.two_sum([1, 0, 3, 4, 5], 6) == [0, 4]
        assert solution.two_sum([3, 1, 4, 5], 6) == [1, 3] 

        # no solutions
        assert solution.two_sum([0, 0, 0, 0], 1) == []

        # one solution that uses two of the same numbers
        assert solution.two_sum([5, 5], 10) == [0, 1]

    def test_edge_cases(self, solution):
        # not enough inputs
        assert solution.two_sum([1], 0) == []
        
        # even with one number returning target, it is an invalid solution
        assert solution.two_sum([0], 0) == []

        # target is 0 and answers are zeros
        assert solution.two_sum([0, 5, 0], 0) == [0, 2]

        # negative numbers
        assert solution.two_sum([-2, 15, 100, -6, -25], 75) == [2, 4]
        assert solution.two_sum([-20, -10, 0, 4, -6], 100) == []

    # performance testing
    @pytest.mark.array
    @pytest.mark.slow
    def test_performance_worst_case(self, solution):
        """Test with large input - worst case (no sums)."""
        # Maximum constraint: 10^5 unique elements
        nums = list(range(100000))
        assert solution.two_sum(nums, -1) == []
    
    @pytest.mark.array
    @pytest.mark.slow
    def test_performance_best_case(self, solution):
        """Test with large input - best case (sorted, two sum are at the 0 and -1 index)."""
        nums = list(range(0, 100000))
        assert solution.two_sum(nums, 99999) == [0, 99999]
    
    @pytest.mark.benchmark
    def test_benchmark(self, benchmark, solution):
        """Benchmark the solution."""
        nums = list(range(1, 11))
        target = 1
        result = benchmark(solution.two_sum, nums, target)
        assert result == []

