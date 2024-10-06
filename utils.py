#
#
# binary1 = [
#     [0b00101011, 0b11111010, 0b01000001, 0b01001101],
#     [0b01001100, 0b10101011, 0b00101111, 0b01010010],
#     [0b11111110, 0b00001100, 0b01000001, 0b01001000],
#     [0b01001101, 0b00001100, 0b00101011, 0b01001000]
# ]
#
# binary2 = [
#     [0b00000010, 0b00000011, 0b00000001, 0b00000001],
#     [0b00000001, 0b00000010, 0b00000011, 0b00000001],
#     [0b00000001, 0b00000001, 0b00000010, 0b00000011],
#     [0b00000011, 0b00000001, 0b00000001, 0b00000010]
# ]
# res = [[0 for _ in range(4)] for _ in range(4)]
#
# for i in range(4):
#     for j in range(4):
#         r = 0
#         for k in range(4):
#             if r != 0:
#                 r ^= gf28_multiply(binary1[i][k], binary2[k][j])
#             else:
#                 r = gf28_multiply(binary1[i][k], binary2[k][j])
#         res[i][j] = hex(r)[2:]
#
# # print(res)
#
# result = [
#     ['3a', '9e', 'f1', '88'],
#     ['ea', 'e4', 'a6', '32'],
#     ['72', '8', '20', 'a1'],
#     ['65', 'ac', '47', 'ac']
#
# ]
#
# a = [
#     [0x3a, 0x9e, 0xf1, 0x88],
#     [0xea, 0xe4, 0xa6, 0x32],
#     [0x72, 0x8, 0x20, 0xa1],
#     [0x65, 0xac, 0x47, 0xac]
# ]
#
# b = [
#     [0x75, 0x07, 0x65, 0x0c],
#     [0xdc, 0xbe, 0xdb, 0xa9],
#     [0xab, 0xce, 0x25, 0x5f],
#     [0x91, 0xfa, 0x97, 0xf6]
# ]
# resultt = []
# for i in range(len(a)):
#     res = []
#     for j in range(len(a)):
#         res.append(hex(a[i][j] ^ b[i][j])[2:])
#     resultt.append(res)
#     res = []
# print(resultt)
#
# final_result = [
#     ['4f', '99', '94', '84'],
#     ['36', '5a', '7d', '9b'],
#     ['d9', 'c6', '5', 'fe'],
#     ['f4', '56', 'd0', '5a']
# ]


# d = {}
# d.update({1:{'tmp1': 0}})
# d.update({2:{'tmp2': 0}})
# a = bin(0x8a84eb01)
# print(hex(int(a[2:], 2) ^ int('01000000', 2)))
# print(hex(0b10001010100001001110101100000001 ^ 0b01000000))


#
# d = {
#     'a': 10,
#     'b': 11,
#     'c': 12,
#     'd': 13,
#     'e': 14,
#     'f': 15,
# }
#
# hex_value1 = '8a84eb01'
# hex_value2 = '01000000'
#
#
# def xor_hex_numbers(hex1, hex2):
#     # Convert hex strings to integers (removing '0x' prefix if present)
#     num1 = int(hex1, 16)
#     num2 = int(hex2, 16)
#
#     # Perform XOR
#     result = num1 ^ num2
#
#     # Convert the result back to hexadecimal, remove '0x' prefix, and ensure 8 characters (32 bits)
#     return f"{result:08x}"
#
#
# print(xor_hex_numbers('a0fafe17', '28aed2e6'))

def xor_hex_numbers(hex1, hex2):
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    result = num1 ^ num2

    return f"{result:08x}"


input_key = '3243f6a8885a308d313198a2e0370734'
cipher_key = '2b7e151628aed2a6abf7158809cf4f3c'
# print(find_after_subword(xor_hex_numbers(input_key, cipher_key)))

after_subBytes = "d4 27 11 ae e0 bf 98 f1 b8 b4 5d e5 1e 41 52 30".split()

# print(res)

after_subBytes_matrix = [
    ['d4', 'e0', 'b8', '1e'],
    ['27', 'bf', 'b4', '41'],
    ['11', '98', '5d', '52'],
    ['ae', 'f1', 'e5', '30']
]

for i in range(len(after_subBytes_matrix)):
    after_subBytes_matrix[i] = after_subBytes_matrix[i][i:] + after_subBytes_matrix[i][:i]


# print(after_subBytes_matrix)

def gf28_multiply(a, b, poly=0x11B):
    result = 0

    while b > 0:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= poly
        a &= 0xFF
        b >>= 1
    return result


# Input matrices
after_shiftRows = [
    ['d4', 'e0', 'b8', '1e'],
    ['bf', 'b4', '41', '27'],
    ['5d', '52', '11', '98'],
    ['30', 'ae', 'f1', 'e5']
]

mix_columns_matrix = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

# Initialize result matrix
res = [[0 for _ in range(4)] for _ in range(4)]

# MixColumns operation
for i in range(4):  # Rows of result
    for j in range(4):  # Columns of result
        r = 0
        for k in range(4):  # Dot product over column j of after_shiftRows and row i of mix_columns_matrix
            a = int(after_shiftRows[k][j], 16)  # Convert hex string to integer
            b = mix_columns_matrix[i][k]

            r ^= gf28_multiply(a, b)  # XOR the result of each multiplication
        res[i][j] = f'{r:02x}'  # Format as two-digit hex

after_mixColumn = [
    ['04', 'e0', '48', '28'],
    ['66', 'cb', 'f8', '06'],
    ['81', '19', 'd3', '26'],
    ['e5', '9a', '7a', '4c']
]

# print(hex(int("e9", 16) ^ int("d0", 16)))
# """04 e0 48 28 66 cb f8 06 81 19 d3 26 e5 9a 7a 4c"""
# """a0 fa fe 17 88 54 2c b1 23 a3 39 39 2a 6c 76 05"""
print(list(range(1, 10, 2)))