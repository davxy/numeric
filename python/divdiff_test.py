# Divided differencies test

from divdiff import divdiff

x = [-1,0,1]
y = [3,-4,5]
D = divdiff(x, y)
print('divdiff({},{}) = {}'.format(x, y, D))