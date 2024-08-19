import cv2

user = input("Image file: ")

image = cv2.imread(user)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(h, w) = image.shape[:2]

new_width = 600

aspect_ratio = h / w
new_height = int(new_width * aspect_ratio)

resized_image = cv2.resize(image, (new_width, new_height))

order = " .',:ceoxkbJCDO@"

order = order[::-1]

str = ''

for row in resized_image:
	str += ''.join(order[int(r//16)] for r in row)
	str+= '\n'
	
open('out.txt', 'w').write(str)

cv2.waitKey(0)

cv2.destroyAllWindows()
