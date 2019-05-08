import hashlib

str = '123456'
md5_str = hashlib.md5(str.encode())
print(md5_str.hexdigest())

# 加盐
salt = '@#$%'
password = '123456'
password += salt

md5_password = hashlib.md5(password.encode())
