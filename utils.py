import cv2
# rectangle coordinates are the following
#rectangleCoordinates = {'top': t, 
#                       'right': r, 
#                       'bottom': b, 
#                       'left': l}

#######################################
# macros go here for use of use
#####################################
TOP_START = 10
RIGHT_START = 350
BOTTOM_START = 220
LEFT_START = 590

BORDER_LIMIT = 10


# NOTE these functions should have checks via assert
# so that they don't something stupid on accident
# (or just don't move if they cant)
def moveRectangleLeft(rectangleCoordinates, amount):
    rectangleCoordinates['right'] -= amount
    rectangleCoordinates['left'] -= amount


def moveRectangleRight(rectangleCoordinates, amount):
    rectangleCoordinates['right'] += amount
    rectangleCoordinates['left'] += amount

def moveRectangleDown(rectangleCoordinates, amount):
    rectangleCoordinates['top'] += amount
    rectangleCoordinates['bottom'] += amount


def moveRectangleUp(rectangleCoordinates, amount):
    rectangleCoordinates['top'] -= amount
    rectangleCoordinates['bottom'] -= amount

def showMessage(message, cloned_image, frameShape):
    cv2.putText(cloned_image, message, 
                (int(frameShape['width']/10), int(frameShape['height']/10)), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0,0,255), 2)


def doACounterClockwiseCircle(rectangleCoordinates, frameShape):
    conditionGoLeft = rectangleCoordinates['top'] == TOP_START \
                        and rectangleCoordinates['bottom'] == BOTTOM_START  \
                        and rectangleCoordinates['right'] > BORDER_LIMIT

    conditionGoDown = rectangleCoordinates['bottom'] < frameShape['height'] - BORDER_LIMIT \
                        and rectangleCoordinates['right'] == BORDER_LIMIT 
                        #and rectangleCoordinates['left'] == BOTTOM_START + (LEFT_START - RIGHT_START)

    conditionGoRight = rectangleCoordinates['bottom'] == frameShape['height'] - BORDER_LIMIT\
                        and rectangleCoordinates['left'] < frameShape['width'] - BORDER_LIMIT
                        # and rectangleCoordinates['top'] == BORDER_LIMIT + (BOTTOM_START - TOP_START)\

    conditionGoUp = rectangleCoordinates['top'] > BORDER_LIMIT \
                        and rectangleCoordinates['left'] == frameShape['width'] - BORDER_LIMIT
                        #and rectangleCoordinates['right'] == frameShape['width'] - BORDER_LIMIT - (LEFT_START - RIGHT_START) \

    if conditionGoLeft:
        moveRectangleLeft(rectangleCoordinates, 2)

    if conditionGoDown:
        moveRectangleDown(rectangleCoordinates, 2)

    if conditionGoRight:
        moveRectangleRight(rectangleCoordinates, 2)

    if conditionGoUp:
        moveRectangleUp(rectangleCoordinates, 2)

        



