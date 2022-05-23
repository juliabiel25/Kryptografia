import Crypto.Cipher import AES

aes = AES.new(key, AES.MODE_CBC, iv)
data = 'hello world 1234' # <- 16 bytes
encd = aes.encrypt(data)