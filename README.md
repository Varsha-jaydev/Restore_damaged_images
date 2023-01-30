# Restore_damaged_images
Opencv
 
 
 This is a simple project in open-cv to restore damaged images.
 
 Here's what happens in the code:

1.Read the damaged image using cv2.imread() and store it in the image variable.

2.Read the mask image, which defines the damaged parts of the image, using cv2.imread() and store it in the marked_damages variable.

3.The second argument of cv2.imread() is set to 0 to read the image in grayscale.

4.Apply binary thresholding to the mask image using cv2.threshold() to convert it into a binary mask, where the damaged parts of the 
image are represented as 255 and the non-damaged parts as 0.

5.Dilate the binary mask using a rectangular kernel and the cv2.dilate() function to expand the damaged regions.

6.Use the cv2.inpaint() function to restore the damaged parts of the image using the binary mask. 

7.The third argument of cv2.inpaint() sets the size of the neighborhood used to interpolate the missing pixels.

8.Show both the original damaged image and the restored image using cv2.imshow() and wait for a key press using cv2.waitKey().

9.Finally, close all the windows using cv2.destroyAllWindows().
