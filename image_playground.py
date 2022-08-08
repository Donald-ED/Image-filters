import filters
import image_io

height = 256
width = 20 
image = []
for i in range(height):
    row = []
    for col in row:
        col = [255, 255, 255]
        row.append(col)
        image.append(row)
        
image_io.write_to_file("output/image.png", image)

# Use this playground to try out different functions!
