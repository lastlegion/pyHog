#pyHog
from SimpleCV import *
def HOG(Img, no_divs=3, no_bins=6):
    
    n_HOG = no_divs*no_divs*no_bins;
    
    #Initialize output HOG vector
    HOG = [0.0]*n_HOG    

    #Apply sobel on image to find x and y orientations of the image
    Icv = Img.getNumpyCv2()
    Ix = cv2.Sobel(Icv, ddepth = cv.CV_32F, dx=1, dy=0, ksize=3)
    Iy = cv2.Sobel(Icv, ddepth = cv.CV_32F, dx=0, dy=1, ksize=3)
 
    Ix = Ix.transpose(1,0,2)
    Iy = Iy.transpose(1,0,2)
    cellx = Img.width/no_divs     #width of each cell(division)
    celly = Img.height/no_divs    #height of each cell(division)    
    
    #Area of image
    img_area = Img.height * Img.width

    #Range of each bin
    BIN_RANGE = (2*pi)/(no_bins)

    m=0
    print Img.size()
    print Ix.shape
    
    while m < no_divs:
        n = 0
        while n < no_divs:
            i = 0
            while i < cellx:
                j=0
                while j < celly:
                    print m*cellx+i
                    print n*celly+j
                    px = Ix[m*cellx +i, n*celly+j][0]
                    py = Iy[m*cellx+i, n*celly+j][0]
                    
                    #grad value
                    grad = sqrt(px*px + py*py)
                    #normalized grad value
                    norm_grad = grad/img_area
                    #print norm_grad
                    #Angle
                    angle = atan2(py,px)
                    if(angle < 0):
                        angle = angle+ 2*pi
                    nth_bin = floor(float(angle/BIN_RANGE))
                    #nth_bin = angle*(180/pi)%180
                    #print nth_bin
                    HOG[((m*no_divs+n)*no_bins + int(nth_bin))] += norm_grad
                    j=j+1
                i= i+1
            n=n+1
        m=m+1
    
    return HOG

def main():
    if not (len(sys.argv) == 2):
        print "Usage: python hog.py <imagepath>"
        return 
    img = Image(sys.argv[1])
    H = HOG(img, 3, 16)
    print H
if __name__ == "__main__":
    main()
