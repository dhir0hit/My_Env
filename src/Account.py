from cryptography.fernet import Fernet
import uuid


class Account:
    def __init__(self,
                 user_name=None,
                 password=None,
                 platform=None,
                 website=None,
                 _id=None):
        # Key for encoding and decoding
        # getting from file
        self._key_ = None
        with open('./utils/passwordManager.txt') as key_file:
            self._key_ = key_file.read().encode()

        # account main fields
        self._id_ = uuid.uuid1() if _id is None else _id
        self._username_ = user_name
        self._password_ = password if type(password) == type(bytes) else self._encrypt_(password)
        self._platform_ = platform
        self._website_ = website

    def _encrypt_(self, _string):
        fernet = Fernet(self._key_)
        return fernet.encrypt(_string.encode())

    def _decrypt_(self, _string):
        fernet = Fernet(self._key_)
        return fernet.decrypt(_string).decode()

    def set_username(self, username):
        self._username_ = username

    def set_password(self, password):
        """
        encrypt string password
        :param password: string password
        """
        self._password_ = self._encrypt_(password)
        print(self._password_)

    def set_platform(self, platform):
        self._platform_ = platform

    def set_website(self, website):
        self._website_ = website

    def get_all(self):
        """
        get all account data
        :return: dictionary of account data
        """
        return {
            "id": self._id_,
            "username": self._username_,
            "password": self._decrypt_(self._password_),
            "platform": self._platform_,
            "website": self._website_
        }

    def Id(self):
        """
        :return: id in UUID
        """
        return self._id_

    def Username(self):
        """
        :return: Username in String
        """
        return self._username_

    def Password(self):
        """
        decrypt encrypted password and returns it
        :return: password in String
        """
        return self._decrypt_(self._password_)

    def encrpytedPassword(self):
        """
        encrpted password for database only
        :return: password in bytes
        """
        return self._password_

    def Platform(self):
        """
        :return: Platform in String
        """
        return self._platform_

    def Website(self):
        """
        :return: Website in String
        """
        return self._website_
