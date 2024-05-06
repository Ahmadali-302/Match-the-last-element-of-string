def end_other():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    str1_con = str1.lower()
    str2_con = str2.lower()
    if str1_con[-1] == str2_con[-1]:
        return True
    else:
        return False


abj = end_other()
print(abj)
