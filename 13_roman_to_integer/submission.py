        
class Solution(object):
    def romanToInt(self, s):
        import re
        
        numeral = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        open_list = list(s.strip().upper())
        
        if not 1 <= len(open_list) <= 15:
            raise Exception("Invalid input!")
        
        pattern = r"^[MDCLXVI]*$"
        
        if not re.match(pattern, s.strip().upper()):
            raise Exception("Input contains illegal characters, please only "
                            "use Roman numerals M, D, C, L, X, V, I"
            )
            
        # only M X C I can be x2 and x3        
        multis = {"M", "C", "X", "I"}
        
        # only 6 legal subraction pairs: 
        legal_subs = ("IV", "IX", "XL", "XC", "CD", "CM")
        
        closed_list = []      
        i = 0
        
        while i < len(open_list):
            if len(open_list) > 1:
                
                # deal with pairs from right to left
                first = open_list.pop()
                second = open_list.pop()
                
                # simplist operation; small number follows larger number
                if numeral[second] > numeral[first]:
                    closed_list.append(numeral[first])
                    open_list.append(second)
                    
                # multiples of the same char
                elif first == second and first in multis:
                    if len(open_list) == 0:
                        closed_list.extend([numeral[first], numeral[second]])
                    else:
                        third = open_list.pop()
                        if first == third: # this is the last legal multiple char we can tolerate.
                            if len(open_list) == 0:
                                closed_list.extend([numeral[first], numeral[second], numeral[third]])
                            else:
                                fourth = open_list.pop()
                                if numeral[fourth] > numeral[first]:
                                    closed_list.extend([numeral[first], numeral[second], numeral[third]])
                                    open_list.append(fourth)
                                else:
                                    raise Exception("Invalid input!")

                        elif numeral[first] < numeral[third]: # convert duo and return legal third
                            closed_list.extend([numeral[first], numeral[second]])
                            open_list.append(third)
                        else:
                            raise Exception("Invalid input!") # Reject e.g. IXX
                    
                # small number followed by large number e.g. "IX" (good) or "IL" (bad)
                else: # numeral[second] < numeral[first]
                    if not str(second+first) in legal_subs:
                        raise Exception("Invalid input!") # Reject e.g. IL
                    if len(open_list) == 0:
                        subbed_value = numeral[first] - numeral[second]
                        closed_list.append(subbed_value)
                    else:
                        third = open_list.pop()
                        if numeral[third] < numeral[first]:
                            raise Exception("Invalid input!")
                        elif third == first == "M":
                            pass
                        subbed_value = numeral[first] - numeral[second]
                        closed_list.append(subbed_value)
                        open_list.append(third)
            else:
                # deal with single item
                first = open_list.pop()
                closed_list.append(numeral[first])

        r = sum(closed_list)

        if r > 3999:
            raise Exception("Number too big!")
            
        else:
            return r
