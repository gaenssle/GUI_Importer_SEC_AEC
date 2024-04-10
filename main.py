#!/usr/bin/python
# Written by ALGaenssle in 2024

import os
import tkinter as tk
import tkinter.messagebox

# Own modules
from graphical_interface import formatting
from graphical_interface import draw_window
from graphical_interface import menu_about
from graphical_interface import menu_change_markers
# from graphical_interface import menu_other
# from graphical_interface.file_actions import FileActions


from import_size_exclusion import main_script
from import_size_exclusion.default_values import DefaultValues


class RawFiles():
	def __init__(self):
		self.input_path = "/home/lucie/Desktop/Git/SmallScripts/TestFiles/RawData"
		self.file_list = []
		self.selection_list = [
				"07_Inj_ Vial  57  BEX4-2b - 1.TXT",
				"08_Inj_ Vial  58  BEX4-3a - 1.TXT"
		]
		self.output_path = "/home/lucie/Desktop/Git/SmallScripts/TestFiles"
		self.file_name = "Module_test"



if __name__=="__main__":
	raw_files = RawFiles()
	# raw_files = FileActions()
	default_values = DefaultValues()
	# message = main_script.export_data(raw_files, default_values, True, True, True)
	# print(message)




# ## Create objects
# default_values = DefaultValues()
colors = formatting.Colors()
formatting = formatting.Formatting()
# raw_files = Files()










## ===============================================================================================
## SETUP WINDOW
## ===============================================================================================  
## Create window
window = tk.Tk()
window.title("Export SEC/GPC raw data files")
window.minsize(formatting.min_x_size, formatting.min_y_size)
window.resizable(False, False)


col_folder = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_export)
col_files = tk.Frame(window, relief=tk.RAISED,  bd=3, bg=colors.col_folder)
col_export = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_export)

# Draw frames
draw_window.draw_frame([col_folder, col_files, col_export])


## ===============================================================================================
## MENU BAR
## ===============================================================================================  
file_list_string=tk.StringVar(value=[""])

## Create main bar
menu_bar = tk.Menu(window)

## Create menu for files (reset, exit)
menu_file = tk.Menu(menu_bar, tearoff=0)
# menu_file.add_command(label="Reset", command=raw_files.get_input_folder(file_list_string, ask=False))
menu_file.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="Window", menu=menu_file)

## Create menu for help (about, set markers)
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="About", command=lambda:menu_about.about_program(window, formatting.font_header, formatting.font_text))
menu_help.add_command(label="Change markers", command=lambda: menu_change_markers.change_markers(window, default_values, formatting))
menu_bar.add_cascade(label="Configure", menu=menu_help)

# Draw menu bar
window.config(menu=menu_bar)

## ===============================================================================================
## COLUMN: FOLDER
## ===============================================================================================  
## Define default values
input_path = tk.StringVar(value="#N/A")
output_path = tk.StringVar(value="#N/A")

## Header
lab_col_folder = tk.Label(col_folder, text="FOLDERS", bg=colors.header, font=formatting.font_header)

# ## Create section for input folder
# button_input_folder = tk.Button(col_folder, text="Select input folder", bg=colors.button, command=raw_files.get_input_folder, font=formatting.font_text)
# labframe_input_folder = tk.LabelFrame(col_folder, bg=colors.col_export, labelwidget=button_input_folder, labelanchor='n')
# display_input_folder = tk.Label(labframe_input_folder, textvariable=input_path, bg=colors.col_export, wraplength=formatting.lab_max_length/2, height=formatting.display_height, font=formatting.info_font)

# ## Create section for output folder
# button_output_folder = tk.Button(col_folder, text="Select output folder", bg=colors.button, command=raw_files.get_output_folder, font=formatting.font_text)
# labframe_output_folder = tk.LabelFrame(col_folder, bg=colors.col_export, font=formatting.export_font, labelwidget=button_output_folder, labelanchor='n')
# display_output_folder = tk.Label(labframe_output_folder, textvariable=output_path, bg=colors.col_export, wraplength=formatting.lab_max_length/2, height=formatting.display_height, font=formatting.info_font)

