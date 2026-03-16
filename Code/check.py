# import matplotlib.pyplot as plt
# import random

# plt.ion()

# x = []
# y = []

# for i in range(10):
#   # random số liệu cho a,y
#   x.append(i)
#   y.append(random.randint(1,10))

#   plt.clf()
#   plt.plot(x,y)
#   plt.title("Biểu đồ")
#   plt.xlabel("Time")
#   plt.ylabel("Value")

#   plt.pause(0.5)

# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# đọc ảnh
img = cv2.imread("image.png")

# chuyển BGR -> RGB (vì matplotlib dùng RGB)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# chuyển grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur (lọc nhiễu)
blur = cv2.GaussianBlur(gray, (5,5), 0)

# edge detection
edges = cv2.Canny(blur, 100, 200)

# hiển thị
plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(img_rgb)
plt.axis("off")

plt.subplot(2,2,2)
plt.title("Gray")
plt.imshow(gray, cmap="gray")
plt.axis("off")

plt.subplot(2,2,3)
plt.title("Blur")
plt.imshow(blur, cmap="gray")
plt.axis("off")

plt.subplot(2,2,4)
plt.title("Edges")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()