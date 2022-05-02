import codecs
import sys

if __name__ == "__main__":
    # unicode ----encode---> bytes
    #  ^                       |
    #  |                       |
    #  -----------decoce--------

    # demo 1 basic type in py3
    # print will use default encoding utf-8
    print("demo 1")
    print(sys.getdefaultencoding())
    u1 = "我"    # py3 str is default to unicode
    u2 = u'\u6211'    # same as u1, but different in py2
    b1 = u1.encode('utf-8')
    b2 = b'\xe6\x88\x91'    # same as b1
    u3 = b2.decode('utf-8')
    print(type(u1), u1)
    print(type(u2), u2)
    print(type(b1), b1)
    print(type(b2), b2)
    print(type(u3), u3)

    # demo 2 bytes wrong len => always decode to unicode first
    print("demo 2")
    s = "中文".encode("utf-8")
    print(s, len(s))
    
    # demo 3 utf-8 mechanism
    print("demo 3")
    # "®": U+00AE 1010 1110
    # utf-8 decoding block U+0080~U+07FF 110xxxxx 10xxxxxx
    # =>                                    00010   101110
    # => 11000010 10101110 = \xc2\xae
    c = b"\xc2\xae".decode('utf-8')
    print(c)
    b = bytes([65, 194, 174]).decode('utf-8')
    print(b)
    print(len(b))

    # demo 4 file length, py3 file I/O default encoded/decoded
    print("demo 4")
    with open("/tmp/bin.txt", 'wb') as f:
        f.write(b"\x41\xc2\xae")    # what will we see when open file? size?
        f.close()
    #  U+6B64 U+00AE U+975E U+5F7C U+0052
    #  3      2      3      3      1
    with open("/tmp/uni.txt", "w") as f2:
        f2.write("此®非彼R")    # write.encode("utf-8"), size?
        f2.close()

    # demo 5 gibberish
    print("demo 5")
    # gibberish = "泰山磐石教會".encode("big5").decode("iso-8859-1")
    gibberish = "®õ¤s½Y¥Û±Ð·|"
    print(gibberish)
    result = gibberish.encode("iso-8859-1").decode("big5")
    print(result)

    # demo 6 gibberish with  big/little endian
    print("demo 6")
    byte = "泰山磐石教會".encode("utf-8")
    print(byte)
    gibberish = byte.decode("utf-16")    # "돦놱ꏧ뎟闦莜"
    print(gibberish)
    # print(gibberish.encode("utf-16").decode("utf-8"))    # exception due to endian bom
    print(gibberish.encode("utf-16"))

    bom = codecs.BOM_UTF16_LE
    result = gibberish.encode("utf-16")[len(bom):].decode("utf-8")
    print(result)
