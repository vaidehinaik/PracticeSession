a = [1,8,6,2,5,4,8,3,7]
# a = [150,200,6,2,5,4,15,3,7]
# a = [1,1,1,1,1,1,1,1,1, 1]
area = 0
for i, v in enumerate(a):
  # print(i)
  prev_y_axis = 0
  for j in range(len(a) - 1, 0, -1):
    # print(j)
    x_axis = (j + 1) - (i + 1)
    y_axis = v if v < a[j] else a[j]
    if y_axis < prev_y_axis:
      continue
    # print(x_axis)
    # print(y_axis)
    if area < x_axis * y_axis:
      area = x_axis * y_axis
    prev_y_axis = v if v > a[j] else a[j]
print("Biggest water container: {}".format(area))
