from hashlib import md5
from hashlib import sha256
from hashlib import sha512
s="anas is the best boy in the world"
result_md5=md5(s.encode())
result_sha256=sha256(s.encode())
result_sha512=sha512(s.encode())
print(result_md5.hexdigest())
print(result_sha256.hexdigest())
print(result_sha512.hexdigest())
