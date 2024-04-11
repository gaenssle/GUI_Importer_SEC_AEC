#!/usr/bin/python
# Written by ALGaenssle in 2024
# MAIN
# main script to extract and combine raw data from size exclusion (SEC)

import os
import tkinter as tk
import tkinter.messagebox

# Own modules
from graphical_interface import formatting
from graphical_interface import draw_window
from graphical_interface import menu_about
from graphical_interface import menu_change_markers
from graphical_interface.file_selection import FileSelection

from import_size_exclusion.main_script import export_data
from import_size_exclusion.default_values import DefaultValues


# Create class objects
if __name__=="__main__":
	files = FileSelection()
	default_values = DefaultValues()
	colors = formatting.Colors()
	formatting = formatting.Formatting()

## ===========================================================================
## FUNCTIONS
## ===========================================================================
# Get input name and set all variables according to it
def set_input_folder(ask=True):
	files.get_input_folder(ask=ask)
	set_truncated_path(files.input_path, input_path)
	set_truncated_path(files.output_path, output_path)
	set_truncated_path(files.file_name, file_name)
	set_file_list()

# Set costumized output folder
def set_output_folder():
	files.get_output_folder()
	set_truncated_path(files.output_path, output_path)

# Rename output file name (for exporting files)
def set_file_name():
	files.file_name = entry_file_name.get()
	print(f"File name was changed to: {files.file_name}")
	tkinter.messagebox.showinfo(
		title="Changed file name",
	 	message=f"Name of output files was changed to '{files.file_name}'")

# Truncate paths that are too long
def set_truncated_path(path, tk_variable):
	max_length = formatting.lab_max_length//4
	if len(path) > max_length:
		tk_variable.set("..." + path[-max_length:])
	else:
		tk_variable.set(path)

# Get all .txt files in folder and select all
def set_file_list():
	files.get_file_list()
	file_list_string.set(files.file_list)
	list_box_input_files.selection_set(0, "end")

# Toggle select/deselect all in file list
def toggle_select_all():
	if files.input_path == "":
		tkinter.messagebox.showwarning("Missing data","No input folder selected!")
		return
	files.selection_list = [list_box_input_files.get(index) 
						for index in list_box_input_files.curselection()]
	if len(files.file_list) == len(files.selection_list):
		list_box_input_files.select_clear(0, "end")
	else:
		list_box_input_files.selection_set(0, "end")
	files.selection_list = [list_box_input_files.get(index) 
						for index in list_box_input_files.curselection()]

# Save selection of input files
def submit_selection():
	if files.input_path == "":
		tkinter.messagebox.showwarning("Missing data","No input folder selected!")
		return
	files.selection_list = [list_box_input_files.get(index) for index in list_box_input_files.curselection()]
	if any(len(name.split("_",1)[0]) == 1 for name in files.file_list):
		rename = tkinter.messagebox.askquestion(title="Warning", message=f"Submitted file list contains names with no leading 0!\nDo you want to add them?", type="yesno")
		if rename:
			rename_files()
	tkinter.messagebox.showinfo("File list updated", 
		f"Input file list now consists of {len(files.selection_list)} files")

# Add 0 to Sample IDs under 10
def rename_files(file_list_string):
	count = 0
	for index, name in enumerate(files.file_list):
		if len(name.split("_",1)[0]) == 1:
			print(f"Name to be changed: {name}")
			os.rename(os.path.join(files.input_path, name), 
						os.path.join(files.input_path, "0" + name))
			files.file_list[index] = "0" + name
			count += 1
	file_list_string.set(files.file_list)		
	files.selection_list = [list_box_input_files.get(index) 
							for index in list_box_input_files.curselection()]
	files.selection_list.sort()		
	files.file_list.sort()
	file_list_string.set(files.file_list)
	tkinter.messagebox.showinfo("Renamed files", f"Renamed {count} files")

# Conduct importing, combining and exporting of files
def export_size_exclusion_data():
	files.file_name = entry_file_name.get()
	message = export_data(files, default_values, export_info.get(), 
							export_raw.get(), export_elute.get())
	if message["m_type"] == "info":
		tkinter.messagebox.showinfo(message["title"], message["message"])


## ===========================================================================
## SETUP WINDOW
## ===========================================================================
## Create window
window = tk.Tk()
window.title("Export SEC/GPC raw data files")
window.resizable(False, False)


col_folder = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_main)
col_files = tk.Frame(window, relief=tk.RAISED,  bd=3, bg=colors.col_sub)
col_export = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_main)

# Draw frames
draw_window.draw_frame([col_folder, col_files, col_export])


## ===========================================================================
## MENU BAR
## ===========================================================================
file_list_string=tk.StringVar(value=[""])

## Create main bar
menu_bar = tk.Menu(window)

## Create menu for files (reset, exit)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Reset", 
						command=lambda: set_input_folder(ask=False))
menu_file.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="Window", menu=menu_file)

## Create menu for help (about, set markers)
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="About", 
						command=lambda: menu_about.about_program(window, 
						formatting.font_heading, formatting.font_text))
menu_help.add_command(label="Change markers", 
						command=lambda: menu_change_markers.change_markers(
							window, default_values, formatting))
menu_bar.add_cascade(label="Configure", menu=menu_help)

# Draw menu bar
window.config(menu=menu_bar)

## ===========================================================================
## COLUMN: FOLDER
## ===========================================================================
## Define default values
input_path = tk.StringVar(value="#N/A")
output_path = tk.StringVar(value="#N/A")

