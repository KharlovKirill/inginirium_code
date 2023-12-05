def csb(cs):
    i,o = 0, 0
    while i < len(cs) and o>=0:
        if "(" == cs[i]:
            o += 1
        else:
            o -= 1
        i += 1
    if 0 == o:
        print("YES")
    else:
        print("NO")

csb("())(()")