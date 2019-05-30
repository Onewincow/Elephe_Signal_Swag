def zippo(xs,ys):
      zs = []
      while not(xs==[] or ys ==[]):
            xs, ys, zs = xs[1:], ys[1:], zs+[xs[0]+ys[0]]
      return zs + xs + ys


print(zippo([],[])) # []
print(zippo([2,7,4],[7,2,5])) # [9,9,9]
print(zippo([2,7,4],[7,2,5,9,9])) # [9,9,9,9,9]
print(zippo([2,7,4,9,9],[7,2,5])) # [9,9,9,9,9]
