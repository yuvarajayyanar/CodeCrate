class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mi=float('inf')

        
        result=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    k = i + j
                    if k < mi:
                        mi = k
                        result = [list1[i]]
                    elif k == mi:
                        result.append(list1[i])
        return result
