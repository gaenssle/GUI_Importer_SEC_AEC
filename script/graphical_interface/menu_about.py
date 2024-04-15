#!/usr/bin/python
# Written by ALGaenssle in 2024
# MODULE - MENU BAR
# Show a window with info about the program


import tkinter as tk
import tkinter.scrolledtext 

## ===========================================================================
## Info text about the program
program_info = 	"""\
(Written in 2024 by a.l.o gaenssle, check github.com/gaenssle/RawData_Importer_AEC_SEC for updates)

This program imports raw files from size exclusion chromatography (SEC/GPC)
- It takes a folder as input and lets you choose the files within this folder to import
- Both the destination folder and the name of the output can be changed as needed
- The program extract and combines all files
- The are three possible output files (information, raw data and elution data)

INFORMATION DATA
exports the header of each file, such as sample name, internal standard and estimated molecular weight

RAW DATA
exports the raw RI values and the time/volume

ELUTION DATA
exports the corrected RI values and time/volume (both x- and y- corrected)

OVERALL REQUIREMENTS:
- All files have to be located in one folder
- There can be additional files in the folder which you need to deselect before saving the selection
- The default output folder is set to the parent folder of the raw files but can be anywhere else
- There is a default name given to the exported files but it can be changed
- The data is extracted based on markers 
(lines in the raw files, check and change accordingly if needed in 'help' ->'change markers')
"""

## ===========================================================================
## Show info about the program
def about_program(window, font_heading, font_text):
	window_about = tk.Toplevel(window)
	window_about.title("About this program")
	window_about.geometry("600x300")

	tk.Label(
			window_about, 
			text ="SEC IMPORTER", 
			font=font_heading
			).pack()

	show_info = tkinter.scrolledtext.ScrolledText(
				window_about, 
				wrap=tk.WORD, 
				font=font_text)
	show_info.pack()
	show_info.insert("end", program_info)
	show_info.config(state="disabled")