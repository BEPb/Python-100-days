"""
 	шифрование и расшифровка
	СИММЕТРИЧНОЕ ШИФРОВАНИЕ - ШИФРОВАНИЕ И РАСШИФРОВКА ЯВЛЯЮТСЯ ОДНИМ И ТЕМ ЖЕ КЛЮЧОМ - DES / AES
	АСИММЕТРИЧНОЕ ШИФРОВАНИЕ - ШИФРОВАНИЕ И РАСШИФРОВКА - ЭТО РАЗНЫЕ КЛЮЧИ - RSA
pip install pycrypto
"""
import base64

from hashlib import md5

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

# # КЛЮЧ ШИФРОВАНИЯ AES (32 БАЙТА В ДЛИНУ)
# key = md5(b'1qaz2wsx').hexdigest()
# # НАЧАЛЬНЫЙ ВЕКТОР ШИФРОВАНИЯ AES (ГЕНЕРИРУЕТСЯ СЛУЧАЙНЫМ ОБРАЗОМ)
# iv = Random.new().read(AES.block_size)


def main():
    """основная функция"""
    # создайте пару ключей
    key_pair = RSA.generate(1024)
    # импорт открытого ключа
    pub_key = RSA.importKey(key_pair.publickey().exportKey())
    # импорт закрытого ключа
    pri_key = RSA.importKey(key_pair.exportKey())
    message1 = 'hello, world!'
    # зашифрованные данные
    data = pub_key.encrypt(message1.encode(), None)
    # КОДИРОВАНИЕ ЗАШИФРОВАННЫХ ДАННЫХ BASSE64
    message2 = base64.b64encode(data[0])
    print(message2)
    # ДЕКОДИРОВАНИЕ ЗАШИФРОВАННЫХ ДАННЫХ BASE64
    data = base64.b64decode(message2)
    # расшифровать данные
    message3 = pri_key.decrypt(data)
    print(message3.decode())
    # # AES - СИММЕТРИЧНОЕ ШИФРОВАНИЕ
    # str1 = 'я люблю вас всех！'
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # # шифрование
    # str2 = cipher.encrypt(str1)
    # print(str2)
    # # расшифровка
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # str3 = cipher.decrypt(str2)
    # print(str3.decode())


if __name__ == '__main__':
    main()
