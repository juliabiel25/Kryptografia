from encypher import encypher
from decypher import decypher
from gen_keys import generate_keys

public_key, private_key = generate_keys()

message = "He was a tall man with an air of superiority about him"
print(f'\noriginal message:\n{message}')

encyphered = encypher(message, public_key)
print(f'\nencyphered message:\n{encyphered}')

decyphered = decypher(encyphered, private_key)
print(f'\ndecyphered message:\n{decyphered}')