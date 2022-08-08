
# Use this file to write your filter functions!

def red_stripes(image_matrix):
  counter = 0
  pixel = 0
  stripes = 50
  while pixel < len(image_matrix):
    counter += 1
    for pixels in range(0, len(image_matrix[0])):
        pixels = image_matrix[pixel][pixels]
        pixels[0] = 255
    if counter >= stripes:
      pixel += 51
      counter = 0 
    else:
      pixel += 1
              
  return image_matrix  
    

def grayscale(image_matrix):
  for pixels in image_matrix:
        for pixel in pixels:
            avg = (pixel[0] + pixel[1] + pixel[2])//len(pixel)
            pixel[0] = avg
            pixel[1] = avg
            pixel[2] = avg
  return image_matrix  

def invert_colors(image_matrix):
    for pixels in image_matrix:
        for pixel in pixels:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return image_matrix        
    pass


def flip(image_matrix):
    image = []
    for i in image_matrix:
        image.insert(0, i)
    return image    
    pass



def sepia(image_matrix):
  for pixels in image_matrix:

    for pixel in pixels:

      R = pixel[0]
      G = pixel[1]
      B = pixel[2]

      pixel[0] = int(((R*0.393)//1) + ((G*0.769)//1) + ((B*0.189)//1))
      pixel[1] = int(((R*0.349)//1) + ((G*0.686)//1) + ((B*0.168)//1))
      pixel[2] = int(((R*0.272)//1) + ((G*0.534)//1) +((B*0.131)//1))
      
      if (pixel[0] or pixel[1] or pixel[2]) > 255:
        pixel[0] = 255
        pixel[1] = 255
        pixel[2] = 255

  return image_matrix    

def blur(image_matrix):
  output_image = []
  R = 0
  G = 0
  B = 0
  for row in range(len(image_matrix)):
    output_row = []
    for col in range(len(image_matrix[row])):
      neighbour = []
      for i in range(-1, 2):
        for j in range(-1 ,2):
          nrow = row + i
          ncol = col + j
          if (nrow < len(image_matrix) and nrow > 0) and (ncol < len(image_matrix[0]) and ncol >= 0):
            neighbour.append(image_matrix[nrow][ncol])
      for pixel in neighbour:
        R += pixel[0]
        G += pixel[1]
        B += pixel[2]                
      R = R//len(neighbour)
      G = G//len(neighbour)
      B = B//len(neighbour)
      blur_pixel = [R, G, B]
      output_row.append(blur_pixel)
    output_image.append(output_row) 
  return output_image 
    



def threshold(image_matrix,
              red_threshold=(0, 255),
              green_threshold=(0, 255),
              blue_threshold=(0, 255)):
  min_red = red_threshold[0]
  max_red = red_threshold[1]
  min_green = green_threshold[0]
  max_green = green_threshold[1]
  min_blue = blue_threshold[0]
  max_blue = blue_threshold[1]
  for pixels in image_matrix:

    for pixel in pixels:

      if (pixel[0] > max_red) or (pixel[0] < min_red) or (pixel[1] > max_green) or (pixel[1] < min_green) or (pixel[2] > max_blue) or (pixel[2] < min_blue):
        pixel[0] = 0
        pixel[1] = 0
        pixel[2] = 0    

  return image_matrix            

def blue(image_matrix):
  for pixels in image_matrix:
    for pixel in pixels:
      pixel.reverse()
  return image_matrix 

   
