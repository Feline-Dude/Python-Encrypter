import random

char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

sec = 0

def Seed_Generator(sifre):
    seed = ""
    seed_len = random.randint(4, 9)  
    i = 0
    while(i != seed_len):
        random_num = random.randint(1, 3)
        if (random_num == 3):
            seed += str(random.randint(1, 9))
            i += 1
        else:
            seed += str(random.choice(char_list))
            i += 1
            
    new_seed = seed[1:]
    return new_seed

def Seed_Decoder(seed):
    new_seed = ""
    for char in seed:
        if char.isalpha():
            new_seed += str(ord(char))
        elif char.isdigit():
            new_seed += char
        else:
            pass
    return new_seed

def RNG_Encrpyter(new_seed, sifre):
    seed_str = str(new_seed)
    digits = [int(char) for char in seed_str]
    digit_sum = sum(digits)
    encrypted_parts = []
    for char in sifre:
        num_pass = ord(char) + digit_sum + digits[2] - (digits[-1] + digits[1])
        encrypted_parts.append(str(num_pass))
    sonuc = " ".join(encrypted_parts)
    return sonuc

def RNG_Decrpyter(seed, sifre):
    if any(c.isalpha() for c in seed):
        seed = Seed_Decoder(seed)
    digits = [int(char) for char in seed]
    digit_sum = sum(digits)
    encrypted_parts = sifre.split()
    decrypted_chars = []
    for part in encrypted_parts:
        num_pass = int(part)
        num_pass = num_pass + (digits[-1] + digits[1])   
        num_pass = num_pass - digits[2]
        num_pass = num_pass - digit_sum
        decrypted_chars.append(chr(num_pass))
    sonuc = "".join(decrypted_chars)
    return sonuc

while(sec != 3):
    sec = int(input("Enter 1 for Encryption, 2 for Decryption and 3 to exit program:  "))
    if(sec == 1):
        sifre = input("Enter string that you want to encrypt: ")
        int_seed = Seed_Generator(sifre)
        de_seed = Seed_Decoder(int_seed)
        sonuc = RNG_Encrpyter(de_seed, sifre)
        print(sonuc)
        print(int_seed, " DO NOT LOSE this seed otherwise the encrypted message will be lost")
    if(sec == 2):
        sifre = input("Enter the message you want to decrypte: ")
        decode = input("Enter the seed: ")
        sonuc = RNG_Decrpyter(decode, sifre)
        print(sonuc, " is the decrypted message.")
    if(sec == 3):
        pass

    #You can additionally create your own RNG encrpytion algorithm
    #For example if you use only additions in the encryption algorithm, you must flip the process and use subtraction!
    