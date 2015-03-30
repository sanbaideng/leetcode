class Solution:
    # @return a tuple, (index1, index2)
    
    
    def twoSum(self, num, target):
        l=[]
        for i in range(0,len(num)):
            if num[i]<target:
                l.append(i)
        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                if num[l[i]]+num[l[j]]==target:
                    t=(l[i],l[j])
                    return t

s = Solution()
t=s.twoSum((1,2,3,4,5),9)
print(t)
