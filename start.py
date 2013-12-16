#!/usr/bin/env python
from chickenfoot import Chickenfoot

config_file = 'chickenfoot.json'
cf = Chickenfoot()
cf.init_from_file(config_file)
cf.listen()
