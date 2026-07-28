class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        new_list=salary[1:-1]
        n=len(new_list)
        if n<2:
            return new_list[0]
        else:
            return sum(new_list)/n
        