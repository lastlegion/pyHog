#pyHog
from SimpleCV import *
def HOG(Img, no_divs, no_bins):
    
    n_HOG = no_divs*no_divs*no_bins;
    
    #Initialize output HOG vector
    HOG = [0]*n_HOG    

    #Apply sobel on image to find x and y orientations of the image
    Ix = Img.sobel(1,0, True, 3)
    Iy = Img.sobel(0,1,True, 3)
    
    cellx = Img.width/no_divs     #width of each cell(division)
    celly = Img.height/no_divs    #height of each cell(division)    
    
    #Area of image
    img_area = Img.height * Img.width

    #Range of each bin
    BIN_RANGE = 2*pi/no_bins

    m=0
    while m < no_divs:
        n = 0
        while n < no_divs:
            i = 0
            while i < cellx:
                j=0
                while j < celly:
                    px = Ix[m*cellx +i, n*celly+j][0]
                    py = Iy[m*cellx+i, n*celly+j][0]
                    
                    #grad value
                    grad = sqrt(px*px + py*py)
                    #normalized grad value
                    norm_grad = grad/img_area

                    #Angle
                    angle = atan2(py,px)
                    
                    if(angle< 0):
                        angle+= 2*pi

                    nth_bin = angle/BIN_RANGE

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

if __name__ == "__main__":
    main()
