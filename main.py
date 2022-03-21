import os,subprocess,tkinter,gdown 

#-----------------------------------------------------------------------------------------------------------
zip_link = r'https://drive.google.com/drive/folders/1U5Uj3b36uVhCyv35jsmVKzBmQhtw0uHD?usp=sharing'
chrome_link = 'ChromeSetup'
fier_fox_link = "Firefox Installer"
note_plus_link = "npp.8.2.1.Installer.x64"
java_link = "jre-8u321-windows-x64"
seven_link = "7z2107-x64"
office_365_link = "OfficeSetup"
adobe_acroat_link = "link adob acrobat"
discord_link = "DiscordSetup"
vs_code_link = "VSCodeUserSetup-x64-1.65.2"
#-----------------------------------------------

def download():
  gdown.download_folder(zip_link)
  warrnig.destroy



warrnig = tkinter.Tk()
warrnig_hitght = 700
warrning_width = 700
warrnig_sceen = tkinter.Canvas(warrnig, width = warrning_width, height = warrnig_hitght, bg = "white")
module_installer_button = tkinter.Button(warrnig,text="Downlaod!", bg="blue",command=download)
module_installer_message = tkinter.Label(warrnig,height=1, width= 100,text="CLick to downlaod nesser files ")
module_installer_message.pack()
module_installer_button.pack()
if not os.path.isdir('\Downlaod_exe'):
  warrnig_sceen.destroy
warrnig_sceen.mainloop()
  

#-----------------------------------------------------------------------------------------------------------
# cahgne buttons colors

def chrome_change_color():
    if chrome_button.cget('bg') == ('red'):
      chrome_button.config(bg= "green")
    else:
      chrome_button.config(bg= "red")
def fier_fox_button_color_change():
    if fier_fox_button.cget('bg') == ('red'):
      fier_fox_button.config(bg= "green")
    else:
      fier_fox_button.config(bg= "red")
def note_plus_color_change():
  if note_plus_button.cget('bg') == ('red'):
    note_plus_button.config(bg='green')
  else:
    note_plus_button.config(bg='red')
def java_color_change():
  if java_button.cget('bg') == ('red'):
      java_button.config(bg= "green")
  else:
    java_button.config(bg= "red")
def seven_zip_color_change():
  if seven_zip_button.cget('bg') == ('red'):
      seven_zip_button.config(bg= "green")
  else:
    seven_zip_button.config(bg= "red")
def office_365_color_change():
  if office_365_button.cget('bg') == ('red'):
      office_365_button.config(bg= "green")
  else:
    office_365_button.config(bg= "red")
def adob_acrobat_color_change():
  if adobe_acrobat_button.cget('bg') == ('red'):
      adobe_acrobat_button.config(bg= "green")
  else:
    adobe_acrobat_button.config(bg= "red")
def discord_color_change():
  if discord_button.cget('bg') == ('red'):
      discord_button.config(bg= "green")
  else:
    discord_button.config(bg= "red")
def vs_code_color_cahnge():
  if vs_code_button.cget('bg') == ('red'):
    vs_code_button.config(bg= "green")
  else:
      vs_code_button.config(bg= "red")
#-----------------------------------------------------------------
def wget_installer():
  list_of_button = [chrome_button,note_plus_button,fier_fox_button,java_button,seven_zip_button,office_365_button,adobe_acrobat_button,discord_button,vs_code_button]
  list_of_link = [chrome_link,note_plus_link,fier_fox_link,java_link,seven_link,office_365_link,adobe_acroat_link,discord_link,vs_code_link]

  try:
    os.remove('Download_links.bat')
  except FileNotFoundError:
    print("")
  print(os.listdir)
  try:
    download_links_file = open("Download_links.bat",'w')
    download_links_file.write('\n')
  except FileExistsError:
    print("Downlaod_links.bat already exixst no need to make file ")
  for i in range(len(list_of_button)):
    if list_of_button[i].cget('bg') == 'green':
      download_links_file.writelines("Downlaod_exe\\" + list_of_link[i] + ".exe")
      download_links_file.write('\n')
  download_links_file.close()
#-----------------------------------------------------------------------------------------------------------Downlaoding 
#creating file for downloaded files
  subprocess.call(r'Download_links.bat')

#-----------------------------------------------------------------------------------------------------------
def install_all():
  #chaning coulr
  chrome_button.config(bg="green")
  note_plus_button.config(bg="green")
  fier_fox_button.config(bg="green")
  java_button.config(bg="green")
  seven_zip_button.config(bg="green")
  office_365_button.config(bg="green")
  adobe_acrobat_button.config(bg="green")
  discord_button.config(bg="green")
  vs_code_button.config(bg="green")
  #done chaning corer
  print ("Installing all apps")    #starting install of apps 
  print ("done")
#script to install all the appps

  # creates in Canvis 
root = tkinter.Tk()
root.title('Auto Installer ')
screen_width = 700
screen_height = 400
screen = tkinter.Canvas(root, width = screen_width, height = screen_height, bg = "white")
# text to be dispalyed

greeting_windows = tkinter.Label(root, height = 1, width = 100, text= "Click the aplicaions you would like installed, applicaons in red will not be innstaled o nly the ones in green")
#buttons  be dispalyed
#-----------------------------------------------------------------------------------------------------------
install_button = tkinter.Button(root, text= "Install",command=wget_installer)
install_all_button = tkinter.Button(root,text="Select All",command= install_all, )
exit_button = tkinter.Button(root, text= "EXIT", command= root.destroy)

chrome_button = tkinter.Button(root, text="Chrome", bg="red", command= chrome_change_color,)
fier_fox_button = tkinter.Button(root, text="Fiier Fox", bg="red", command= fier_fox_button_color_change,)
note_plus_button = tkinter.Button(root, text="Note++", bg= "red" ,command= note_plus_color_change, )
java_button = tkinter.Button(root,text="JAVA",bg="red",command= java_color_change)
seven_zip_button = tkinter.Button(root,text="7-zip",bg="red",command= seven_zip_color_change)
office_365_button = tkinter.Button(root,text="Office 365",bg="red",command= office_365_color_change)
adobe_acrobat_button = tkinter.Button(root,text="Adobe Acrobat",bg="red",command= adob_acrobat_color_change)
discord_button = tkinter.Button(root,text="Discord",bg="red",command= discord_color_change)
vs_code_button =  tkinter.Button(root,text="VS Code",bg="red",command =vs_code_color_cahnge)
#------------------------------------------------------------------------------------------------------------
  
#paking
greeting_windows.pack()
chrome_button.pack()
fier_fox_button.pack()
note_plus_button.pack()
java_button.pack()
seven_zip_button.pack()
office_365_button.pack()
adobe_acrobat_button.pack()
discord_button.pack()
vs_code_button.pack()
install_button.pack()

install_all_button.pack()
exit_button.pack()
  #downloading the selected aplications
root.mainloop()
  # x = str(input("url: "))
    #download(x)

    #ask wich apps
    #this is for debug

