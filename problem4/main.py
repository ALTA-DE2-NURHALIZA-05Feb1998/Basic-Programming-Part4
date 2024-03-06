def ubah_huruf(sentence):
    pattern = ""
    for i in range (len(sentence)) :
        teks=sentence[i]
        if teks.isupper() :
            pattern += chr((ord(teks)+10-65) % 26 +65)
        elif teks ==' ':
            pattern +=' '
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB