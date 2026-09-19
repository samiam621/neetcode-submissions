class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str=""
        code='#'
        #.  5#Hello5#World
        for word in strs:
            length=len(word)
            new_str= f'{new_str}{length}{code}{word}' 
        return new_str


    def decode(self, s: str) -> List[str]:
        #.    '5#Hello5#World'
        new_lst=[]
        start,end,i = 0,0,0
        length = ''
        code='#'
        while s:
            #what if length is two or three digit
            length = s[:s.find(code)]
            start= len(length) + len(code)
            length = int(length)

            end = start + length
            word=s[start:end]
            new_lst.append(word)

            s=s[end:]

        return new_lst
            
            
