from re import findall
from random import choice, randint

from rsa import newkeys, encrypt, decrypt


class Crypts(object):

    def get_numbers(self, text):
        template = r"[0-9]+"
        return findall(template, text)

    def get_two_symbols(self, text):
        template = r"[A-Z]{2}"
        return findall(template, text)

    def a1z26(self, mode, message, final=""):
        message = message.upper()
        alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if mode == 'E':
            for symbol in message:
                if symbol not in [chr(x) for x in range(65, 91)]:
                    message = message.replace(symbol, '')
            for symbol in message:
                final += "%hu " % (alpha.index(symbol) + 1)
        else:
            for number in self.get_numbers(message):
                final += "%s" % alpha[int(number) - 1]
        return final

    def affine(self, mode, message, key):
        message = list(message.upper())
        key = key.split()
        for k in key:
            try:
                int(k)
            except Exception:
                return ":: Key is not int type ::"
        if len(key) != 2:
            return ":: Qualitity keys must be 2 ::"
        for index, symbol in enumerate(message):
            if mode == 'E':
                message[index] = chr((int(key[0]) * ord(symbol) + int(key[1]) - 13) % 26 + ord('A'))
            else:
                message[index] = chr(pow(int(key[0]), 11) * ((ord(symbol) + 26 - int(key[1]) - 13)) % 26 + ord('A'))
        return "".join(message)

    def atbash(self, message):
        message = list(message.upper())
        alpha_default = [chr(x) for x in range(65, 91)]
        alpha_reverse = list(alpha_default)
        alpha_reverse.reverse()
        for index, symbolMessage in enumerate(message):
            for indexAlpha, symbolAlpha in enumerate(alpha_default):
                if symbolMessage == symbolAlpha:
                    message[index] = alpha_reverse[indexAlpha]
        return "".join(message)

    def bacon_regular(self, text):
        template = r"[A-Z]{5}"
        return findall(template, text)

    def bacon(self, mode, message, final=""):
        keys = {
            'A': "AAAAA", 'B': "AAAAB", 'C': "AAABA",
            'D': "AAABB", 'E': "AABAA", 'F': "AABAB",
            'G': "AABBA", 'H': "AABBB", 'I': "ABAAA",
            'J': "ABAAB", 'K': "ABABA", 'L': "ABABB",
            'M': "ABBAA", 'N': "ABBAB", 'O': "ABBBA",
            'P': "ABBBB", 'Q': "BAAAA", 'R': "BAAAB",
            'S': "BAABA", 'T': "BAABB", 'U': "BABAA",
            'V': "BABAB", 'W': "BABBA", 'X': "BABBB",
            'Y': "BBAAA", 'Z': "BBAAB", ' ': "BBABA"}
        message = message.upper()
        if mode == 'E':
            for symbol in message:
                if symbol in keys:
                    final += keys[symbol]
        else:
            for symbolsFive in self.bacon_regular(message):
                for key in keys:
                    if symbolsFive == keys[key]:
                        final += key
        return final

    def book(self, mode, message, key, final=""):
        if not key:
            return ":: Key is not found ::"
        if mode == 'E':
            for symbolMessage in message:
                list_of_keys = []
                for indexKey, symbolKey in enumerate(key):
                    if symbolMessage == symbolKey:
                        list_of_keys.append(indexKey)
                try:
                    final += str(choice(list_of_keys)) + '/'
                except IndexError:
                    pass
        else:
            for numbers in self.get_numbers(message):
                for indexKey, symbolKey in enumerate(key):
                    if numbers == str(indexKey):
                        final += symbolKey
        return final

    def caesar(self, mode, message, key):
        message = list(message.upper())
        try:
            key = int(key)
        except Exception:
            return ":: Key is not int type ::"
        for index, symbol in enumerate(message):
            if mode == 'E':
                message[index] = chr((ord(symbol) + key - 13) % 26 + ord('A'))
            else:
                message[index] = chr((ord(symbol) - key - 13) % 26 + ord('A'))
        return "".join(message)

    def couples(self, message):
        keys = {
            'A': 'B', 'C': 'D', 'E': 'F', 'G': 'H', 'I': 'J', 'K': 'L',
            'M': 'N', 'O': 'P', 'Q': 'R', 'S': 'T', 'U': 'V', 'W': 'X',
            'Y': 'Z'}
        message = list(message.upper())
        for symbol in range(len(message)):
            for key in keys:
                if message[symbol] == key:
                    message[symbol] = keys[key]
                elif message[symbol] == keys[key]:
                    message[symbol] = key
        return "".join(message)

    def gronsfeld(self, mode, message, key):
        message = message.upper()
        try:
            int(key)
        except Exception:
            return ":: Key is not int type ::"
        key *= len(message) // len(key) + 1
        for index, symbol in enumerate(message):
            if mode == 'E':
                message[index] = chr((ord(symbol) + int(key[index]) - 13) % 26 + ord('A'))
            else:
                message[index] = chr((ord(symbol) - int(key[index]) - 13) % 26 + ord('A'))
        return "".join(message)

    def homophonic(self, mode, message, final=""):
        values = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c',
                  'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '\\', '#', '№', '$', ';', '%', '^',
                  ':', '&', '?', '(', ')', '-', '_', '+', '=', '`', '~', '[', ']', '{',
                  '}', '.', ',', '/', '|', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '<',
                  '>', 'А', 'М', 'В', 'С', 'у', 'Е', 'Т', 'а', 'Х', 'З')
        dict_hom = {
            'A': values[0:8], 'B': values[8:10],
            'C': values[10:13], 'D': values[13:17],
            'E': values[17:29], 'F': values[29:31],
            'G': values[31:33], 'H': values[33:39],
            'I': values[39:45], 'J': [values[45]],
            'K': [values[46]], 'L': values[47:51],
            'M': values[51:53], 'N': values[53:59],
            'O': values[59:66], 'P': values[66:68],
            'Q': [values[68]], 'R': values[69:75],
            'S': values[75:81], 'T': values[81:90],
            'U': values[90:93], 'V': [values[93]],
            'W': values[94:96], 'X': [values[96]],
            'Y': values[97:99], 'Z': [values[99]]
        }
        if mode == 'E':
            for symbol in message.upper():
                if symbol in dict_hom:
                    final += choice(dict_hom[symbol])
        else:
            for symbol in message:
                for key in dict_hom:
                    if symbol in dict_hom[key]:
                        final += key
        return final

    def polibiy(self, mode, message):
        final = []
        message = message.upper()
        keys = {
            'A': '11', 'B': '12', 'C': '13', 'D': '14',
            'E': '15', 'F': '16', 'G': '21', 'H': '22',
            'I': '23', 'J': '24', 'K': '25', 'L': '26',
            'M': '31', 'N': '32', 'O': '33', 'P': '34',
            'Q': '35', 'R': '36', 'S': '41', 'T': '42',
            'U': '43', 'V': '44', 'W': '45', 'X': '46',
            'Y': '51', 'Z': '52', '0': '53', '1': '54',
            '2': '55', '3': '56', '4': '61', '5': '62',
            '6': '63', '7': '64', '8': '65', '9': '66'
        }
        if mode == 'E':
            for symbol in message:
                if symbol in keys:
                    final.append(keys[symbol])
        else:
            for twoNumbers in self.get_numbers(message):
                for key in keys:
                    if twoNumbers == keys[key]:
                        final.append(key)
        return ".".join(final)

    def replace(self, mode, message):
        message = list(message.upper())
        symbols_alpha = [chr(x) for x in range(65, 91)]
        symbols_crypt = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=',
                         '+', '?', ':', ';', '<', '>', '/', '[', ']', '{', '}', '|', '.', ',', '~')
        keys = dict(zip(symbols_alpha, symbols_crypt))
        if mode == 'E':
            for index, symbol in enumerate(message):
                if symbol in keys:
                    message[index] = keys[symbol]
        else:
            for index, symbol in enumerate(message):
                for key in keys:
                    if symbol == keys[key]:
                        message[index] = key
        return "".join(message)

    def rot13(self, message):
        message = list(message.upper())
        for symbol in range(len(message)):
            message[symbol] = chr(ord(message[symbol]) % 26 + ord('A'))
        return "".join(message)

    def rotors(self, mode, message, final=""):
        message = message.upper()
        list_rotors = (
            (10, 24, 14, 12, 23, 2, 7, 15, 24, 2, 7, 5, 22, 6, 2, 1, 22, 12, 6, 9, 7, 2, 11, 23, 14, 2),
            (1, 7, 11, 26, 12, 5, 11, 20, 11, 7, 18, 6, 17, 18, 19, 1, 13, 5, 2, 9, 11, 13, 6, 17, 26, 24),
            (9, 1, 21, 6, 4, 19, 25, 6, 17, 10, 26, 1, 23, 6, 1, 17, 19, 17, 25, 21, 3, 21, 17, 1, 18, 20)
        )
        x, y, z = 1, 2, 3
        for symbol in message:
            rotor = list_rotors[0][x] + list_rotors[1][y] + list_rotors[2][z]
            if mode == 'E':
                if symbol in [chr(x) for x in range(65, 91)]:
                    final += chr((ord(symbol) - 13 + rotor) % 26 + ord('A'))
                else:
                    continue
            else:
                final += chr((ord(symbol) - 13 - rotor) % 26 + ord('A'))
            if x != len(list_rotors[0]) - 1:
                x += 1
            else:
                x = 0
                if y != len(list_rotors[1]) - 1:
                    y += 1
                else:
                    y = 0
                    if z != len(list_rotors[2]) - 1:
                        z += 1
                    else:
                        z = 0
        return final

    def rsa(self, mode, message, key):
        if mode == 'E':
            message = message.encode("utf8")
            if not key:
                pub, priv = newkeys(1024)
                encrypt_message = encrypt(message, pub)
                return "%s\n%s\n%s" % (str(pub), str(priv), encrypt_message)
            else:
                encrypt_message = encrypt(message, eval(key))
                return str(encrypt_message)
        else:
            try:
                decrypt_message = decrypt(eval(message), eval(key))
            except Exception:
                return ":: Key is not found::"
            else:
                return decrypt_message

    def thritemius(self, mode, message, key):
        message = list(message.upper())
        for symbol in message:
            if symbol not in [chr(x) for x in range(65, 91)]:
                message.remove(symbol)
        try:
            key = eval('lambda x: ' + key)
        except Exception:
            return ":: Key is not found ::"
        for index, symbol in enumerate(message):
            if mode == 'E':
                message[index] = chr((ord(symbol) + key(index) - 13) % 26 + ord('A'))
            else:
                message[index] = chr((ord(symbol) - key(index) - 13) % 26 + ord('A'))
        return "".join(message)

    def vernam(self, mode, message, key):
        message = list(message.upper())
        keys = []
        if mode == 'E':
            for index, symbol in enumerate(message):
                key = randint(0, 25)
                keys.append(str(key))
                message[index] = chr((ord(symbol) + key - 13) % 26 + ord('A'))
            return "".join(message) + '\n' + '.'.join(keys)
        else:
            for index, symbol in enumerate(message):
                try:
                    message[index] = chr((ord(symbol) - int(self.get_numbers(key)[index]) - 13) % 26 + ord('A'))
                except Exception:
                    return ":: Key is not found ::"
            return "".join(message)

    def vishener(self, mode, message, key):
        message = list(message.upper())
        key = key.upper()
        try:
            key *= len(message) // len(key) + 1
        except Exception:
            return ":: Key is not found ::"
        for index, symbol in enumerate(message):
            if mode == 'E':
                message[index] = chr((ord(symbol) + ord(key[index])) % 26 + ord('A'))
            else:
                message[index] = chr((ord(symbol) - ord(key[index])) % 26 + ord('A'))
        return "".join(message)

    def xor(self, message, key):
        message = list(message)
        for symbol in range(len(message)):
            try:
                message[symbol] = chr(ord(message[symbol]) ^ int(key))
            except Exception:
                return ":: Key is not int type ::"
        return "".join(message)
