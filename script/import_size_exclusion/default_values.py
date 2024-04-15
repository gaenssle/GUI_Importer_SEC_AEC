#!/usr/bin/python
# Written by ALGaenssle in 2024

## ====================================================================
## CLASS
## Default values defining how the data is imported
## ====================================================================

## Class for default values
class DefaultValues():
	def __init__(self):
		# Encoding of the raw data files
		self.file_encoding = "cp1252"

		# Extract sample name from the line starting with this string
		self.sample_line = "Sample :"

		# Marker lines used to split the raw data
		self.info_stop = "Calibration Coefficients:\n"
		self.raw_start = "RAWstart :\n"
		self.raw_stop = "RAWstop :\n"
		self.elu_start = "ELUstart :\n"
		self.elu_stop = "ELUstop :\n"

		# Lines of info to be extracted
		self.info_keys = (
			"Internal Standard Calibration",
			"Internal Standard Acquisition", 
			"Mn", 
			"Mw", 
			"Mz", 
			"Mp")

		# Define which column contains the RI values
		self.elu_column = 2
		self.raw_column = 1