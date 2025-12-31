def subset_sum(a,s):
    if s == 0: return True
    if not a: return False
    return subset_sum(a[1:],s) or subset_sum(a[1:],s-a[0])

print(subset_sum([3,34,4,12,4,2],9))