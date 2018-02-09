with open('annotations/trainval.txt', 'w') as the_file:
    for x in range(11, 30):
        the_file.write('yellow_buoy_'+str(x)+' 1\n')
    for y in range(100, 127):
        the_file.write('yellow_buoy_'+str(y)+' 1\n')
