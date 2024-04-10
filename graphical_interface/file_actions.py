#!/usr/bin/python
# Written by ALGaenssle in 2024
# CLASS
# Obtain all required information which data should be imported

import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

## ====================================================================
## Create class for storing file locations
class FileActions():
	def __init__(self):
		self.input_path = ""
		self.file_list = []
		self.selection_list = []
		self.output_path = ""
		self.file_name = ""

	## FOLDERS --------------------------------------------------------
	# Get input folder
	def get_input_folder(self, file_list_string, ask=True):
		if ask:
			self.input_path = tk.filedialog.askdirectory()
		else:
			self.input_path = ""
		self.get_file_list(file_list_string)
		self.output_path = os.path.dirname(self.input_path)
		self.file_name = os.path.basename(
			os.path.normpath(self.output_path))
		self.set_truncated_path(self.input_path, input_path)
		self.set_truncated_path(self.output_path, output_path)
		self.set_truncated_path(self.file_name, file_name)

	# Set new output folder
	def get_output_folder(self):
		self.output_path = tk.filedialog.askdirectory()
		self.set_truncated_path(self.output_path, output_path)

	# truncate paths
	def set_truncated_path(self, path, variable):
		max_length = formatting.lab_max_length//4
		if len(path) > max_length:
			variable.set("..." + path[-max_length:])
		else:
			variable.set(path)

	## INPUT FILES ----------------------------------------------------
	# Get list of input files
	def get_file_list(self, file_list_string):
		file_list = []
		for file_name in os.listdir(os.path.abspath(self.input_path)):
			if  file_name.endswith(".txt") \
				or file_name.endswith(".TXT") \
				and not file_name in file_list:
				file_list.append(file_name)
		file_list.sort()
		self.file_list = file_list
		self.selection_list = self.file_list
		file_list_string.set(self.file_list)
		list_box_input_files.selection_set(0, "end")

	def select_deselect_file_list(self):
		if self.input_path == "":
			tkinter.messagebox.showwarning('Missing data','No input folder selected!')
			return
		self.selection_list = [list_box_input_files.get(index) for index in list_box_input_files.curselection()]
		if len(self.file_list) == len(self.selection_list):
			list_box_input_files.select_clear(0, "end")
		else:
			list_box_input_files.selection_set(0, "end")
		self.selection_list = [list_box_input_files.get(index) for index in list_box_input_files.curselection()]

	def submit_selection(self):
		if self.input_path == "":
			tkinter.messagebox.showwarning('Missing data','No input folder selected!')
			return
		self.selection_list = [list_box_input_files.get(index) for index in list_box_input_files.curselection()]
		if any(len(name.split("_",1)[0]) == 1 for name in self.file_list):
			rename = tkinter.messagebox.askquestion(title="Warning", message=f"Submitted file list contains names with no leading 0!\nDo you want to add them?", type='yesno')
			if rename:
				self.rename_files()
		tkinter.messagebox.showinfo(title="File list updated", message=f"Input file list now consists of {len(self.selection_list)} files")

	# Add 0 to Sample IDs under 10
	def rename_files(self, file_list_string):
		count = 0
		for index, name in enumerate(self.file_list):
			if len(name.split("_",1)[0]) == 1:
				print(f"Name to be changed: {name}")
				os.rename(os.path.join(self.input_path, name), os.path.join(self.input_path, "0" + name))
				self.file_list[index] = "0" + name
				count += 1
		file_list_string.set(self.file_list)		
		self.selection_list = [list_box_input_files.get(index) for index in list_box_input_files.curselection()]
		self.selection_list.sort()		
		self.file_list.sort()
		file_list_string.set(self.file_list)
		tkinter.messagebox.showinfo(title="Renamed files", message=f"Renamed {count} files")
	
	## EXPORT ---------------------------------------------------------
	# get file name (for exporting files)
	def get_file_name(self):
		self.file_name = entry_file_name.get()
		print(f"File name was changed to: {self.file_name}")
		tkinter.messagebox.showinfo(title="Changed file name", message=f"Name of output files was changed to '{self.file_name}'")

