![image](https://user-images.githubusercontent.com/127352017/229747357-db56f032-a52f-4f72-bfe8-338a7bba261b.png)


# NYNET
NyNet is a basic python 3 stresser that comes with 3 pre-made methods (basic) and can also add implimentation for your own API. It also comes with a login system that can be configured easily and also managed and maintained within the C2 itself.

## How to setup

1. Do `pip install colorama` to install the required python module
2. Go to the setup folder and then add your new users and passwords this can be done by editing the currently implimented users "root" and "test".
3. Run the python file and you will then get a database.db file
4. In line 12 of `nynet.py` add your admin users in a list format
5. In line 13 of `nynet.py` add your VIP users in a list format
6. in line 14 of `nynet.py` add your VIP methods in a list format
7. In line 16 of `nynet.py` add your blacklisted IP's
8. If you are hosting your `database.db` file on a external server you can remove the comments in line 7,8,9 of `nynet.py` and in line `9` you should add your server IP and port you want to connect to when logging in.
9. In line `292` of `nynet.py` add your attack methods from your API
10. In line 88 of `nynet.py` add your API inside of `requests.get()`

This is only meant to serve as a PoC and is to be used at your own risk. This is just a base product.
