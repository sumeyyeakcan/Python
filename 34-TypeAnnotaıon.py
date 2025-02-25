# name:str="atıl"
# print(type(name))

# name:str="atıl"
# age:int=30
# is_student :bool=False

# def add_numbers(a:int,b:int) ->int:
#     return a+b
# print(add_numbers(4,3))

# def process_value(value:int  | str) ->str:
#     if isinstance(value,int):
#         return f"processed integer:{value}"
#     else:
#         return f"processed string:{value}"
# print(process_value(12))
# print(process_value("selma"))

# from typing import List
# def sum_list(numbers:List[int])->int:
#     return sum(numbers)

# numbers=[1,2,3,4,5]
# print(sum_list(numbers))

# import cv2
# import numpy as np

# def clahe_color(image):
#     """Apply CLAHE to a color image."""

#     # Convert the image to grayscale
#     grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply CLAHE to the grayscale image
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     clahe_image = clahe.apply(grayscale_image)

#     # Convert the CLAHE image back to color
#     color_image = cv2.cvtColor(clahe_image, cv2.COLOR_GRAY2BGR)

#     return color_image

# # Open the satellite image
# image = cv2.imread("rgb.png")

# # Apply CLAHE to the image
# clahe_image = clahe_color(image)

# # Save the CLAHE image
# cv2.imwrite("clahe_image1.png", clahe_image)
#calıstı  sıyah beyaz