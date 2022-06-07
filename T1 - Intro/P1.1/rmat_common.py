def plt_image(path_colab,png_name):
	from imageio import imread
	import matplotlib.pyplot as plt
	path=path_colab+png_name
	image = imread(path)
	plt.imshow(image,cmap=plt.cm.binary)
	plt.axis('off')
	plt.show