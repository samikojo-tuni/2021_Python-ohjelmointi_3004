# None on Pythonin null arvo. Eri asia kuin esim. 0, false tai "". None ei viittaa mihinkään
def hello(name=None):
  if name is None:
    print("Hello")
  else:
    print("Hello", name)


hello()
hello("Mika")
