import apache

if apache.version == (2, 2):
    from apache22.util_script import *
elif apache.version == (2, 0):
    from apache20.util_script import *
elif apache.version == (1, 3):
    from apache13.util_script import *
else:
    raise RuntimeError('Apache version not supported.')
