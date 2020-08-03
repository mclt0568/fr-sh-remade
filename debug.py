import DirControls

print(DirControls.getShortPath("/home/frankium/test"))
print(DirControls.getShortPath("/home/./frankium/test"))
print(DirControls.getShortPath("/home/../home/frankium/test"))
print(DirControls.getShortPath("/home/frankium/home/frankium"))
print(DirControls.getShortPath("/home/test/test"))