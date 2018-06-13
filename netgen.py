import secrets

out_string = "  <Option name=\\\"NetworkKey\\\" value=\\\"0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s\\\" />"
RAN_SPOTS = 16

def to_hex(n):
    if n < 10:
        return str(n)
    elif n == 10:
        return "A"
    elif n == 11:
        return "B"
    elif n == 12:
        return "C"
    elif n == 13:
        return "D"
    elif n == 14:
        return "E"
    elif n == 15:
        return "F"
    return "0"

def ran_hex():
    seq = range(16)
    return "%s%s" % (to_hex(secrets.choice(seq)), to_hex(secrets.choice(seq)))


val_list = list()

for spot in range(RAN_SPOTS):
    gen = ran_hex()
    val_list.append(gen)

out_val = out_string % (val_list[0],
                        val_list[1],
                        val_list[2],
                        val_list[3],
                        val_list[4],
                        val_list[5],
                        val_list[6],
                        val_list[7],
                        val_list[8],
                        val_list[9],
                        val_list[10],
                        val_list[11],
                        val_list[12],
                        val_list[13],
                        val_list[14],
                        val_list[15]
                        )

print(out_val)
