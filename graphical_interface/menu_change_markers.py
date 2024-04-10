#!/usr/bin/python
# Written by ALGaenssle in 2024
# MODULE - MENU BAR
# Change default values (temporarily)

import tkinter as tk
import tkinter.messagebox

## ===========================================================================
## Offer a way to temporarily change the default values with an entry mask
def change_markers(window, default_values, formatting):
	## Check if the entered data in the column entry widgets are integers ----
	def validate_integer():
		raw_column = column_raw_data.get()
		elu_column = column_elu_data.get()
		try:
			default_values.raw_column = int(raw_column) - 1
			default_values.elu_column = int(elu_column) - 1
		except ValueError:
			tkinter.messagebox.showwarning('Incorrect data', "Please enter full numbers for the columns (raw and elution data)")
			return False
		return True

	## Check if the markers have been edited and update them -----------------
	def update_markers(default, variable):
		if "\n" not in variable.get():
			default = variable.get() + "\n"

	## Submit the changes to alter the default values ------------------------
	def submit_marker_change():
		if validate_integer():
			update_markers(default_values.info_stop, marker_info_stop)
			update_markers(default_values.raw_start, marker_raw_start)
			update_markers(default_values.raw_stop, marker_raw_stop)
			update_markers(default_values.elu_start, marker_elu_start)
			update_markers(default_values.elu_stop, marker_elu_stop)
			tkinter.messagebox.showinfo('Changed markers', "Markers were changed sucessfully and remain set until program is closed")

	marker_info = ("The program imports the data from the files by using markers, lines in the text directly before and after the lines which should be imported."
					"\nThese lines might differ for other systems and can be changed temporarily here."
					"\n\nIf you want to change them permanently, copy-paste the program file, open it in a text editor and search for the section starting with 'class Default_Values'")
	

	# Create window for changing the markers
	window_change_markers = tk.Toplevel(window)
	window_change_markers.title("Change default values")
	# window_change_markers.geometry("600x500")
	tk.Label(window_change_markers, text ="MARKERS", font=formatting.font_header).grid(row=0, columnspan=2)
	show_info = tk.Text(window_change_markers, wrap=tk.WORD, height=8, width=60, font=formatting.font_text)
	show_info.grid(row=1, columnspan=2, padx=formatting.padx, pady=formatting.pady)
	show_info.insert("end", marker_info)
	show_info.config(state='disabled')

	# Create variables for the entry widgests
	marker_info_stop = tk.StringVar(value=default_values.info_stop)
	column_raw_data = tk.StringVar(value=default_values.raw_column+1)
	marker_raw_start = tk.StringVar(value=default_values.raw_start)
	marker_raw_stop = tk.StringVar(value=default_values.raw_stop)
	column_elu_data = tk.StringVar(value=default_values.elu_column+1)
	marker_elu_start = tk.StringVar(value=default_values.elu_start)
	marker_elu_stop = tk.StringVar(value=default_values.elu_stop)

	# List all default values and show the current values in the entry widgets
	tk.Label(window_change_markers, text="Information: stop marker", font=formatting.font_text).grid(row=2, column=0, sticky = 'w', padx=formatting.padx)
	tk.Entry(window_change_markers, textvariable=marker_info_stop, font=formatting.font_text).grid(row=2, column=1, padx=formatting.padx)
	tk.Label(window_change_markers, text="Raw data: column with RI values", font=formatting.font_text).grid(row=3, column=0, sticky = 'w', padx=formatting.padx)
	tk.Entry(window_change_markers, textvariable=column_raw_data, font=formatting.font_text).grid(row=3, column=1, padx=formatting.padx)	
	tk.Label(window_change_markers, text="Raw data: start marker", font=formatting.font_text).grid(row=4, column=0, sticky = 'w', padx=formatting.padx)
	tk.Entry(window_change_markers, textvariable=marker_raw_start, font=formatting.font_text).grid(row=4, column=1, padx=formatting.padx)
	tk.Label(window_change_markers, text="Raw data: stop marker", font=formatting.font_text).grid(row=5, column=0, sticky = 'w', padx=formatting.padx)
	tk.Entry(window_change_markers, textvariable=marker_raw_stop, font=formatting.font_text).grid(row=5, column=1, padx=formatting.padx)
	tk.Label(window_change_markers, text="Elution data: column with RI values", font=formatting.font_text).grid(row=6, column=0, sticky = 'w', padx=formatting.padx)
	tk.Entry(window_change_markers, textvariable=column_elu_data, font=formatting.font_text).grid(row=6, column=1, padx=formatting.padx)
	tk.Label(window_change_markers, text="Elution data: start marker", font=formatting.font_text).grid(row=7, column=0, sticky = 'w', padx=formatting.padx)
	tk.Entry(window_change_markers, textvariable=marker_elu_start, font=formatting.font_text).grid(row=7, column=1, padx=formatting.padx)
	tk.Label(window_change_markers, text="Elution data: stop marker", font=formatting.font_text).grid(row=8, column=0, sticky = 'w', padx=formatting.padx)
	tk.Entry(window_change_markers, textvariable=marker_elu_stop, font=formatting.font_text).grid(row=8, column=1, padx=formatting.padx)
	
	# Create button to submit the added changes
	tk.Button(window_change_markers, text="Submit changes", command=submit_marker_change, font=formatting.font_text).grid(row=10, columnspan=2, padx=formatting.padx, pady=formatting.pady)