from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            print(filename)
            i = 1
            if filename != 'Razzrr':
                # try:
                new_name = filename
                extension = 'noname'
                try:
                    extension = str(os.path.splitext(folder_to_track + '\\' + filename)[1])
                    path = extensions_folders[extension]
                except Exception:
                    extension = 'noname'

                now = datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")

                folder_destination_path = extensions_folders[extension]
                            
                year_exists = False
                month_exists = False
                for folder_name in os.listdir(extensions_folders[extension]):
                    if folder_name == year:
                        folder_destination_path = extensions_folders[extension] + "\\" +year
                        year_exists = True
                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = extensions_folders[extension] + "\\" + year + "\\" + month
                                month_exists = True
                if not year_exists:
                    os.mkdir(extensions_folders[extension] + "\\" + year)
                    folder_destination_path = extensions_folders[extension] + "\\" + year
                if not month_exists:
                    os.mkdir(folder_destination_path + "\\" + month)
                    folder_destination_path = folder_destination_path + "\\" + month


                file_exists = os.path.isfile(folder_destination_path + "\\" + new_name)
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(folder_to_track + '\\' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + filename)[1]
                    new_name = new_name.split("\\")[4]
                    file_exists = os.path.isfile(folder_destination_path + "\\" + new_name)
                src = folder_to_track + "\\" + filename

                new_name = folder_destination_path + "\\" + new_name
                os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "C:\\Users\\Razzrr\\Uncategorized",
#Audio
    '.aif' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.cda' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.mid' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.midi' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.mp3' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.mpa' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.ogg' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.wav' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.wma' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.wpl' : "C:\\Users\\Razzrr\\Media\\Audio",
    '.m3u' : "C:\\Users\\Razzrr\\Media\\Audio",
#Text
    '.txt' : "C:\\Users\\Razzrr\\Text\\Textfiles",
    '.doc' : "C:\\Users\\Razzrr\\Text\\Word",
    '.docx' : "C:\\Users\\Razzrr\\Text\\Word",
    '.odt ' : "C:\\Users\\Razzrr\\Text\\Textfiles",
    '.pdf': "C:\\Users\\Razzrr\\Text\\PDF",
    '.rtf': "C:\\Users\\Razzrr\\Text\\Textfiles",
    '.tex': "C:\\Users\\Razzrr\\Text\\Textfiles",
    '.wks ': "C:\\Users\\Razzrr\\Text\\Textfiles",
    '.wps': "C:\\Users\\Razzrr\\Text\\Textfiles",
    '.wpd': "C:\\Users\\Razzrr\\Text\\Textfiles",
#Video
    '.3g2': "C:\\Users\\Razzrr\\Media\\Video",
    '.3gp': "C:\\Users\\Razzrr\\Media\\Video",
    '.avi': "C:\\Users\\Razzrr\\Media\\Video",
    '.flv': "C:\\Users\\Razzrr\\Media\\Video",
    '.h264': "C:\\Users\\Razzrr\\Media\\Video",
    '.m4v': "C:\\Users\\Razzrr\\Media\\Video",
    '.mkv': "C:\\Users\\Razzrr\\Media\\Video",
    '.mov': "C:\\Users\\Razzrr\\Media\\Video",
    '.mp4': "C:\\Users\\Razzrr\\Media\\Video",
    '.mpg': "C:\\Users\\Razzrr\\Media\\Video",
    '.mpeg': "C:\\Users\\Razzrr\\Media\\Video",
    '.rm': "C:\\Users\\Razzrr\\Media\\Video",
    '.swf': "C:\\Users\\Razzrr\\Media\\Video",
    '.vob': "C:\\Users\\Razzrr\\Media\\Video",
    '.wmv': "C:\\Users\\Razzrr\\Media\\Video",
#Images
    '.ai': "C:\\Users\\Razzrr\\Images",
    '.bmp': "C:\\Users\\Razzrr\\Images",
    '.gif': "C:\\Users\\Razzrr\\Images",
    '.ico': "C:\\Users\\Razzrr\\Images",
    '.jpg': "C:\\Users\\Razzrr\\Images",
    '.jpeg': "C:\\Users\\Razzrr\\Images",
    '.png': "C:\\Users\\Razzrr\\Images",
    '.ps': "C:\\Users\\Razzrr\\Images",
    '.psd': "C:\\Users\\Razzrr\\Images",
    '.svg': "C:\\Users\\Razzrr\\Images",
    '.tif': "C:\\Users\\Razzrr\\Images",
    '.tiff': "C:\\Users\\Razzrr\\Images",
    '.CR2': "C:\\Users\\Razzrr\\Images",
#Internet
    '.asp': "C:\\Users\\Razzrr\\Internet",
    '.aspx': "C:\\Users\\Razzrr\\Internet",
    '.cer': "C:\\Users\\Razzrr\\Internet",
    '.cfm': "C:\\Users\\Razzrr\\Internet",
    '.cgi': "C:\\Users\\Razzrr\\Internet",
    '.pl': "C:\\Users\\Razzrr\\Internet",
    '.css': "C:\\Users\\Razzrr\\Internet",
    '.htm': "C:\\Users\\Razzrr\\Internet",
    '.js': "C:\\Users\\Razzrr\\Internet",
    '.jsp': "C:\\Users\\Razzrr\\Internet",
    '.part': "C:\\Users\\Razzrr\\Internet",
    '.php': "C:\\Users\\Razzrr\\Internet",
    '.rss': "C:\\Users\\Razzrr\\Internet",
    '.xhtml': "C:\\Users\\Razzrr\\Internet",
