import numpy as np
import matplotlib.pyplot as plt

#data
mikes_courses = [4,5,8,2,9,9,1,3,7]
life_happiness = [6,7,9,3,9,3,1,6,7]

#mean-center
m = mikes_courses - np.mean(mikes_courses)
l = life_happiness - np.mean(life_happiness)

#compute correlation
numerator = np.dot(m,l)
denominator = np.sqrt(np.dot(m,m)) * np.sqrt(np.dot(l,l))

r1 = numerator/denominator
r2 = np.corrcoef(m,l)

plt.plot(mikes_courses, life_happiness, 'ms', label = 'r=%g' %r1)
plt.axis([0.0,10.0, 0.0,10.0])
plt.gca().set_aspect("equal")
plt.legend()
plt.xlabel("Number of Mike's Courses Taken")
plt.ylabel("Overall Life Happiness")
plt.show()