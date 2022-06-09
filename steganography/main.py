import cv2
import math
from bitarray import bitarray
from bitarray.util import int2ba, ba2int

img = cv2.imread('benio.jpg', cv2.IMREAD_COLOR)

# max number of bytes to hide in an image:
max_len = math.floor(img.shape[0] * img.shape[1] * img.shape[2] / 8)
print(f'max length of hidden message: {max_len}')

secret = b'Pies na horyzoncie - powtarzam - pies na horyzoncie'
secret_bitarray = bitarray()
secret_bitarray.frombytes(secret)

def encode_duplicated(img, secret_bitarray):
    cursor = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                new_ba = int2ba(int(img[i][j][k]))
                new_ba[-1] = secret_bitarray[cursor]
                new_num = ba2int(new_ba)
                img[i][j][k] = new_num
                cursor = (cursor + 1) % len(secret_bitarray)
    return img

def encode(img, secret_bitarray):
    cursor = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                if cursor < len(secret_bitarray):
                    new_ba = int2ba(int(img[i][j][k]))
                    new_ba[-1] = secret_bitarray[cursor]
                    new_num = ba2int(new_ba)
                    img[i][j][k] = new_num
                    cursor += 1
                else:
                    return img
    return img

def decode(img):
    secret_bitarray = bitarray()

    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                new_ba = int2ba(int(img[i][j][k]))
                secret_bitarray.append(new_ba[-1])

    return secret_bitarray.tobytes()


print('Encoding...')
encoded_img = encode(img, secret_bitarray)
cv2.imwrite('encoded_benio.jpg', encoded_img)
print('The encoded file was saved')

print('Decoding...')
decoded_message = decode(encoded_img)
print(f'decoded message: {decoded_message[:100]} [...]')