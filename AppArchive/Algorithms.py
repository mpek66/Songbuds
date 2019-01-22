#finds the index of a member of a sorted list or returns -1
def binary_search(target, ll):
    lb = 0
    ub = len(ll)-1
    searching = True
    while searching:
        m = (lb+ub)//2
        if target == ll[m]: #found it
            return m
        elif target > ll[m]: #if midpoint too low
            lb = m + 1
        elif target < ll[m]: #if midpoint too high
            ub = m
        elif lb == ub: #if searching an empty list
            searching = False
    return -1 #target not found

#merges two lists into a list of similar elements
#assumes the two lists have unique elements
def merge(a, b):
    ai = 0
    bi = 0
    result = []
    going = True
    while going:
        if ai >= len(a):
            going = False
        elif bi >= len(b):
            going = False
        elif a[ai] == b[bi]:
            result.append(a[ai])
            ai += 1
            bi += 1
        elif a[ai] > b[bi]:
            bi += 1
        elif a[ai] < b[bi]:
            ai += 1
    return result

#given a user list, calculates and returns a list of song ids
def algorithm_v1(UL):
    #a dictionary to track all shared songs
    shared = {}
    fix = 0
    while fix < len(UL.users):
        six = fix + 1
        while six < len(UL.users):
            a = UL.users[fix].songs
            b = UL.users[six].songs
            subshared = merge(a,b)
            for song in subshared:
                shared[song] = shared.get(song, 0) + 1
            six += 1
        fix += 1
    #most times one song occurs
    max_occur = max(list(shared.values()))
    #final list of songs
    result = []
    for num_occur in range(max_occur, 0, -1):
        for song in shared:
            if shared[song] == num_occur:
                result.append(song)
    return result
