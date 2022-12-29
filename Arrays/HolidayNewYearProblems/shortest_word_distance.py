'''
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list.

Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
'''
def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
    dist = len(wordsDict)
    idx1 = -1
    idx2 = -1
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            idx1 = i
        elif wordsDict[i] == word2:
            idx2 = i

        if idx1 >= 0 and idx2 >= 0:
            if abs(idx2 - idx1) < dist:
                dist = abs(idx2 - idx1)

    return dist if idx1 >= 0 and idx2 >= 0 else 0