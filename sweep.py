# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid)
def validate( block_data ):
  # Check whether the centre block is a bomb, a number, or an invalid input
  # Skip bombs, send an error on invalid input, verify numbers
  validi = True
  #Check if the input is valid(a square)
  for i in range(0, len(block_data)):
    if len(block_data[i]) == len(block_data):
      validi = True
      i += 1
    else:
      validi = False
      i = -10
  
  if validi == True:
    #Check every coordinate in the grid
    for y in range(0, len(block_data)):
      for x in range(0, len(block_data[y])):
        #Check if the coordinate is a valid number
        if block_data[y][x] >= -1 and block_data[y][x] <= 8:
          if block_data[y][x] >= 0:
            bcount = 0
            #Check the coordinates around the number for bombs
            for cx in range (-1, 2):
              for cy in range (-1, 2):
                if y+cy >= 0 and y+cy <= len(block_data)-1 and x+cx >= 0 and x+cx <= len(block_data)-1:
                  if block_data[y+cy][x+cx] == -1:
                    #Add to the coordinates block count
                    bcount += 1
                cy+=1
              cx+=1
            if bcount != block_data[y][x]:
              return 'Invalid value at: ' + str(x) + ", " +str(y) + '. ' + str(bcount) + ' bombs found, ' + str(block_data[y][x]) + ' bombs required.'
        else:  
          return "Value out of range(-1-8) at:" + str(x) + ", " + str(y) + "."
        x+=1
      y+=1
  else:
    return "Invalid minesweeper board. Must be square."
  return "Valid minesweeper board!"


grid = [
  [-1,1,0],
  [1,1,0],
  [0,0,0]
]
print (validate(grid))