## Header
lab_col_folder = tk.Label(col_folder, text="FOLDERS", bg=colors.heading, 
				font=formatting.font_heading)

## Create section for input folder
button_input_folder = tk.Button(col_folder, 
								text="Select input folder", 
								bg=colors.button, 
								command=set_input_folder, 
								font=formatting.font_text)
labframe_input_folder = tk.LabelFrame(col_folder, 
									bg=colors.col_main, 
									labelwidget=button_input_folder, 
									labelanchor="n")
display_input_folder = tk.Label(labframe_input_folder, 
								textvariable=input_path, 
								bg=colors.col_main, 
								wraplength=formatting.lab_max_length/2, 
								height=formatting.display_height, 
								font=formatting.font_note)

## Create section for output folder
button_output_folder = tk.Button(col_folder, 
								text="Select output folder", 
								bg=colors.button, 
								command=set_output_folder, 
								font=formatting.font_text)
labframe_output_folder = tk.LabelFrame(col_folder, 
									bg=colors.col_main, 
									labelwidget=button_output_folder, 
									labelanchor="n")
display_output_folder = tk.Label(labframe_output_folder, 
								textvariable=output_path, 
								bg=colors.col_main, 
								wraplength=formatting.lab_max_length/2, 
								height=formatting.display_height, 
								font=formatting.font_note)

## Draw widgets (as dict {widget: pady-multiplier})
widgets = {
			lab_col_folder:1, 
			labframe_input_folder:2, 
			display_input_folder:1, 
			labframe_output_folder:2, 
			display_output_folder:1
			}
draw_window.draw_widget(widgets, formatting)


## ===========================================================================
## COLUMN: FILES
## ===========================================================================
## Define default values
file_list_string=tk.StringVar(value=[""])

## Header
lab_col_files = tk.Label(col_files, 
						text="FILES", 
						bg=colors.heading, 
						font=formatting.font_heading)

## Display/hide, correct, label and display input files
button_files_select = tk.Button(col_files,
								text="Toggle select all", 
								bg=colors.button, 
								command=toggle_select_all, 
								font=formatting.font_text)
labframe_input_folder = tk.LabelFrame(col_files, 
									bg=colors.col_sub,  
									labelwidget=button_files_select, 
									labelanchor="n") 

## Create listbox with scrollbar
list_box_input_files = tk.Listbox(labframe_input_folder, 
								selectmode = "multiple", 
								listvariable=file_list_string, 
								height=12)
scrollbar_input_files = tk.Scrollbar(labframe_input_folder, 
									orient="vertical", 
									command=list_box_input_files.yview)
list_box_input_files["yscrollcommand"] = scrollbar_input_files.set

## Create button to submit selection and check file names
button_files_submit = tk.Button(col_files, 
								text="Save selection", 
								bg=colors.button, 
								command=submit_selection, 
								font=formatting.font_text)
spacer = tk.Label(col_files, 
				text="", 
				bg=colors.col_sub, 
				font=formatting.font_heading)

## Draw widgets (as dict {widget: pady-multiplier})
widgets = {
			lab_col_files:1, 
			labframe_input_folder:2, 
			list_box_input_files:1, 
			scrollbar_input_files:1, 
			button_files_submit:0, 
			spacer:1
			}
draw_window.draw_widget(widgets, formatting)


## ===========================================================================
## COLUMN: EXPORT
## ===========================================================================
## Define default values
file_name = tk.StringVar(value=files.file_name)
export_info = tk.BooleanVar()
export_raw = tk.BooleanVar()
export_elute = tk.BooleanVar()

## Header
lab_col_export = tk.Label(col_export, 
						text="EXPORT", 
						bg=colors.heading, 
						font=formatting.font_heading)

## Give option to change the export file name
button_file_name = tk.Button(col_export, 
							text="Save output file name", 
							bg=colors.button, 
							command=set_file_name, 
							font=formatting.font_text)
labframe_file_name = tk.LabelFrame(col_export, 
									bg=colors.col_main, 
									labelwidget=button_file_name, 
									labelanchor="n")
entry_file_name = tk.Entry(labframe_file_name, 
							textvariable=file_name, 
							font=formatting.font_text)

## List types of output that can be exported
lab_file_column = tk.Label(col_export, 
							text="SELECT OUTPUT", 
							bg=colors.heading, 
							font=formatting.font_heading)
check_info = tk.Checkbutton(col_export, 
							text="Information data", 
							variable=export_info, 
							bg=colors.col_main, 
							font=formatting.font_text)
check_raw = tk.Checkbutton(col_export, 
							text="Raw data",
							variable=export_raw, 
							bg=colors.col_main, 
							font=formatting.font_text)
check_elute = tk.Checkbutton(col_export, 
							text="Elution data", 
							variable=export_elute, 
							bg=colors.col_main, 
							font=formatting.font_text)
check_info.select()
check_raw.select()
check_elute.select()

## Conduct export
button_export = tk.Button(col_export, 
						text="EXPORT DATA!", 
						command=export_size_exclusion_data, 
						bg=colors.accent, 
						font=formatting.font_subheading)


## Draw widgets (as dict {widget: pady-multiplier})
widgets = {
			lab_col_export:1, 
			labframe_file_name:2, 
			entry_file_name:1, 
			lab_file_column:1, 
			check_info:0, 
			check_raw:0, 
			check_elute:0, 
			button_export:2
			}
draw_window.draw_widget(widgets, formatting)


## ===========================================================================
## MAIN LOOP
## ===========================================================================
window.mainloop()