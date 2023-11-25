class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_dict = dict(Counter(arr))
        filtered_dict = {k:v for k, v in arr_dict.items() if v == 1}
        arri = list(filtered_dict.keys())
        if len(arri) < k:
            return ""
        return arri[k-1]