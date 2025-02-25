from rembg import remove
import onnxruntime as ort

input_path = "C:/Users/akcan/Desktop/Yazilim/image.png"
output_path = "C:/Users/akcan/Desktop/Yazilim/outputtttt.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

        