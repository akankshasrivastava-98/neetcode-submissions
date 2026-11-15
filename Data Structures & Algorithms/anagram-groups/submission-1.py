class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict={}
        res = []
        # if len(strs)==0:
        #     return [""]
        # if len(strs) == 1:
        #     return [strs]
        # for s in strs:
        #     comp = ''.join(sorted(s, reverse=False))
        #     if comp in anagramDict:
        #         temp = anagramDict[comp]
        #         temp.append(s)
        #         anagramDict[comp] = temp
        #     else:
        #         anagramDict[comp] = [s]
        # for k,v in anagramDict.items():
        #     res.append(v)
        # return res
        for s in strs:

            count = [0]*26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)

            if key not in anagramDict:
                anagramDict[key] = []

            anagramDict[key].append(s)

        return list(anagramDict.values())

        

                

        