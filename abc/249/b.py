S = input()
st = set()

is_upper = False
is_lower = False
no_dup = True
for s in S:
    if s.isupper():
        is_upper = True
    if s.islower():
        is_lower = True
    if s in st:
        no_dup = False
    st.add(s)

if is_upper and is_lower and no_dup:
    print("Yes")
else:
    print("No")
