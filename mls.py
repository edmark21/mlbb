import os, sys, time


a = "*.unity3d"
s = " "
#a
p = "/Art/android/"
#ui
u = "/UI/android/"
#audio
au = "/Audio/android/"

b = "/storage/emulated/0/"
c = "/storage/emulated/0/Android/data/com.mobile.legends/files/dragon2017/assets"
#d = "
#e = "

final = "/storage/emulated/0/download/"


w = '''

    *****************************
            ML Skin Script
    *****************************
            \ Created By /
             ------------
                3DM4RK
             
    
    
    '''
role = '''



.  .   .   .     .                 .   
|\/| _ |_ *| _   |    _  _  _ ._  _| __
|  |(_)[_)||(/,  |___(/,(_](/,[ )(_]_) 
                        ._|            

 
 '''
print(w)    
print(role)


file = input("Enter Code: ")


def unzip():
	os.system("unzip " + final + file + ".zip")
unzip()
		
def main():
	#fn = input("Enter Skin Folder Name: ")
	sounds = input("File contain Audio [y/n]: ")
	#art
	os.system("cp " + file + p + a + s + c + p)
	#ui
	
	os.system("cp " + file + u + a + s + c + u)
	#audio
	if not sounds == "n":
		os.system("cp " + file + au + a + s + c + au)
	else:
		print ("no audio files....")
	os.system("rm -r " + file)
	
	print("************************")
	print("Skin Added Successfully..")
	print("************************")

main()	
    
            
	
