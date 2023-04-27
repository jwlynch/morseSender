# file: mk_cfg_file.py
#
# writes an example config file

from configparser import ConfigParser

import beeps

# make config file
config = ConfigParser()

config['audio'] = {
    "sample_rate": 48000,
    "dit_time": 0.060, # 60 msec
    "frequency": 440, # A below middle C
}

with open("beeps-cfg-example.cfg", "w") as f:
    config.write(f)
