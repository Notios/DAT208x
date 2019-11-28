import numpy as np

#
x = [9, 4, 1, 10, 3, 2]
print(len(x))

#
plt.hist(x)

#
costs = np.column_stack(([2, 2, 3, 1, 3, 3, 3, 2], 
                         [5, 4, 5, 5, 4, 5, 5, 4]))
mean_costs = np.mean(costs[:, 0])
print(mean_costs)

#
x = [[11, 5, 0], [9, 4, 3], [12, 10, 8]]
print(x[0][:2])

#
x = "there are eight planets in our solar system"
print(x.count('e'))

#
x = np.array([2.1, 1.3, 3.2])
print(np.std(x))

#
x = [9, "H", "M", 3, "R", 11]
del(x[2:4])
print(x)

#
a = True
b = [0, 1]
c = ["1", "2", "3"]
print([b,c,a])


#
x = 4.123412
print(int(x))

#
x = [6, 9, 7, 12]
x.reverse()
print(x)

#
x = np.array([5, 3, 7, 8, 1])
bool_x = x > 3
print(bool_x)

#
x = [8, 6, 15, 18, 11, 10]
print(sorted(x, reverse = True))

#
x = np.array([12, 19, 20, 18, 17])
x_small = x[x > 16]
print(x_small)

#
x = [9, 3, 2, 4, 8, 1]
print(x[-3] + x[-5])

#
p = ["D", 2, "E", 5, "F", 4]
q = p + ['Y', 12]
print(q)

#
x = np.array([9, 8, 1, 4, 3, 2])
x_small = x[1:3]
print(x_small)

#
x = np.array([5, 4, 5, 5, 4, 5, 5, 4])
y = np.array([4, 2, 9, 0, 5, 1, 6, 8])
print(np.corrcoef(x, y))

#
store = np.array(["A", "A", "B", "C", "C", "C", "B"])
cost = np.array([23, 20, 28, 26, 27, 21, 24])
select_cost = cost[store == "B"]
print(select_cost)

#
x = "cautioned"
print(x.replace("a", "*"))

#
import pandas as pd
stores = pd.read_csv("https://goo.gl/LN5wGF")
print(stores.loc['b'])

#
x = -7
y = 10
z = -9.2
print(not(x > y) and y < z)

#
a = True
b = "bool"
c = -5
d = 10.25
print(type(d))

#
x = ["c", "b", "a", "b", "c", "a"]
print(x.count("c"))
