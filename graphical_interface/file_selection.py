#!/usr/bin/python
# Written by ALGaenssle in 2024
# CLASS
# Obtain all required information which data should be imported

import os
import tkinter as tk
import tkinter.filedialog

## ====================================================================
## Create class for storing file locations
class FileSelection():
	def __init__(self):
		self.input_path = ""
		self.file_list = []
		self.selection_list = []
		self.output_path = ""
		self.file_name = ""
		self.file_ending = ".txt"

	## FOLDERS --------------------------------------------------------
	# Get input folder
	def get_input_folder(self, ask=True):
		if ask:
			self.input_path = tk.filedialog.askdirectory()
		else:
			self.input_path = ""
		self.get_file_list()
		self.output_path = os.path.dirname(self.input_path)
		self.file_name = os.path.basename(
			os.path.normpath(self.output_path))

	# Set new output folder
	def get_output_folder(self):
		self.output_path = tk.filedialog.askdirectory()

	## INPUT FILES ----------------------------------------------------
	# Get list of input files
	def get_file_list(self):
		file_list = []
		for file_name in os.listdir(os.path.abspath(self.input_path)):
			if (file_name.endswith(self.file_ending.lower()) \
				or file_name.endswith(self.file_ending.upper()) \
				and not file_name in file_list):
				file_list.append(file_name)
		file_list.sort()
		self.file_list = file_list
		self.selection_list = self.file_list