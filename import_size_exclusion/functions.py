#!/usr/bin/python
# Written by ALGaenssle in 2024
## SCRIPT - FUNCTIONS
## All functions for importing and exporting SEC data

import pandas as pd


## ===========================================================================
## Split file into the needed sections
def split_file(file_path, default_values):
	with open(file_path, 'r', encoding=default_values.file_encoding) as file:
		line_list = file.readlines()

		# Get info from header section
		info_stop = line_list.index(default_values.info_stop)
		part_info = line_list[:info_stop]

		# Get raw data
		raw_start = line_list.index(default_values.raw_start, info_stop) + 1
		raw_stop = line_list.index(default_values.raw_stop, raw_start)
		part_raw = line_list[raw_start:raw_stop]

		# Get elution data
		elu_start = line_list.index(default_values.elu_start, raw_stop) + 1
		elu_stop = line_list.index(default_values.elu_stop, elu_start)
		part_elution = line_list[elu_start:elu_stop]
	
	return part_info, part_raw, part_elution


## ===========================================================================
## Extracts information from the calibration and peak analysis
def extract_info(file_part, info_values):
	data = {}
	for line in file_part:
		if line.startswith("Sample"):
			name = line.split(':',2)[2].rsplit('-',1)[0].strip()
		elif line.startswith(info_values):
			key, value = line.split(':',1)
			key = key.strip()
			value = value.split('\t')[1].strip()
			data[key] = value
	return name, data


## ===========================================================================
## Extracts the raw signal data and appends it to the joined data
def extract_data(file_part, column):
	data = {}
	for line in file_part:
		if len(line) > 1 and line[1].isdigit():
			line = line.replace(' ','')
			volume = "{:.3f}".format(round(
					float(line.split('\t')[0])*60)/60)
			signal = float(line.split('\t')[column])
			data[volume] = signal
	return data


## ===========================================================================
## Export the data to files
def export_file(input_data, file_name, label="Volumne"):
	data_frame = pd.DataFrame.from_dict(input_data)
	data_frame.index.name = label
	data_frame.to_csv(file_name, sep=";", index=True, header=True)
	print(f"File saved as: {file_name}\n")






	# output_file = open(output_path, "w")
	# output_file.write("volume\t")
	# output_file.write("\t".join(sample_list))
	# if label == "information":
	# 	for unit in sorted(input_data.keys()):
	# 		output_file.write("\n%s\t" % unit)
	# 		output_file.write("\t".join(map(str,input_data[unit])))
	# else:
	# 	for unit in sorted(input_data.keys(), key=lambda x:float(x)):
	# 		output_file.write("\n%s\t" % unit)
	# 		output_file.write("\t".join(map(str,input_data[unit])))
	# print(f"{output_file} has been created")

