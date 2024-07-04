import hashlib
m = hashlib.new("md5")
input = "yzbqklnj"
validation = False
num = 1
while validation == False:
    hash = input + str(num)
    m.update(hash)
    hash_encoded = m.hexdigest()
    if hash_encoded[0:4] == 00000:
        validation = True
    else:
        num += 1
print(num)
