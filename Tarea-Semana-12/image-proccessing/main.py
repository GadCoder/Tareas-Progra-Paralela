# main_script.py
from PIL import Image
import numpy as np
from mpi4py import MPI

from image import divide_image_in_quarters
from filter import apply_sepia_filter


# MPI initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = 4

img_path = "sample_image.jpg"
img_quartes = divide_image_in_quarters(img_path)



# Analyze sentiment for the assigned subset of opinions

img_part = {rank: apply_sepia_filter(img_quartes[rank])}

# Gather results on process 0
img_parts = comm.gather(img_part, root=0)

# Process 0 prints the results
if rank == 0:
    parts = {}
    for part in img_parts:
        for key, img in part.items():
            parts[key] = np.array(img)
    top_row = np.hstack((parts[0], parts[1]))
    bottom_row = np.hstack((parts[2], parts[3]))
    joined_image = np.vstack((top_row, bottom_row))

    # Convert the NumPy array back to a PIL image
    joined_image = Image.fromarray(joined_image)
    joined_image.show()
           
 

