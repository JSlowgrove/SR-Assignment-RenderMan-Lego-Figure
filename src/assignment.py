#!/usr/bin/python
# import the python renderman library
import prman
# import the system libraries
import sys
import sys,os.path,subprocess

# cube definition from Cube.py by Jon Macey (https://github.com/NCCA/Renderman/blob/master/Lecture1Intro/Cube.py)
def Cube(width=1.0,height=1.0,depth=1.0) :	
	w=width/2.0
	h=height/2.0
	d=depth/2.0
	ri.ArchiveRecord(ri.COMMENT, 'Cube Generated by Cube Function')
	#rear
	face=[-w,-h,d,-w,h,d,w,-h,d,w,h,d]								
	ri.Patch("bilinear",{'P':face})
	#front
	face=[-w,-h,-d,-w,h,-d,w,-h,-d,w,h,-d]								
	ri.Patch("bilinear",{'P':face})
	#left
	face=[-w,-h,-d,-w,h,-d,-w,-h,d,-w,h,d]									
	ri.Patch("bilinear",{'P':face})
	#right
	face=[w,-h,-d,w,h,-d,w,-h,d,w,h,d]								
	ri.Patch("bilinear",{'P':face})
	#bottom
	face=[w,-h,d,w,-h,-d,-w,-h,d,-w,-h,-d]								
	ri.Patch("bilinear",{'P':face})
	#top
	face=[w,h,d,w,h,-d,-w,h,d,-w,h,-d]								
	ri.Patch("bilinear",{'P':face})
	ri.ArchiveRecord(ri.COMMENT, '--End of Cube Function--')

# load osl shader definition is from scene.py by Jon Macey (https://github.com/NCCA/Renderman/blob/master/Lecture4Shaders/scene.py)
def checkAndCompileShader(shader) :
  	if os.path.isfile(shader+'.oso') != True  or os.stat(shader+'.osl').st_mtime - os.stat(shader+'.oso').st_mtime > 0 :
		print 'compiling shader %s' %(shader)
		try :
			subprocess.check_call(['oslc', shader+'.osl'])
		except subprocess.CalledProcessError :
			sys.exit('shader compilation failed')

# the definiton of the shader to use on the legs
def legsShader() :
	ri.Pattern('legsShader','legsShader', 
	{ 
		'color colourIn' : [0,0,1]
	})
	ri.Bxdf('PxrSurface', 'plastic',
	{
		'reference color diffuseColor' : ['legsShader:Cout'],
		'int diffuseDoubleSided' : [1]

	})

# the definiton of the shader to use on the head
def headShader() :
	ri.Pattern('headShader','headShader', 
	{ 
		'color colourIn' : [1,1,0]
	})
	ri.Bxdf('PxrSurface', 'plastic',
	{
		'reference color diffuseColor' : ['headShader:Cout'],
		'int diffuseDoubleSided' : [1]

	})

# the definiton of the shader to use on the chest
def chestShader() :
	ri.Pattern('chestShader','chestShader', 
	{ 
		'color colourIn' : [1,0,0]
	})
	ri.Bxdf('PxrSurface', 'plastic',
	{
		'reference color diffuseColor' : ['chestShader:Cout'],
		'int diffuseDoubleSided' : [1]

	})

# the definiton of the shader to use on the legs
def tableShader() :
	ri.Pattern('tableShader','tableShader', 
	{ 
		'string TextureName' : ["../img/table.tx"]
	})
	ri.Bxdf('PxrSurface', 'wood',
	{
		'reference color diffuseColor' : ['tableShader:Cout'],
		'int diffuseDoubleSided' : [1]

	})

