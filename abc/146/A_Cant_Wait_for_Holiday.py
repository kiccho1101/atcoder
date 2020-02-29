yobis = {"MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6, "SUN": 7}
S = input()
print(7 if yobis["SUN"] - yobis[S] == 0 else yobis["SUN"] - yobis[S])

