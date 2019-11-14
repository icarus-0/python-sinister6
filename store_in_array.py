# Store the Text file data into array

import numpy as np
with open ("D:\\112.txt", "r") as myfile:
    data=np.array(myfile.readlines())
print(data)
