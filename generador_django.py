"""
Pseudo-random django secret key generator.
- Does print SECRET key to terminal which can be seen as unsafe.
"""

import string
import random

# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

with open('.env', 'a') as f:
    f.write(f'SECRET_KEY = "{SECRET_KEY}"\n')