class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[[strs[0]]]


        for data in strs[1:]:
            print(data)
            flag=False
            for i in range(len(output)):
                tempData = output[i][0]
                print(sorted(tempData), sorted(data))
                if sorted(tempData) == sorted(data):
                    output[i].append(data)
                    flag=True
                    break
            if flag==False:
                output.append([data])

            print(f'output={output}')

        return output
            