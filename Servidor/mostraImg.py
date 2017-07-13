# coding=UTF-8
import cv2
import os
import thread

											

def mostraImg():
    cont= 0
    while True:
		path = '/home/joao/Documentos/projetoFinal/fotos/temp%s.jpeg'%str(cont)
		if len(os.listdir('/home/joao/Documentos/projetoFinal/fotos')) == 0:
			path = '/home/joao/Documentos/projetoFinal/semFoto/semFoto.jpg'
		cont=cont+1
		if (cont >= len(os.listdir('/home/joao/Documentos/projetoFinal/fotos'))):
			cont = 0
		img =  cv2.imread(path)
		cv2.namedWindow("SlideShow", cv2.WND_PROP_FULLSCREEN)          
		cv2.setWindowProperty("SlideShow", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
		cv2.imshow("SlideShow",img)
		key=cv2.waitKey(0)
        

		if key==27:
			break
		if key==65361:
			cont = cont - 2
			if cont < 0:
				cont = len(os.listdir('/home/joao/Documentos/projetoFinal/fotos'))-1



#os.system("python clique_auto.py")
#main()
