#!/usr/bin/python
# Written by ALGaenssle in 2024

## ====================================================================
## SCRIPT - MAIN
## Main script for importing SEC data
## ====================================================================

import os

# Import own modules
from . import functions


## ====================================================================
## Main export data funtion
def export_data(raw_files, default_values, export_info, export_raw, export_elute):
	if raw_files.input_path == "":
		return ['Warning', 'Missing data', 'No input folder selected!']

	# Combine the data from all files
	sample_list = []
	information = {}
	raw_data = {}
	elution_data = {}
	for index, file in enumerate(raw_files.selection_list):
		# try:
		part_info, part_raw, part_elution = functions.split_file(
				os.path.join(raw_files.input_path, file), default_values)
		# except:
		# 	return ['Warning', 'Incorrect data','Could not import data!\nPlease check file path and your input files']

		# Extract and combine data

		name, info = functions.extract_info(part_info, 
			default_values.info_keys)
		raw = functions.extract_data(part_raw, default_values.raw_column)
		elution = functions.extract_data(part_elution, default_values.elu_column)
		information.update({name:info})
		raw_data.update({name:raw})
		elution_data.update({name:elution})
		
	# Export data
	message = "Created files:\n\n"
	file_name_part = os.path.join(raw_files.output_path, raw_files.file_name)
	if export_info:
		functions.export_file(information, 
							file_name_part + "_information.txt",
							label="Marker")
		message += "- Information file\n"
	if export_raw:
		functions.export_file(raw_data, 
							file_name_part + "_raw_data.txt")
		message += "- Merged raw data\n"
	if export_elute: 
		functions.export_file(elution_data, 
							file_name_part + "_elution_data.txt")
		message += "- Merged elution data\n"

	return ['Info', 'Done exporting', message]
