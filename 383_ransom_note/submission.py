"""
Given two strings ransomNote and magazine, return true if ransomNotecan be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        magazine_list = list(magazine)
        
        for letter in ransomNote:
            try:
                magazine_list.pop(magazine_list.index(letter))
            
            except ValueError:
                return False
                
        return True
            
