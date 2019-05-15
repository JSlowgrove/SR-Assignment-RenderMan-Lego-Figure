This is the code for my Renderman Assignment. The code is in Python.  
  
This code can take input commands to generate different variations of lego figure.  
  
Commands:  
-ct or --chest-type sets the type of pattern the chest will have, current options are ["check","blank","perlin","camo"] (Example command: python assignment.py -ct check)  
-cbc or --chest-base-colour sets the base colour of the chest, the values can be either values of either 0.0-1.0 or 0-255 and have to have the format set as a command after either as -1 or 255 (Example command:  python assignment.py -cbc 0.0,0.4,1 -1)(Example command:  python assignment.py -cbc 0,30,255 -255)  
-cdc or --chest-detail-colour sets the detail colour of the chest, the values can be either values of either 0.0-1.0 or 0-255 and have to have the format set as a command after either as -1 or 255 (Example command:  python assignment.py -cdc 0.0,0.4,1 -1)(Example command:  python assignment.py -cdc 0,30,255 -255)  
-lc or --legs-colour sets the colour of the legs, the values can be either values of either 0.0-1.0 or 0-255 and have to have the format set as a command after either as -1 or 255 (Example command:  python assignment.py -lc 0.0,0.4,1 -1)(Example command:  python assignment.py -lc 0,30,255 -255)  
-hc or --head-colour sets the colour of the head, the values can be either values of either 0.0-1.0 or 0-255 and have to have the format set as a command after either as -1 or 255 (Example command:  python assignment.py -hc 0.0,0.4,1 -1)(Example command:  python assignment.py -hc 0,30,255 -255)  
-alt or --alternate-angle sets the angle of the scene to that of the alternate angle (Example command: python assignment.py -alt)  
-o or --output sets the type of output to generate, current options are ["it","rib","exr"] (Example command: python assignment.py -o exr)   
-dv or --dirt-value sets the amount of dirt to apply to the figure, between 0.0 and 1.0 (Example command: python assignment.py -dv 0.5)   
-d or --damage sets the seed for the damage to apply to the figure as an integer, 0 is for no damage (Example command: python assignment.py -d 3)   
-fn or --file-name sets a custom output filename (Example command: python assignment.py -fn my_filename)  
  
HDRI: https://hdrihaven.com/hdri/?c=indoor&h=aerodynamics_workshop  
Table Texture: https://freestocktextures.com/texture/wooden-plank-wall,1111.html  

