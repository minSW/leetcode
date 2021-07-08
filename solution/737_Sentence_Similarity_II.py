class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2) : 
            return False
        
        i = 0
        linked, words = list(), dict()

        while similarPairs :
            a, b = similarPairs.pop()
            if not a in words and not b in words :
                words[a] = words[b] = i
                i += 1
            elif not a in words :
                words[a] = words[b]
            elif not b in words :
                words[b] = words[a]
            elif words[a] != words[b] :
                link_set = [ link for link in linked if words[a] in link or words[b] in link ]
                if link_set :
                    link_set[0].add(words[a])
                    link_set[0].add(words[b])
                else :
                    linked.append(set([words[a], words[b]]))
        
        for w1, w2 in zip(sentence1, sentence2) :
            if w1 == w2 : 
                continue
            elif not w1 in words or not w2 in words :
                return False
            
            if words[w1] != words[w2] : 
                link_set = [ link for link in linked if words[w1] in link and words[w2] in link ]
                if not link_set :
                    return False
        
        return True
