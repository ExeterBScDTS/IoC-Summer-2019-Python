# mow.py
#
# Print the children's song : Went to mow a meadow
#

mowers=3

for m in range(mowers):
    print(m+1, "men went to mow")
    print("went to mow a meadow")
    
    for n in range(m+1):
        print((m+1)-n, "men, ", end="")
    
    print("and his dog")
    print("went to mow a meadow")
    print("")
