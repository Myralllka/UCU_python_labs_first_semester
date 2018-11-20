a = [i for i in range(10)]
print(a)

b = []
for i in range(10):
    b.append(i)

print(b)

a = [(i*100) for i in range(20) if i%5 == 0]
print(a)
  
b = []
for i in range(20):
    if i%5 == 0:
        b.append(i*100)

print(b)
sent = '''As the food crisis grows worse for Baghili and other Yemenis,  \
          the UN World Food Programme fears the devastating toll that \
          hunger could have on the war-torn country'''
print([len(w) for w in sent.split() if w.startswith('A') or w.endswith("r")] )
