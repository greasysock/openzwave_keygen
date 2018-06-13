import netgen

file = "/usr/local/etc/openzwave/options.xml"
output = file

config_target = "  <!-- <Option name=\"NetworkKey\" value=\"0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10\" /> -->\n"

keychain = netgen.hex_keychain()
newlines = []
with open(file, "r") as f:
    for x, line in enumerate(f):
        if line == config_target:
            newlines.append("%s\n"%(keychain))
        else:
            newlines.append(line)
with open(output, "w") as nf:
    nf.writelines(newlines)
