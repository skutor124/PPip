
import aes128

def encrypt_aes(key, input_path, out_path):
    with open(input_path, 'rb') as f:
        data = f.read()
    crypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            crypted_part = aes128.encrypt(temp, key)
            crypted_data.extend(crypted_part)
            del temp[:]
    else:
        if 0 < len(temp) < 16:
            empty_spaces = 16 - len(temp)
            for i in range(empty_spaces - 1):
                temp.append(0)
            temp.append(1)
            crypted_part = aes128.encrypt(temp, key)
            crypted_data.extend(crypted_part)

        # Ounput data
        with open(out_path, 'wb') as ff:
            ff.write(bytes(crypted_data))


def decrypt_aes(key, input_path, out_path):
    with open(input_path, 'rb') as f:
        data = f.read()
    decrypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            decrypted_part = aes128.decrypt(temp, key)
            decrypted_data.extend(decrypted_part)
            del temp[:]
    else:
        if 0 < len(temp) < 16:
            empty_spaces = 16 - len(temp)
            for i in range(empty_spaces - 1):
                temp.append(0)
            temp.append(0)
            decrypted_part = aes128.encrypt(temp, key)
            decrypted_data.extend(decrypted_part)

    # Output data
    with open(out_path, 'wb') as ff:
        ff.write(bytes(decrypted_data))
