import os, sys, time
os.system("clear")

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


file = input("Enter Code: ")


def unzip():
	with ZipFile(final + file + ".zip", 'r') as zipObj:
		zipObj.extractall()
unzip()		
		
def main():
	#fn = input("Enter Skin Folder Name: ")
	sounds = input("File contain Audio [y/n]: ")
	#art
	os.system("cp " + b + file + "/" + p + a + s + c + p)
	#ui
	os.system("cp " + b + file + "/" + u + a + s + c + u)
	#audio
	if not sounds == "n":
		os.system("cp " + b + file + "/" + au + a + s + c + au)
	else:
		print ("no audio files....")
	os.system("rm -r " + file)
	print("Skin replace Successfully..")

main()	
    
            
print(w)    
print(role)

main()
	
