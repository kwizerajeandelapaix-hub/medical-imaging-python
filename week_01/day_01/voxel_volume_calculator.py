#collecting user inputs
image_width = int(input("type image width: "))
image_height = int(input("type image height: "))
number_slices = int(input("type number of slices: "))
horizantal_spacing = float(input("type horizontal pixel spacing: "))
vertical_spacing = float(input("type vertical pixel spacing: "))
slice_thickness = float(input("type slice thivkness: "))
#calculations
spacing_area = horizantal_spacing * vertical_spacing
voxel_volume = spacing_area * slice_thickness
total_number_voxels = image_width * image_height * number_slices
total_phyisical_image_volume = total_number_voxels * voxel_volume
total_phyisical_image_cm = total_phyisical_image_volume/1000

#printing and display

print("\n===== MEDICAL IMAGE VOLUME REPORT =====\n")

print(f"Pixel area: {spacing_area:.3f} mm²")
print(f"Voxel volume: {voxel_volume:.3f} mm³")
print(f"Total number of voxels:{total_number_voxels}")
print(f"Total image volume: {total_phyisical_image_volume:.3f} mm³")
print(f"Total image volume: {total_phyisical_image_cm:.3f} cm³")



print("\n================================")