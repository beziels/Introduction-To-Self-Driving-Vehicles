## alternative answers
hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
v = hsv[:,:,2]
redRegion = v[4:12, 12:22]
yellowRegion = v[13:21, 12:22]
greenRegion = v[22:31, 12:22]
feature = [np.mean(redRegion), np.mean(yellowRegion ), np.mean(greenRegion )]
return feature


###

def create_feature(rgb_image):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # Detect red light
    output_hsv= np.copy(hsv)[2:29, 10:27]
    mask1 = cv2.inRange(output_hsv, np.array([0,20,150]), np.array([10,255,255]))
    mask2 = cv2.inRange(output_hsv, np.array([155,20,150]), np.array([179,255,255]))
    mask = mask1 + mask2
    output_hsv[np.where(mask==0)] = 0
    red_brightness = np.sum(output_hsv[:,:,2])

    # Detect yellow light
    output_hsv= np.copy(hsv)[2:29, 10:27]
    mask = cv2.inRange(output_hsv, np.array([13,10,150]), np.array([30,255,255]))
    output_hsv[np.where(mask==0)] = 0
    yellow_brightness = np.sum(output_hsv[:,:,2])

    # Detect green light
    output_hsv= np.copy(hsv)[2:29, 10:27]
    mask = cv2.inRange(output_hsv, np.array([75,10,100]), np.array([100,255,255]))
    output_hsv[np.where(mask==0)] = 0
    green_brightness = np.sum(output_hsv[:,:,2])

    ## Create and return a feature value and/or vector
    feature = [red_brightness, yellow_brightness, green_brightness]

    return feature
