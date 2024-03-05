class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def process_string(string):
            result = []
            for char in string:
                if char == '#':
                    if result:
                        result.pop()
                else:
                    result.append(char)
            return ''.join(result)

        return process_string(s) == process_string(t)
