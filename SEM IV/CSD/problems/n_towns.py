# There are N towns in a coordinate plane. Town i is located at coordinate (xi,yi)
# The distance btw town i and town j is |xi-xj|+|yi-yj|
# Your task is to compute the sum of the distance btw each pair of towns

# 


xi, yi = 5, 7
xj, yj = 4, 1

i = {xi,yi}
j = {xj,yj}

dist = (xi-xj)+(yi-yj)

print(dist)