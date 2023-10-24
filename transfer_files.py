import os, shutil

'''
Beware:
	*this is in testing face
	*you may lose your data, do this at your own risk
	*if same name exists in the destination folder, 
		moved-file with the same name will replace the older file
'''

class Transfer_Files:
	def __init__(self):
		cur_loc = os.getcwd()
		#print(cur_loc)
		self.source = cur_loc+'\\' #source auto generated

		#Put ur desired location in the string (plz use double \\ instead of \)
		your_desired_loc = 'E:\\Generated from downloads'

		self.destination = your_desired_loc+'\\'
		self.moved_files = {}
		self.file_count = 0

		#Commands
		print('Press 1 : Move Courses')
		print('Press 2 : Move Images')
		print('Press 3 : Move Applications')
		print('Press 4 : Move Videos')
		n = int(input())

		os.chdir(self.source)

		for file in os.listdir():
			#print(file)
			if n == 1:
				self.courses(file)
			elif n == 2:
				self.images(file)
			elif n == 3:
				self.applications(file)
			elif n == 4:
				self.videos(file)

		print('*******************************')
		print('Total moved files:', self.file_count)
		print("Moved files:")
		if self.file_count == 0:
			print("There's no file to move")
		else:
			self.show_moved_files()

	def store_moved_files(self, file, moved_path):
		self.file_count += 1
		if moved_path not in self.moved_files:
			self.moved_files[moved_path] = [file]
		else:
			self.moved_files[moved_path].append(file)

	def show_moved_files(self):
		for folder,files in self.moved_files.items():
			print(folder, ':')
			for file in files:
				print(file, end="\n")
			print('-------------------------------')

	def courses(self, file):
		item_type_folder = self.destination+'Courses'
		if not os.path.isdir(item_type_folder):
			os.mkdir(item_type_folder)

		#optimization: use dict instead of list, ex: courses = {'CSE':['220','221'], 'MAT':['215','216']}
		courses = {
					'CSE':['220', '221', '320','230', '111', '110', '260', 
						'250', '331', '330', '251', '340', '370', '321'],
					'MAT':['110','120','215','216','092','101'],
					'PHY':['110','111','112'],
					'STA':['201'],
					'BIO':[],
					'CHE':[]
					}
		'''
					'cse':['220', '221', '320','230', '111', '110', '260', 
						'250', '331', '330', '251', '340', '370', '321'],
					'mat':['110','120','215','216','092','101'],
					'phy':['110','111','112']
		course_name = ['CSE','MAT', 'cse', 'mat', 'Cse', 'Mat']
		course_code = ['220', '221', '320', '216', '215', '230', '111', '110', '260', 
						'250', '331', '330', '251', '340', '370', '321']

		for name in course_name:
			for code in course_code:
		'''


		for name, codes in courses.items():
			for code in codes:
				#file name format
				t = [name+code,name+'_'+code,name+'-'+code] #type of file name
				#moving condition
				if any(i in file.upper() for i in t):
				#if t[0][0] in file.upper() or t[1][0] in file.upper() or t[2][0] in file.upper():
					#moving logic
					new_path = item_type_folder+'\\'+name+code
					if not os.path.isdir(new_path):
						os.mkdir(new_path)
						shutil.move(self.source+file, item_type_folder+'\\'+name+code+'\\'+file)
					else:
						shutil.move(self.source+file, item_type_folder+'\\'+name+code+'\\'+file)

					#show which files moved to which location
					self.store_moved_files(file, new_path)

	def images(self, file):
		item_type_folder = self.destination+'Images'
		if not os.path.isdir(item_type_folder):
			os.mkdir(item_type_folder)

		image_extentions = ['png', 'peg', 'jpg', 'gif', 'tif','iff','bmp','raw']
		#print(file[-3:])
		if file[-3:] in image_extentions:
			shutil.move(self.source+file, item_type_folder+'\\'+file)
			self.store_moved_files(file, item_type_folder)

	def applications(self, file):
		item_type_folder = self.destination+'Applications'
		if not os.path.isdir(item_type_folder):
			os.mkdir(item_type_folder)

		if file[-3:] == 'exe':
			shutil.move(self.source+file, item_type_folder+'\\'+file)
			self.store_moved_files(file, item_type_folder)

	def videos(self, file):
		item_type_folder = self.destination+'Videos'
		if not os.path.isdir(item_type_folder):
			os.mkdir(item_type_folder)

		video_extentions = ['m4a', 'mp4', 'avi', 'mov', 'wmv', 'flv', 'webm']
		#print(file[-3:])
		if file[-3:] in video_extentions:
			shutil.move(self.source+file, item_type_folder+'\\'+file)
			self.store_moved_files(file, item_type_folder)

if __name__ == '__main__':
	try:
		Transfer_Files()
	except BaseException:
	    import sys
	    print(sys.exc_info()[0])
	    import traceback
	    print(traceback.format_exc())
	finally:
		print('*******************************')
		print("Press Enter to continue ...")
		input()

'''
Todo:
	*[done]put application files in one folder, using split for last 3 char (exe) 
	*[done]put images files in one folder, using split for last 3 char (png,jpg) 
	*[done]videos (m4a,mp4,avi,mov,wmv,flv, webm) 
	*if same name exists, rename the moved-file as _copy(1) or something like this
	*gui (PySimpleGUI)?
	*copy option?
'''

'''
bugs:
	minor: 
		*[Fixed]capital and small letters (python case sensitive but windows sees same)
		*if same name, file replaces (can be named as filename_copy)
	major: Dunno
'''
