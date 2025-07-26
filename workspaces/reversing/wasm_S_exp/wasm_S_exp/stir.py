values = {
    38:0x7b,
    20:0x67,
    46:0x5f,
    3:0x21,
    18:0x63,
    119:0x6e,
    51:0x5f,
    59:0x79,
    9:0x34,
    4:0x57,
    37:0x35,
    12:0x33,
    111:0x62,
    45:0x63,
    97:0x7d,
    54:0x30,
    112:0x74,
    106:0x31,
    43:0x66,
    17:0x34,
    98:0x34,
    120:0x54,
    25:0x5f,
    127:0x6c,
    26:0x41
}
results = {}
for k, v in values.items():
    result = 1024 + ((((k ^ 0x5a5a) * 37) + 23) % 101)
    results[result] = v

for k, v in sorted(results.items(), key=lambda x:x[0]):
    print(f"{chr(v)}", end="")
print()
