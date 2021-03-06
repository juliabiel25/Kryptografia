encoded = "ALEXMWXLIEJVMGERPMSREJVMGERPMSRWLEZIFIIREHQMVIHXLVSYKLSYXLMWXSVCJSVEWWCQFSPWSJGSYVEKIERHWXVIRKXLXLIWIMGSRMGERMQEPWLEZITSAIVJYPFSHMIWMRXLIGEXJEQMPCXLICVIWIGSRHMRWMDISRPCXSXMKIVWERHVSEVWXLEXGERFILIEVHJVSQJMZIQMPIWEAECEREHYPXPMSRWGSEXMWCIPPSAKSPHERHNYZIRMPIWLEZIWSQIPMKLXWTSXWXLEXHMWETTIEVAMXLEKISRPCQEPIPMSRWXCTMGEPPCFSEWXQERIWXLIMQTVIWWMZIJVMRKISJPSRKLEMVXLEXIRGMVGPIWXLIMVLIEHW"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
freqs = []
en_freqs = [('E', 12.2), ('T', 8.8), ('A', 7.9), ('O', 7.2), ('I', 6.8), ('N', 6.5), ('S', 6.1), ('H', 5.9), ('R', 5.8), ('D', 4.1), ('L', 3.9), ('C', 2.7), ('U', 2.7), ('W', 2.3), ('M', 2.3), ('F', 2.1), ('G', 1.9), ('Y', 1.9), ('P', 1.8), ('B', 1.4), ('V', 1.0), ('Z', 1.0), ('K', 0.8), ('J', 0.2), ('X', 0.2), ('Q', 0.1)]
decoded = ""

example1 = "IHADTHUSLEARNEDASECONDFACTOFGREATIMPORTANCETHISWASTHATTHEPLANETTHELITTLEPRINCECAMEFROMWASSCARCELYANYLARGERTHANAHOUSEBUTTHATDIDNOTREALLYSURPRISEMEMUCHIKNEWVERYWELLTHATINADDITIONTOTHEGREATPLANETSSUCHASTHEEARTHJUPITERMARSVENUSTOWHICHWEHAVEGIVENNAMESTHEREAREALSOHUNDREDSOFOTHERSSOMEOFWHICHARESOSMALLTHATONEHASAHARDTIMESEEINGTHEMTHROUGHTHETELESCOPEWHENANASTRONOMERDISCOVERSONEOFTHESEHEDOESNOTGIVEITANAMEBUTONLYANUMBERHEMIGHTCALLITFOREXAMPLEASTEROID"
example_encoded = ""
offset = 5

# szyfrowanie
for l in example1:
    example_encoded += alphabet[(alphabet.index(l) + offset)%len(alphabet)]
print(example1)
print(example_encoded)
encoded = example_encoded

# encoded = "JRERABFGENATREFGBYBIRLBHXABJGUREHYRFNAQFBQBVNSHYYPBZZVGZRAGFJUNGVZGUVAXVATBSLBHJBHYQAGTRGGUVFSEBZNALBGURETHLVWHFGJNAANGRYYLBHUBJVZSRRYVATTBGGNZNXRLBHHAQREFGNAQVZARIRETBAANTVIRLBHHCARIRETBAANYRGLBHQBJAARIRETBAANEHANEBHAQNAQQRFREGLBHARIRETBAANZNXRLBHPELARIRETBAANFNLTBBQOLRARIRETBAANGRYYNYVRNAQUHEGLBH"

freqs = {}
for l in alphabet:
    freqs[l] = 0

# liczenie wystąpień liter w szyfrogramie
for l in encoded:
    freqs[l] += 1

# sortowanie + utworzenie słownika
freqs = sorted(freqs.items(), key=lambda item: item[1], reverse=True)
trans = {}
for i in range(len(alphabet)):
    trans[freqs[i][0]] = (en_freqs[i][0], round((freqs[i][1]/len(encoded)*100) - en_freqs[i][1], 2))

# podstawienie
cut = 100
for l in encoded:
    if trans[l][1] >= cut:
        decoded += '_'
    else:
        decoded += trans[l][0]

print(decoded)

for t in trans:
    print(t, '->', trans[t])
