def check(s1,s2):
# the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("are anagrams.")
    else:
        print(" aren't anagrams.")        
s1 = input("Enter the first string: ")
s2 = input("Enter the first string:")
check(s1, s2)