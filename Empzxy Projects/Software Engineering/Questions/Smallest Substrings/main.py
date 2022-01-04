import collections 
def longest(input, chars):
    counts = collections.Counter(chars)
    st = 0 
    def isValid():
        return not any(counts.values())
    
    while input[st] not in counts: st+=1

    end = st 
    out = ""

    while end < len(input):
        if input[end] in counts:
            counts[input[end]]-=1
            if isValid():
                subStr = input[st:end+1]
                if not out:
                    out = subStr
                elif len(subStr) < len(out):
                    out = subStr
                st+1
                counts[input[st]]+=1
                while input[st] not in counts:
                    st+1 

                return out
                