#Compressed
    '.7z': "C:\\Users\\Razzrr\\Compressed",
    '.arj': "C:\\Users\\Razzrr\\Compressed",
    '.deb': "C:\\Users\\Razzrr\\Compressed",
    '.pkg': "C:\\Users\\Razzrr\\Compressed",
    '.rar': "C:\\Users\\Razzrr\\Compressed",
    '.rpm': "C:\\Users\\Razzrr\\Compressed",
    '.tar.gz': "C:\\Users\\Razzrr\\Compressed",
    '.z': "C:\\Users\\Razzrr\\Compressed",
    '.zip': "C:\\Users\\Razzrr\\Compressed",
#Disc
    '.bin': "C:\\Users\\Razzrr\\Disc",
    '.dmg': "C:\\Users\\Razzrr\\Disc",
    '.iso': "C:\\Users\\Razzrr\\Disc",
    '.toast': "C:\\Users\\Razzrr\\Disc",
    '.vcd': "C:\\Users\\Razzrr\\Disc",
#Data
    '.csv': "C:\\Users\\Razzrr\\Programming\\Database",
    '.dat': "C:\\Users\\Razzrr\\Programming\\Database",
    '.db': "C:\\Users\\Razzrr\\Programming\\Database",
    '.dbf': "C:\\Users\\Razzrr\\Programming\\Database",
    '.log': "C:\\Users\\Razzrr\\Programming\\Database",
    '.mdb': "C:\\Users\\Razzrr\\Programming\\Database",
    '.sav': "C:\\Users\\Razzrr\\Programming\\Database",
    '.sql': "C:\\Users\\Razzrr\\Programming\\Database",
    '.tar': "C:\\Users\\Razzrr\\Programming\\Database",
    '.xml': "C:\\Users\\Razzrr\\Programming\\Database",
    '.json': "C:\\Users\\Razzrr\\Programming\\Database",
#Executables
    '.apk': "C:\\Users\\Razzrr\\Executables",
    '.bat': "C:\\Users\\Razzrr\\Executables",
    '.com': "C:\\Users\\Razzrr\\Executables",
    '.exe': "C:\\Users\\Razzrr\\Executables",
    '.gadget': "C:\\Users\\Razzrr\\Executables",
    '.jar': "C:\\Users\\Razzrr\\Executables",
    '.wsf': "C:\\Users\\Razzrr\\Executables",
#Fonts
    '.fnt': "C:\\Users\\Razzrr\\Fonts",
    '.fon': "C:\\Users\\Razzrr\\Fonts",
    '.otf': "C:\\Users\\Razzrr\\Fonts",
    '.ttf': "C:\\Users\\Razzrr\\Fonts",
#Presentations
    '.key': "C:\\Users\\Razzrr\\Presentations",
    '.odp': "C:\\Users\\Razzrr\\Presentations",
    '.pps': "C:\\Users\\Razzrr\\Presentations",
    '.ppt': "C:\\Users\\Razzrr\\Presentations",
    '.pptx': "C:\\Users\\Razzrr\\Presentations",
#Programming
    '.c': "C:\\Users\\Razzrr\\Programming\\C&C++",
    '.class': "C:\\Users\\Razzrr\\Programming\\Java",
    '.dart': "C:\\Users\\Razzrr\\Programming\\Dart",
    '.py': "C:\\Users\\Razzrr\\Programming\\Python",
    '.sh': "C:\\Users\\Razzrr\\Programming\\Shell",
    '.swift': "C:\\Users\\Razzrr\\Programming\\Swift",
    '.html': "C:\\Users\\Razzrr\\Programming\\C&C++",
    '.h': "C:\\Users\\Razzrr\\Programming\\C&C++",
#Spreadsheets
    '.ods' : "C:\\Users\\Razzrr\\Text\\Excel",
    '.xlr' : "C:\\Users\\Razzrr\\Text\\Excel",
    '.xls' : "C:\\Users\\Razzrr\\Text\\Excel",
    '.xlsx' : "C:\\Users\\Razzrr\\Text\\Excel",
#System
    '.bak' : "C:\\Users\\Razzrr\\Disc\\System",
    '.cab' : "C:\\Users\\Razzrr\\Disc\\System",
    '.cfg' : "C:\\Users\\Razzrr\\Disc\\System",
    '.cpl' : "C:\\Users\\Razzrr\\Disc\\System",
    '.cur' : "C:\\Users\\Razzrr\\Disc\\System",
    '.dll' : "C:\\Users\\Razzrr\\Disc\\System",
    '.dmp' : "C:\\Users\\Razzrr\\Disc\\System",
    '.drv' : "C:\\Users\\Razzrr\\Disc\\System",
    '.icns' : "C:\\Users\\Razzrr\\Disc\\System",
    '.ico' : "C:\\Users\\Razzrr\\Disc\\System",
    '.ini' : "C:\\Users\\Razzrr\\Disc\\System",
    '.lnk' : "C:\\Users\\Razzrr\\Disc\\System",
    '.msi' : "C:\\Users\\Razzrr\\Disc\\System",
    '.sys' : "C:\\Users\\Razzrr\\Disc\\System",
    '.tmp' : "C:\\Users\\Razzrr\\Disc\\System",
}

folder_to_track = 'C:\\Users\\Razzrr\\Desktop'
folder_destination = 'C:\\Users\\Razzrr\\'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
