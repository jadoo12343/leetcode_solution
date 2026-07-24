class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        expected_diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            current_diff = arr[i+1] - arr[i]
            if current_diff != expected_diff:
                return False
        return True

        