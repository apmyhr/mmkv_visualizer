import mmkv

"""
Small script to create basic test data, in attempt to visual and analyze all the basic 
types within MMKV (the protobuf wire types). 
Note: For every run, it will attempt to delete `test_data` if it exists so we don't 
append data records in a "log-structured" fashion, but rather can just simply look at the data.
"""


if __name__ == "__main__":
    mmkv.MMKV.initializeMMKV('.')

    kv = mmkv.MMKV('test_data')

    # 1. int32 - positive
    kv.set(1234, 'int32_positive_key')

    # 2. int32 - negative (10-bytes needed)
    kv.set(-1234, 'int32_negative_key')

    # 3. int64 - positive
    kv.set(2 ** 32 + 1, 'int64_positive_key')

    # 4. int64 - negative
    kv.set(-1 * (2 ** 32) - 1, 'int64_negative_key')

    # 5. bool - true
    kv.set(True, 'bool_true_key')

    # 6. bool - false
    kv.set(False, 'bool_false_key')

    # 7. string
    kv.set('Hi Steven!', 'string_key')

    # 8. bytes
    kv.set(b'some bytes', 'bytes_key')

"""      
00000000  bd 00 00 00 ff ff ff 07  12 69 6e 74 33 32 5f 70  |?...???..int32_p|
00000010  6f 73 69 74 69 76 65 5f  6b 65 79 02 d2 09 12 69  |ositive_key.?..i|
00000020  6e 74 33 32 5f 6e 65 67  61 74 69 76 65 5f 6b 65  |nt32_negative_ke|
00000030  79 0a ae f6 ff ff ff ff  ff ff ff 01 12 69 6e 74  |y.?????????..int|
00000040  36 34 5f 70 6f 73 69 74  69 76 65 5f 6b 65 79 05  |64_positive_key.|
00000050  81 80 80 80 10 12 69 6e  74 36 34 5f 6e 65 67 61  |......int64_nega|
00000060  74 69 76 65 5f 6b 65 79  0a ff ff ff ff ef ff ff  |tive_key.???????|
00000070  ff ff 01 0d 62 6f 6f 6c  5f 74 72 75 65 5f 6b 65  |??..bool_true_ke|
00000080  79 01 01 0e 62 6f 6f 6c  5f 66 61 6c 73 65 5f 6b  |y...bool_false_k|
00000090  65 79 01 00 0a 73 74 72  69 6e 67 5f 6b 65 79 0b  |ey...string_key.|
000000a0  0a 48 69 20 53 74 65 76  65 6e 21 09 62 79 74 65  |.Hi Steven!.byte|
000000b0  73 5f 6b 65 79 0b 0a 73  6f 6d 65 20 62 79 74 65  |s_key..some byte|
000000c0  73 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |s...............|
000000d0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00004000
"""

