from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class Aes:

    @staticmethod
    def encrypt(data, key):
        '''
        AES的ECB模式加密方法
        :param key: 密钥
        :param data:被加密字符串（明文）
        :return:密文
        '''
        key = key.encode('utf8')
        data = pad(data)
        cipher = AES.new(key, AES.MODE_ECB)
        result = cipher.encrypt(data.encode())
        encodestrs = base64.b64encode(result)
        return encodestrs.decode('utf8')

    @staticmethod
    def decrypt(data, key):
        '''
        AES的ECB模式解密方法
        :param key: 密钥
        :param data: 加密后的数据（密文）
        :return:明文
        '''
        key = key.encode('utf8')
        data = base64.b64decode(data)
        cipher = AES.new(key, AES.MODE_ECB)
        return unpad(cipher.decrypt(data)).decode('utf8')


if __name__ == '__main__':
    key = 'I6bPqY4nJqZ1Nk3S'
    data = 'OaegrzN62PXMyXUQxE1Bmw=='

    res = Aes.decrypt(data, key)
    res = Aes.encrypt('aa111111', key)
    print(res)
    exit(0)
