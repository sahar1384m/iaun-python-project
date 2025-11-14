class MyStringLibrary:
    # Convert the first letter to uppercase and the rest to lowercase
    def mycaptilize(s):
      result = ""
      for i in range(len(s)):
        if i == 0:
            ch = s[i]
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            else:
                result += ch
        else:
            ch = s[i]
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch
      return result
        
    # Convert all text to case-insensitive
    def mycasefold(s):
        result = ""
        for ch in s:
          if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
          else:
            result += ch
        return result

    # Count the number of occurrences of a substring
    def mycount(s, sub):
      count = 0
      for i in range(len(s) - len(sub) + 1):
        match = True
        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            count += 1
      return count

    # Does the string end with a substring?
    def myendswith(s, sub):
     if len(sub) > len(s):
        return False

     for i in range(len(sub)):
        if s[len(s) - len(sub) + i] != sub[i]:
            return False
     return True

    # Find the first place
    def myfind(s, sub):
     for i in range(len(s) - len(sub) + 1):
        match = True
        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
     return -1

    # Like a find, but if it wasn't there, it would give an error.
    def myindex(s, sub):
     pos = myfind(s, sub)
     if pos == -1:
        raise ValueError("substring not found!")
     return pos

    # Are all characters digits?
    def myisdigit(s):
     if len(s) == 0:
        return False

     for ch in s:
        if not ('0' <= ch <= '9'):
            return False
     return True

    # Are all letters lowercase?
    def myislower(s):
     found = False
     for ch in s:
        if 'A' <= ch <= 'Z':
            return False
        if 'a' <= ch <= 'z':
            found = True
     return found

    # Are all letters isupper?
    def myisupper(s):
     found = False
     for ch in s:
        if 'a' <= ch <= 'z':
            return False
        if 'A' <= ch <= 'Z':
            found = True
     return found

    # Remove leading and trailing spaces
    def mystrip(s):
     start = 0
     end = len(s) - 1
     while start <= end and s[start] == ' ':
        start += 1
     while end >= start and s[end] == ' ':
        end -= 1
     result = ""
     for i in range(start, end + 1):
        result += s[i]
     return result

    # Remove spaces on the right
    def myrstrip(s):
     end = len(s) - 1
     while end >= 0 and s[end] == ' ':
        end -= 1
     return s[:end+1]

    # Remove spaces on the left
    def mylstrip(s):
     start = 0
     while start < len(s) and s[start] == ' ':
        start += 1
     return s[start:]

    # Switch lowercase ↔ uppercase letters
    def myswapcase(s):
     result = ""
     for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
     return result

    # Substring replacement
    def myreplace(s, old, new):
     result = ""
     i = 0
     while i < len(s):
        match = True
        for j in range(len(old)):
            if i + j >= len(s) or s[i + j] != old[j]:
                match = False
                break

        if match:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
     return result

    
