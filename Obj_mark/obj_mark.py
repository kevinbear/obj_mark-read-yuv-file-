import sys , os
import numpy as np

#Golbol var set
width = 640
height = 480
ysize = width*height
usize = int(ysize/4)
vsize = int(ysize/4)
def main():
	frame = 0
	pos = 0
	'''Y = [0] * height * width
	U = [0] * height * width
	V = [0] * height * width
	ydata = np.zeros(height*width,dtype = np.uint8)
	udata = np.zeros(height*width,dtype = np.uint8)
	vdata = np.zeros(height*width,dtype = np.uint8)'''
	while True :
		with open("C:/Users/kevinkuo/Desktop/Obj_mark/1.yuv", "rb") as File:
			File.seek(pos,0)
			Y = File.read(ysize)
			U = File.read(usize)
			V = File.read(vsize)
			pos = File.tell()
			print(pos)
			#print(type(Y)) # <class 'bytes'>
			#print(V[0],V[319])
			filesize = int(width*height*1.5*frame)
			if pos == filesize :
				File.close()
				break
			else :
				with open("C:/Users/kevinkuo/Desktop/Obj_mark/test.yuv", "ab") as raw:
					YUV = Y
					YUV += U
					YUV += V
					frame += 1
					print('frame {}'.format(frame))
					raw.write(YUV)
					raw.close()
		
if __name__ == "__main__" :
	main()
