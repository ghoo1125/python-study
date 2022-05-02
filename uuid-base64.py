import uuid
import sys
import base64

id = uuid.uuid1()
print(id)
print(id.bytes, len(id.bytes))

# uuid string base64 encode
uuid_str = str(id)
url_uuid = base64.urlsafe_b64encode(uuid_str.encode('ascii'))
print(url_uuid, len(url_uuid))

# 128 bit uuid base64 encode
short_uuid = base64.b64encode(id.bytes)
print(short_uuid, len(short_uuid))

# = (\x22)
# 0010 0010
# 0010 00 10 0000
# I :001000 (8)
# g: 100000 (32)
