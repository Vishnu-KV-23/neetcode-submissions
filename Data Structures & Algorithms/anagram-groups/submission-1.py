class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for i in strs:

            #print("Sorted:","".join(sorted(i)))
            if "".join(sorted(i)) in output:
                output["".join(sorted(i))].append(i)
            else:
                k=[]
                k.append(i)
                output["".join((sorted(i)))] =k

        return list(output.values())

        