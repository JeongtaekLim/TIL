def isPal(mstring):
  while len(mstring) > 1:
    if mstring[0] == mstring[-1]:
      mstring = mstring[1:-1]
    else:
      return False
  return True

userin = raw_input()
print isPal(userin)