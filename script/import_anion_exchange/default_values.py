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
		self.sample_line = "Injection\t"

		# Marker lines used to split the raw data
		self.info_stop = "Signal Parameter Information:\n"
		self.raw_start = "Chromatogram Data:\n"

		# Lines of info to be extracted
		self.info_keys = (
			"Instrument Method",
			"Injection Volume", 
			"Dilution Factor", 
			"Signal Min.", 
			"Signal Max.", 
			"Mp")

		# Define which column contains the RI values
		self.raw_column = 2