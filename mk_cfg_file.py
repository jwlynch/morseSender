# file: mk_cfg_file.py
#
# writes an example config file

from configparser import ConfigParser

# make config file
config = ConfigParser()

config['audio'] = {
    "sample_rate": 48000,
    "dit_time": 0.060, # 60 msec
    "frequency": 440, # A below middle C
}

config['morse'] = {
    "char_space_mult": 3,
    "word_space_mult": 7,
    "dah_mult": 3,
}


with open("beeps-cfg-example.cfg", "w") as f:
    config.write(f)
