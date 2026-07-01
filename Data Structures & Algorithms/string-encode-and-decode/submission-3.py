class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""

        for word in strs:
            result+=str(len(word))
            result+="#"
            result+=word

        return result    

    def decode(self, string: str) -> List[str]:
        result=[]
        i=0

        while i < len(string):
            j=i
            while string[j]!="#":
                j=j+1
            length= int(string[i:j])
            word=string[j+1:j+1+length]

            result.append(word)
            i=j+1+length
        return result

        


