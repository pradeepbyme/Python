# The enumerate() function adds counter to an iterable
# and returns it. The returned object is an enumerate object.


# names = ['Pradeep', 'Sai', 'Deep']
# name_new = []
# for name in enumerate(names):
#     name_new.append(list(name))
#
# print(name_new)

# simple enumerate example

movies = ['Wolf Street', 'Robotica', 'George']
movies_ref = enumerate(movies)
for movie in enumerate(movies, 10):
    print(type(movie))
print(type(movies_ref))