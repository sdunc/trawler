
def hex_to_rgb(h):
	# 6 long integer
	rgb = []
	for i in range(0, len(h), 2):
		print(h[i:i+2])
		rgb.append(int(h[i:i+2], 16))
	return tuple(rgb)

print(hex_to_rgb("576a92"))
