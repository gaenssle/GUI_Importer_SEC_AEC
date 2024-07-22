#!/usr/bin/python
# Written by ALGaenssle in 2024
## SCRIPT - FUNCTIONS
## All functions for importing and exporting SEC data

import pandas as pd
import re


## ===========================================================================
## Split file into the needed sections
def split_file(file_path, default_values):
	with open(file_path, "r", encoding=default_values.file_encoding) as file:
		line_list = file.readlines()

		# Get info from header section
		info_stop = line_list.index(default_values.info_stop)
		part_info = line_list[:info_stop]

		# Get raw data
		raw_start = line_list.index(default_values.raw_start, info_stop) + 1
		part_raw = line_list[raw_start:]
	
	return part_info, part_raw


## ===========================================================================
## Extracts information from the calibration and peak analysis
def extract_info(file_part, sample_line, info_values):
	data = {}
	for line in file_part:
		if line.startswith(sample_line):
			name = line.split("\t",1)[1].strip()
			name = name.replace(" ", "_")
		elif line.startswith(info_values):
			key, value = line.strip().split("\t",1)
			key = key.strip()
			data[key] = value
	return name, data


## ===========================================================================
## Extracts the raw signal data and appends it to the joined data
def extract_data(file_part, column):
	data = {}
	convert = detect_type(file_part[2].split("\t",1)[0])
	for line in file_part:
		if len(line) > 1 and line[3].isdigit():
			line = line.replace(" ","")

			volume = line.split("\t",1)[0]
			volume = convert_to_eng_format(volume, convert)
			volume = "{:.3f}".format(round(float(volume)*60)/60)

			signal = line.split("\t")[column]
			signal = convert_to_eng_format(signal, convert)
			signal = float(signal)

			data[volume] = signal
	return data


## ===========================================================================
## Export the data to files
def export_file(input_data, file_name, label="Time (min)"):
	data_frame = pd.DataFrame.from_dict(input_data)
	data_frame.index.name = label
	data_frame.to_csv(file_name, sep=";", index=True, header=True)
	print(f"File saved as: {file_name}\n")


## ===========================================================================
## Check each line for numbers and convert them to the international format
def convert_to_eng_format(number, convert):
	if convert:
		return number.replace(".","").replace(",", ".") 
	else:
		return number.replace(",","") 


## ===========================================================================
## Detect type of thousand and decimal separator
def detect_type(number):
	is_number = re.compile("[\d., +-]+")
	dot_comma = re.compile('[+-]?\d+(\.\d\d\d)*,\d+')
	comma_dot = re.compile('[+-]?\d+(,\d\d\d)*\.\d+')
	number = number.replace(" ", "")
	if is_number.fullmatch(number):	
		if dot_comma.fullmatch(number):
			return True
		elif comma_dot.fullmatch(number):
			return False
	return "Error"



