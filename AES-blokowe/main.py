from Crypto.Cipher import AES
import time
from os import listdir
from os.path import dirname, join

curr_path = dirname(__file__)
files = [join(curr_path, 'text-samples', f) for f in listdir(join(curr_path, 'text-samples'))]
print(files)

key = b'Sixteen byte key'

results = []

# parse all text files
for f in files:
    file = open(f, "r")
    size = float(file.readline().strip())
    print('size:', size, 'MB')

    res_dict = {}
    res_dict['size'] = size

    # read text
    text = ""
    for l in file:
        text += l

    # tryb ECB
    start = time.perf_counter_ns()
    cipher = AES.new(key, AES.MODE_ECB)
    end = time.perf_counter_ns()
    res_dict['ECB'] = cipher
    res_dict['ECB_time'] = end - start

    # tryb CBC
    start = time.perf_counter_ns()
    cipher = AES.new(key, AES.MODE_CBC)
    end = time.perf_counter_ns()
    res_dict['CBC'] = cipher
    res_dict['CBC_time'] = end - start

    # tryb CTR
    start = time.perf_counter_ns()
    cipher = AES.new(key, AES.MODE_CTR)
    end = time.perf_counter_ns()
    res_dict['CTR'] = cipher
    res_dict['CTR_time'] = end - start


    #########

    # tryb OFB
    start = time.perf_counter_ns()
    cipher = AES.new(key, AES.MODE_OFB)
    end = time.perf_counter_ns()
    res_dict['OFB'] = cipher
    res_dict['OFB_time'] = end - start

    # tryb CFB
    start = time.perf_counter_ns()
    cipher = AES.new(key, AES.MODE_CFB)
    end = time.perf_counter_ns()
    res_dict['CFB'] = cipher
    res_dict['CFB_time'] = end - start

    results.append(res_dict)

    file.close()

print(res_dict)
