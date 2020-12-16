import os, sys, time
import requests, zipfile, io


fname = 'requirements.txt'
with open(fname, 'r', encoding='utf-8') as fhd:
        for line in fhd:
            try:
            	exec("import " + line)
            except:
            	print("[ERROR] Missing module:", line)


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



dl = input("Download File link [y/n]: ")
if dl == "y" or dl == "Y" or dl == "yes" or dl == "YES" or dl == "Yes":
	download = input("Enter Download link: ")
	print("Downloading Please wait...")
	r = requests.get("https://drive.google.com/uc?id=" + download + "&export=download")
	z = zipfile.ZipFile(io.BytesIO(r.content))
	z.extractall()
	
else:
	print("file already")
	

file = input("Enter Code: ")



		
def main():
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

main()	
    
            
	
