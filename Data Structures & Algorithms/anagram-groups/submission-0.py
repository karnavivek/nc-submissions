class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            grouped[key].append(i)
        return list(grouped.values())