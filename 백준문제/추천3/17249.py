a = input() # @===@==@=@==(^0^)==@=@===@

l_face = a.find("(") #12
r_face = a.find(")") #16

print(a[:l_face].count("@"),a[r_face:].count("@"))
