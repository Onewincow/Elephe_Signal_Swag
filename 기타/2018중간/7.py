def blast(ns):
      bs = []
      for x in range(len(ns)):
          bs += [ns[x]]*ns[x]
      return bs


print(blast([]))	#[]
print(blast([1,2,4]))	#[1,2,2,4,4,4,4]
print(blast([3,5]))	#[3,3,3,5,5,5,5,5]
print(blast([2,-3,3]))	#[2,2,3,3,3]
