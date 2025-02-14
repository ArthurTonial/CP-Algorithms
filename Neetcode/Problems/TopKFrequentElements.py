# https://neetcode.io/problems/top-k-elements-in-list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        arr = []
        for n, freq in count.items():
            arr.append([freq, n])
        arr.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(arr[i].second)
        return ans   