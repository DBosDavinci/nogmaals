dagen = "ma", "di", "wo", "do", "vr", "za", "zo"
vraag = input("Welke dag van de week kiest u? {} ".format(dagen))
i=0
while i < dagen.index(vraag)+1:
    print(dagen[i])
    i+=1