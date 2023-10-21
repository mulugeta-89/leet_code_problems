class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = [chr(ord('a') + i) for i in range(26)]
        alphabet = set(alphabet)
        sentence = set(sentence)
        if alphabet.issubset(sentence):
            return True
        return False
        
                    
        