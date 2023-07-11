def scan_to_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(scan_to_palindrome('шалаш'))