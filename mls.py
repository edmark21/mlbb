import importlib.util, requests
import requests, zipfile, io
import os, sys


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

final = "/storage/emulated/0/Download/"



def zp():
	dl = input("Download File link [y/n]: ")
	if dl == "y" or dl == "Y" or dl == "yes" or dl == "YES" or dl == "Yes":
		download = input("Enter Code: ")
		print("Downloading Please wait...")
		r = requests.get("https://drive.google.com/uc?id=" + download + "&export=download")
		z = zipfile.ZipFile(io.BytesIO(r.content))
		z.extractall()
	else:
		print("file already")
	





		
def main():
	file = input("Enter Skin Code: ")
	#fn = input("Enter Skin Folder Name: ")
	sounds = input("Does File contain Audio Folder [y/n]: ")
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

    
            
	



# For illustrative purposes.
package_name = 'requests'

spec = importlib.util.find_spec(package_name)
if spec is None:
    print(package_name +" is not installed")
    print("Install it via: pip3 install " + package_name)
else:
    zp()
    main()
    






