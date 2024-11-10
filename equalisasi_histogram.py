import imageio.v2 as imageio  # Menambahkan .v2 untuk memastikan kompatibilitas
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# Membaca citra awal dengan mode grayscale
citra = imageio.imread('captain-america.jpg', mode='L') / 255.0  # Membuat intensitas antara 0 dan 1

# Fungsi untuk melakukan ekualisasi histogram
def ekualisasi_histogram(citra):
    # Hitung histogram dan histogram kumulatif
    histogram, bin_edges = np.histogram(citra, bins=256, range=(0, 1), density=True)
    histogram_kumulatif = np.cumsum(histogram)
    
    # Normalisasi histogram kumulatif
    histogram_kumulatif_normalisasi = histogram_kumulatif / histogram_kumulatif[-1]
    
    # Transformasi intensitas piksel
    citra_ekualisasi = np.interp(citra.flatten(), bin_edges[:-1], histogram_kumulatif_normalisasi)
    
    return citra_ekualisasi.reshape(citra.shape)

# Memproses citra dengan ekualisasi histogram
citra_ekualisasi = ekualisasi_histogram(citra)

# Menampilkan hasil sebelum dan sesudah ekualisasi
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(citra, cmap='gray')
axes[0].set_title("Citra Awal")
axes[1].imshow(citra_ekualisasi, cmap='gray')
axes[1].set_title("Citra Setelah Ekualisasi Histogram")
plt.show()