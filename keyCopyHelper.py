# keyframeCopyHelper.py
# v 1.0
# made by Han Syuan,Yang
# email:yang.hansyuan@gmail.com
# yanghansyuan.com



import maya.cmds as cmds
import maya.cmds as mc
import functools
#print "------------------------------Main program-----------------------------------------"

_mode=1
_key=2
global _attri
_attri=["tx","ty","tz","rx","ry","rz","null","null","null"] #default value of scale is null(uncheck)

global index
index=0

global ax_x_value
global ax_y_value
global ax_z_value

global ax_x
global ax_y
global ax_z

global tr_value
global ro_value
global sc_value

global tr
global ro
global sc



def createUI(pWindowTitle,pApplyCallback):
    
    windowID="myWindowID"
    
    if cmds.window(windowID,exists=True):
        cmds.deleteUI(windowID)
        
    cmds.window(windowID,title=pWindowTitle,sizeable=False,resizeToFitChildren=True)
    cmds.rowColumnLayout(numberOfColumns=4,columnWidth=[(1,100),(2,100),(3,100),(4,100)],columnOffset=[(1,"right",3)])
    cmds.text(label="copy mode:   ")
    cmds.radioCollection()
    cmds.radioButton(label="copy",select=True,onc="_mode = 1")   
    cmds.radioButton(label="opposite",onc="_mode = 2")
    cmds.separator(h=10,style="none") 
        
    cmds.text(label="key type :   ")
    cmds.radioCollection()
    cmds.radioButton(label="single key",onc="_key = 1")   
    cmds.radioButton(label="all key",select=True,onc="_key = 2")
    cmds.separator(h=10,style="none") 
                       
    

    cmds.text(label="axis :   ")
    global ax_x_value #recall global variable again
    global ax_y_value
    global ax_z_value
    global ax_x
    global ax_y
    global ax_z
    #query to global variable
    ax_x=cmds.checkBox( label="x",value=True) 
    ax_y=cmds.checkBox( label="y",value=True)
    ax_z=cmds.checkBox( label="z",value=True)
    ax_x_value=cmds.checkBox(ax_x,query=True,value=True)
    ax_y_value=cmds.checkBox(ax_y,query=True,value=True)
    ax_z_value=cmds.checkBox(ax_z,query=True,value=True)
#    print "ax_x_value1 = %s" %ax_x_value
#    print "ax_y_value1 = %s" %ax_y_value
#    print "ax_z_value1 = %s" %ax_z_value

    
    cmds.text(label="attribute :   ")
    global tr_value
    global ro_value
    global sc_value
    global tr
    global ro
    global sc
    tr=cmds.checkBox( label="translate",value=True)
    ro=cmds.checkBox( label="rotation",value=True)
    sc=cmds.checkBox( label="scale",value=False)
    tr_value=cmds.checkBox(tr,query=True,value=True)
    ro_value=cmds.checkBox(ro,query=True,value=True)
    sc_value=cmds.checkBox(sc,query=True,value=True)
    cmds.separator(h=10,style="none")   
   
    cmds.separator(h=10,style="none")
    cmds.separator(h=10,style="none")
    cmds.separator(h=10,style="none")
    cmds.separator(h=10,style="none")
    
    cmds.button(label="Apply",command=functools.partial(pApplyCallback))

    
    def cancelCallback(*pArgs):
        if cmds.window(windowID,exists=True):
            cmds.deleteUI(windowID)
            
    cmds.button(label="Cancel",command=cancelCallback)
    cmds.showWindow()


def checkList():
    #recall global variable again
    global ax_x_value 
    global ax_y_value
    global ax_z_value
    ax_x_value=cmds.checkBox(ax_x,query=True,value=True)
    ax_y_value=cmds.checkBox(ax_y,query=True,value=True)
    ax_z_value=cmds.checkBox(ax_z,query=True,value=True)
    global tr_value
    global ro_value
    global sc_value
    tr_value=cmds.checkBox(tr,query=True,value=True)
    ro_value=cmds.checkBox(ro,query=True,value=True)
    sc_value=cmds.checkBox(sc,query=True,value=True)
    
    global _attri
    if (ax_x_value):
        if tr_value == True:
            _attri[0]="tx"
        else:
            _attri[0]="null"
            
        if ro_value == True:
            _attri[3]="rx"
        else:
            _attri[3]="null"
            
        if sc_value == True:
            _attri[6]="sx"
        else:
            _attri[6]="null"
    else:
            _attri[0]="null"
            _attri[3]="null"
            _attri[6]="null"
            
            
    if ax_y_value == True:
        if tr_value == True:
            _attri[1]="ty"
        else:
            _attri[1]="null"
            
        if ro_value == True:
            _attri[4]="ry"
        else:
            _attri[4]="null"
            
        if sc_value == True:
            _attri[7]="sy"
        else:
            _attri[7]="null"
    else:
            _attri[1]="null"
            _attri[4]="null"
            _attri[7]="null"
            
            
    if (ax_z_value):
        if tr_value == True:
            _attri[2]="tz"
        else:
            _attri[2]="null"
            
        if ro_value == True:
            _attri[5]="rz"
        else:
            _attri[5]="null"
            
        if sc_value == True:
            _attri[8]="sz"
        else:
            _attri[8]="null"
    else:
        _attri[2]="null"
        _attri[5]="null"
        _attri[8]="null"
    print "--"
    print "_attri now is =%s" %_attri



def applyCallback(*pArgs):
#	print "-------------applyCallback----------------"
#	print "first mode= %s" %_mode 
#	print "first key= %s" %_key
#	print "attri key= %s" %_attri

# call function to chect array after press "apply"
	checkList()
	
	global index
	index=0

	
	nowJ=cmds.ls(orderedSelection=True)
	nowTime=mc.currentTime(q=1)
	for i in nowJ:
#	    print "now i= %s" %i
	    index += 1
	    if index >= 2:
	        targetJ=nowJ[index-1]
#	        print "target obj is = %s" %(targetJ) 
	        if _key == 2: #all key
	            cmds.copyKey(nowJ,at=_attri)
	            cmds.pasteKey(targetJ,at=_attri,option="replace")
	            if _mode == 2:
	                cmds.scaleKey(targetJ,at=_attri,valueScale=-1)
	        else: # single key

	            cmds.copyKey(nowJ,at=_attri,time=(nowTime,nowTime))
	            cmds.pasteKey(targetJ)
	            if _mode == 2:
	                cmds.scaleKey(targetJ,at=_attri,valueScale=-1,time=(nowTime,nowTime))
                
                    
	         



createUI("Keyframe Copy Helper",applyCallback)        