# ## Draw widgets (as dict {widget: pady-multiplier})
# widgets = {lab_col_folder:1, labframe_input_folder:2, display_input_folder:1, labframe_output_folder:2, display_output_folder:1}
# draw_widget(widgets)



## ===============================================================================================
## COLUMN: FILES
## ===============================================================================================  
# Define default values
file_list_string=tk.StringVar(value=[""])

## Header
lab_col_files = tk.Label(col_files, text="FILES", bg=colors.header, font=formatting.font_header)

# ## Display/hide, correct, label and display input files
# button_files_select = tk.Button(col_files,text='Toggle select all', bg=colors.button, command=raw_files.select_deselect_file_list, font=formatting.font_text)
# labframe_input_folder = tk.LabelFrame(col_files, bg=colors.col_folder,  labelwidget=button_files_select, labelanchor='n') 

# ## Create listbox with scrollbar
# list_box_input_files = tk.Listbox(labframe_input_folder, selectmode = "multiple", listvariable=file_list_string, height=12)
# scrollbar_input_files = tk.Scrollbar(labframe_input_folder, orient='vertical', command=list_box_input_files.yview)
# list_box_input_files['yscrollcommand'] = scrollbar_input_files.set

# ## Create button to submit selection and check file names
# button_files_submit = tk.Button(col_files, text='Save selection', bg=colors.button, command=raw_files.submit_selection, font=formatting.font_text)
# spacer = tk.Label(col_files, text="", bg=colors.col_folder, font=formatting.font_header)

# ## Draw widgets (as dict {widget: pady-multiplier})
# widgets = {lab_col_files:1, labframe_input_folder:2, list_box_input_files:1, scrollbar_input_files:1, button_files_submit:0, spacer:1}
# draw_widget(widgets)


## ===============================================================================================
## COLUMN: EXPORT
## ===============================================================================================  
## Define default values
file_name = tk.StringVar(value=raw_files.file_name)
export_info = tk.BooleanVar()
export_raw = tk.BooleanVar()
export_elute = tk.BooleanVar()

## Header
lab_col_export = tk.Label(col_export, text="EXPORT", bg=colors.header, font=formatting.font_header)

# ## Give option to change the export file name
# button_file_name = tk.Button(col_export, text='Save output file name', bg=colors.button, command=raw_files.get_file_name, font=formatting.font_text)
# labframe_file_name = tk.LabelFrame(col_export, bg=colors.col_export, labelwidget=button_file_name, labelanchor='n')
# entry_file_name = tk.Entry(labframe_file_name, textvariable=file_name, font=formatting.font_text)

# ## List types of output that can be exported
# lab_file_column = tk.Label(col_export, text="SELECT OUTPUT", bg=colors.header, font=formatting.font_header)
# check_info = tk.Checkbutton(col_export, text='Information data', variable=export_info,bg=colors.col_export, font=formatting.font_text)
# check_raw = tk.Checkbutton(col_export, text='Raw data',variable=export_raw, bg=colors.col_export, font=formatting.font_text)
# check_elute = tk.Checkbutton(col_export, text='Elution data', variable=export_elute, bg=colors.col_export, font=formatting.font_text)
# check_info.select()
# check_raw.select()
# check_elute.select()

# ## Conduct export
# button_export = tk.Button(col_export, text="EXPORT DATA!", command=export_data, bg=colors.export, font=formatting.export_font)


# ## Draw widgets (as dict {widget: pady-multiplier})
# widgets = {lab_col_export:1, labframe_file_name:2, entry_file_name:1, lab_file_column:1, check_info:0, check_raw:0, check_elute:0, button_export:2}
# draw_widget(widgets)


widgets = {lab_col_folder:1, lab_col_files:1, lab_col_export:1}
draw_window.draw_widget(widgets, formatting)

## ===============================================================================================
## MAIN LOOP
## ===============================================================================================  
window.mainloop()