# Medical Image Information Program
# Stage 1: Collecting user input

modality = input("Enter imaging modality: ")
image_width = int(input("Enter image width in pixels: "))
image_height = int(input("Enter image height in pixels: "))
pixel_spacing = float(input("Enter pixel spacing in mm: "))
number_of_slices = int(input("Enter number of slices: "))

# Stage 2: Processing and calculations

total_pixels = image_width * image_height
physical_width = image_width * pixel_spacing
physical_height = image_height * pixel_spacing
total_voxels = total_pixels * number_of_slices

# Stage 3: Formatted output

print("\n===== MEDICAL IMAGE REPORT =====\n")

print(f"Modality: {modality}")
print(f"Image dimensions: {image_width} x {image_height} pixels")
print(f"Pixel spacing: {pixel_spacing:.2f} mm")
print(f"Number of slices: {number_of_slices}")
print()
print(f"Total pixels per slice: {total_pixels}")
print(f"Phyisical width: {physical_width:.2f} mm")
print(f"Physical height: {physical_height:.2f} mm")
print(f"Total voxels: {total_voxels}")
print("\n================================")