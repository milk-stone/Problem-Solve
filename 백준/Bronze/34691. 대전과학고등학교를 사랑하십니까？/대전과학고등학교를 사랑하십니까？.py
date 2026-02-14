while True:
    s = input().strip()
    if s == "end":
        break
    ans = ""
    if s == "animal":
        ans = "Panthera tigris"
    elif s == "tree":
        ans = "Pinus densiflora"
    else:
        ans = "Forsythia koreana"
        
    print(ans)