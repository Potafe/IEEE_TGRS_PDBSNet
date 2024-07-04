import scipy.io
import matplotlib.pyplot as plt

# Load .mat file
mat_file = r'C:\Users\Yazat\OneDrive\Desktop\IEEE_TGRS_PDBSNet\result\WHU-HI-River\detectmap.mat'
mat_data = scipy.io.loadmat(mat_file)

data = mat_data['detectmap']
print(data)

threshold = 0.1 # Adjust threshold based on your detectmap values
anomaly_map = data > threshold

    # Visualize detectmap with anomalies in white and rest in black
plt.figure(figsize=(10, 8))
plt.imshow(anomaly_map, cmap='gray')  # Use grayscale colormap
plt.title('Anomaly Detection Map')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()

# import numpy as np
# import scipy.io as sio
# from spectral import *

# # Load ENVI files
# img_file = r"C:\Users\Yazat\OneDrive\Desktop\1st July 2024\TDD\data\WHU-Hi-River.img"
# hdr_file = r"C:\Users\Yazat\OneDrive\Desktop\1st July 2024\TDD\data\WHU-Hi-River.hdr"

# img = envi.open(hdr_file, img_file)
# data = img.load()

# # Save as .mat file
# sio.savemat('WHU-HI-River.mat', {'data': data})

# print('Conversion completed.')