# the definition of the scene to generate
def drawScene(ri) :
	##############################LEGO FIGURE BEGIN##############################
	ri.ArchiveRecord(ri.COMMENT, 'lego figure group')
	ri.TransformBegin()
	ri.Translate(0,0,-1)
	ri.Rotate(25, 0, 1, 0)

	#********************************HEAD BEGIN**********************************
	ri.ArchiveRecord(ri.COMMENT, 'head')
	# set the shader to use
	headShader()
	ri.AttributeBegin()
	ri.Attribute( 'identifier',{ 'name' :'head'})
	ri.TransformBegin() 
	ri.Translate(-0.1,0.5,0.1)
	ri.Rotate(90,1,0,0)
	ri.Cylinder(0.15,-0.125,0.125,360)
	ri.TransformEnd() 
	ri.AttributeEnd()
	#*********************************HEAD END***********************************

	#*******************************CHEST BEGIN**********************************
	ri.ArchiveRecord(ri.COMMENT, 'chest')
	# set the shader to use
	chestShader()
	ri.AttributeBegin()
	ri.Attribute( 'identifier',{ 'name' :'chest'})
	ri.TransformBegin() 
	ri.TransformEnd() 
	ri.AttributeEnd()
	#********************************CHEST END**********************************

	#********************************LEGS BEGIN**********************************
	ri.ArchiveRecord(ri.COMMENT, 'legs group')
	# set the shader to use
	legsShader()
	ri.TransformBegin()

	#-------------------------------WAIST BEGIN----------------------------------
	ri.ArchiveRecord(ri.COMMENT, 'waist')
	ri.AttributeBegin()
	ri.Attribute( 'identifier',{ 'name' :'waistLeg'})
	ri.TransformBegin() 
	ri.Translate(-0.12,-0.5,0.1)
	Cube(0.43,0.1,0.3)
	ri.Translate(-0.003,-0.145,0)
	ri.Rotate(90,0,1,0)
	ri.Cylinder(0.14,-0.02,0.02,360)
	ri.Translate(0,0,0.02)
	ri.Disk(0,0.14,360)
	ri.TransformEnd() 
	ri.AttributeEnd()
	#--------------------------------WAIST END-----------------------------------

	#------------------------------LEFT LEG BEGIN--------------------------------
	ri.ArchiveRecord(ri.COMMENT, 'left leg')
	ri.AttributeBegin()
	ri.Attribute( 'identifier',{ 'name' :'leftLeg'})
	ri.TransformBegin() 
	ri.Translate(0,-1.0,0)
	Cube(0.2,0.1,0.1)
	ri.Translate(0,0.15,0.15)
	Cube(0.2,0.4,0.2)
	ri.Translate(0,0.2,-0.04)
	ri.Rotate(90,0,1,0)
	ri.Cylinder(0.14,-0.1,0.1,360)
	ri.Translate(0,0,0.1)
	ri.Disk(0,0.14,360)
	ri.TransformEnd() 
	ri.AttributeEnd()
	#-------------------------------LEFT LEG END---------------------------------

	#-----------------------------RIGHT LEG BEGIN--------------------------------
	ri.ArchiveRecord(ri.COMMENT, 'right leg')
	ri.AttributeBegin()
	ri.Attribute( 'identifier',{ 'name' :'rightLeg'})
	ri.TransformBegin()
	ri.Translate(-0.25,-1.0,0)
	Cube(0.2,0.1,0.1)
	ri.Translate(0,0.15,0.15)
	Cube(0.2,0.4,0.2)
	ri.Translate(0,0.2,-0.04)
	ri.Rotate(90,0,1,0)
	ri.Cylinder(0.14,-0.1,0.1,360)
	ri.Translate(0,0,0.1)
	ri.Disk(0,0.14,360)
	ri.TransformEnd() 
	ri.AttributeEnd()
	#------------------------------RIGHT LEG END---------------------------------

	ri.TransformEnd()
	#*********************************LEGS END***********************************

	ri.TransformEnd() 
	###############################LEGO FIGURE END###############################

	#################################TABLE BEGIN#################################
	ri.ArchiveRecord(ri.COMMENT, 'table')
	# set the shader to use
	tableShader()
	ri.AttributeBegin()
	ri.Attribute( 'identifier',{ 'name' :'table'})
	ri.TransformBegin() 
	ri.Rotate(20,0,1,0)
	ri.Translate(-3,-1.3,-1.5)
	Cube(8,0.5,5)
	ri.TransformEnd() 
	ri.AttributeEnd()
	###################################TABLE END###################################

# the main function
if __name__ == '__main__':
	ri = prman.Ri() # create an instance of the RenderMan interface
	ri.Option("rib", {"string asciistyle": "indented"})

	filename = "assignment.rib"
	ri.ArchiveRecord(ri.COMMENT, 'assignment.rib')

	# Initalise Renderman in Python
	ri.Begin("__render") # render to it
	#ri.Begin(filename) # write to a .rib
	# Specify the output
	ri.Display("assignment.exr", "it", "rgba")
	# Specify 1080p resolution 1:1 pixel Aspect ratio
	ri.Format(1920,1080,1)
	# set the projection to perspective
	ri.Projection(ri.PERSPECTIVE,{ri.FOV:50}) 

	# set the depth of field (fstop, focal length, focal distance)
	ri.DepthOfField(3.2,0.01,1)

	# update render type to apply shadows
	ri.Hider('raytrace', {'int incremental' :[1]})
	ri.Integrator('PxrPathTracer', 'integrator')

	# compile the shaders
	checkAndCompileShader('legsShader')
	checkAndCompileShader('headShader')
	checkAndCompileShader('chestShader')
	checkAndCompileShader('tableShader')

	# Start the world
	ri.WorldBegin()

	###################################LIGHT BEGIN###################################
	#hdr light & background
	ri.TransformBegin()
	ri.Rotate(80,1,0,0)
	ri.Rotate(180,0,1,0)
	ri.Rotate(25,0,0,1)
	ri.Light("PxrDomeLight","hdrLight", {"float exposure" : [0], "string lightColorMap" : ["../img/hdr_4k.tx"]})
	ri.TransformEnd()
	####################################LIGHT END####################################

	ri.ArchiveRecord(ri.COMMENT, 'move everything back')
	ri.Translate(0,0,4)

	drawScene(ri)

	ri.WorldEnd()
	ri.End()