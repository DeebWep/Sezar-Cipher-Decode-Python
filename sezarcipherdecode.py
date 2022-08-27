"""DECODER BY MAGA"""
ciphercharsen_A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphercharsen_a = "abcdefghijklmnopqrstuvwxyz"
ciphertext = input("Enter Cipher Text:\n")
key = int(input("Enter Key Number: "))
textready = []
text = ""
for i in ciphertext:
    textready.append(i)

for j in textready:
    if j.isalpha():
        if j.isupper():
            k = ciphercharsen_A.index(j)
            k-=key
            if k <0:
                k=26+k
            text += ciphercharsen_A[k]
        if j.islower():
            k = ciphercharsen_a.index(j)
            k-=key
            if k<0:
                k=26+k
            text +=ciphercharsen_a[k]
    else:
        text += j
print("Cipher Text: ",text)

