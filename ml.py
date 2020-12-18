import importlib.util
import requests, zipfile, io
import os, sys, time


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


ll = '''\033[1;33m
	
		[1] Install Skin
		[2] Buckup File
		[3] Remove all Skin
			
			
		\033[37m	'''



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
		print("Activating Skin Please Wait..")
		try:
			r = requests.get("https://drive.google.com/uc?id=" + download + "&export=download")
			z = zipfile.ZipFile(io.BytesIO(r.content))
			z.extractall()
			main()
		except:
			print("No Internet Connection / Invalid Code")
			print("please try Again")
			os.system("exit")
	else:
		print("Thanks for using this script...")
	


def install():
	print("\033[1;36m", w)
	print(role)
	print(ll)
	want = input("Select option [1-3]: ")
	if want == "1":
		zp()
	elif want == "2":
		print("backuping your data..")
	elif want == "3":
		print("Removing all Skin...")
	else:
		print("Invalid Command")
		time.sleep(2)
		os.system("clear")
		print(w)
		print(role)
		
		install()
		


		
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
	
	print("\033[32m************************")
	print("Skin Added Successfully..")
	print("************************\033[37m")

    
            
	


def check():
	try:
		import requests
		package_name = 'requests'
		spec = importlib.util.find_spec(package_name)
		print("\033[32mrequests found ✓\033[37m")
		time.sleep(2)
		os.system("clear")
		install()
	except:
		print("\033[31mrequests not found [x],\033[37m" + " Installing")
		os.system("pip3 install requests")
		print("python mls.py")
check()    
    






