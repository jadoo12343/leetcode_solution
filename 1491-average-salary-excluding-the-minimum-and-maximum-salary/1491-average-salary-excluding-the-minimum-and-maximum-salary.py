class Solution:
    def average(self, salary: List[int]) -> float:
        avg = (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
        return avg
        