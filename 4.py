def is_valid(passphrase):
    words = passphrase.split()
    anagrams = [''.join(sorted(w)) for w in words]
    return len(set(anagrams)) == len(anagrams)


valid_passphrases = 0
with open("4.txt") as f:
    for line in f.readlines():
        if is_valid(line):
            valid_passphrases += 1

print(valid_passphrases)