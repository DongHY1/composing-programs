from urllib.request import urlopen
res = urlopen('https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt')
words = set(res.read().decode().split())

print ({w for w in words if len(w) == 6 and w[::-1] in words})