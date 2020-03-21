####################################################### VARIABLES #########################################################

T_1 = "PLAGIARISM DETECTION SOFTWARE VERSION 1.0"
T_2 = "PLAGIARISM\n\tDETECTION\n\t\tSOFTWARE\n\t\t\t-Version 1.0"
T_3 = "A project by:\n\tManas Joshi\n\tHrushikesh Joshi\n\tSameer Rathod"
T_4 = "\tWelcome, We have created a software that detects TEXT and C++ CODE PLAGIARISM, all you need to do is to upload documented to be tested and documents to be referenced. Our software will Detect similarity and will provide analytical data for the user to make the decision !"
T_5 = "BROWSE YOUR DOCUMENTS :"
T_6 = "Document to be tested :"
T_7 = "Document to be referred :"
T_8 = "MATCHES FOUND IN :"
T_9 = "Do you really wanna QUIT?"
T_10 = "BROWSE YOU FILE"
T_11 = "SIMILARITY WITH SELECTED DOCUMENT IS:"
T_12 = "SIMILARITY : "
B_1 = "NEXT"
B_2 = "BACK"
B_3 = "BROWSE"
B_4 = "REMOVE"
B_5 = "QUIT"
B_6 = "YES"
B_7 = "NO"
B_8 = "DETAILS"
C_2 = "#E95420"#UBUNTU ORANGE
C_3 = "#77216F"#LIGHT AUBERGINE
C_4 = "#772953"#CANONICAL AUBERGINE
C_5 = "#5E2750"#MID AUBERGINE
C_6 = "#2C001E"#DARK AUBERGINE
C_0 = "#FFFFFF"#WHITE
C_1 = "#000000"#BLACK
C_7 = "#2A1363"#MY
C_8 = "#001B33"#DARK BLUE
B_C = "#2A1363"
F_C = "#FFFFFF"
F_S = 9
FONT_1 = "Times "
FONT_2 = "Arial"
output_path="/home/sameerrathod/Desktop/SDLATEST/BUFFER/"
STRING_MATCHED_LINES=[]
TOKEN_MATCHED_LINES=[]
PARSE_MATCHED_LINES=[]
PDG_MATCHED_LINES=[]
METRICS_MATCHED_LINES=[]

###################################################### PROGRAM #########################################################
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import shutil
import CODE_AUTO_FORMATTER	as CAF
import CODE_PLAGIARISM_DETECTION_ALGORITHMS as CPDA
import fileMatcher as fm

WINDOW = tk.Tk()
WINDOW.title(T_1)
WINDOW.minsize(960,540)#REQIURED SCREEN RESOLUTION IS 1024p*720p+
W_H = float(WINDOW.winfo_screenheight()/540)
W_W = float(WINDOW.winfo_screenwidth()/960)
ratio=float(float(W_H+W_W)/2)
FRAME_1 = tk.Frame(WINDOW,bd=10,height=540,width=960,relief=tk.GROOVE,bg=B_C)
FRAME_2 = tk.Frame(WINDOW,bd=10,height=540,width=960,relief=tk.GROOVE,bg=B_C)
FRAME_3 = tk.Frame(WINDOW,bd=10,height=540,width=960,relief=tk.GROOVE,bg=B_C)
FRAME_4 = tk.Frame(WINDOW,bd=10,height=540,width=960,relief=tk.GROOVE,bg=B_C)

for FRAME in(FRAME_1,FRAME_2,FRAME_3,FRAME_4):
	FRAME.grid(column=0,row=0,sticky=(tk.E,tk.W,tk.N,tk.S))

#######################################################  FUNCTIONS  ###################################################
VARIABLE_TEXT_1 = tk.StringVar()
VARIABLE_TEXT_2 = tk.StringVar()
VARIABLE_TEXT_3 = tk.StringVar()
VARIABLE_TEXT_4 = tk.StringVar()
VARIABLE_TEXT_5 = tk.StringVar()
VARIABLE_TEXT_6 = tk.StringVar()
total=0
percentage=0.00
S_highlights=set()
T_highlights=set()
M_highlights=set()
def quit_function():
	QUIT_WINDOW = tk.Toplevel(WINDOW)
	QUIT_WINDOW.title("QUIT?")
	QUIT_WINDOW.minsize(560,150)
	QUIT_FRAME = tk.Frame(QUIT_WINDOW,relief=tk.GROOVE,bg=C_0,bd=10,padx=10,pady=10)
	LABEL_9 = tk.Label(QUIT_FRAME,text=T_9,bg=C_0,fg=C_1,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+5))
	BUTTON_9 = tk.Button(QUIT_FRAME,text=B_6,command=quit,width=6,font= FONT_1+str(int(F_S*ratio)))
	BUTTON_10 = tk.Button(QUIT_FRAME,text=B_7,command=QUIT_WINDOW.destroy,width=6,font= FONT_1+str(int(F_S*ratio)))
	QUIT_FRAME.grid(row=0,column=0,sticky=(tk.S,tk.W,tk.E,tk.N))
	QUIT_FRAME.rowconfigure(0,weight=1)
	QUIT_FRAME.columnconfigure(0,weight=1)
	QUIT_WINDOW.rowconfigure(0,weight=1)
	QUIT_WINDOW.columnconfigure(0,weight=1)
	LABEL_9.grid(row=0,column=0,columnspan=2,padx=20,pady=20,sticky=(tk.S,tk.W,tk.E,tk.N))
	BUTTON_9.grid(row=1,column=1,sticky=(tk.S,tk.E))
	BUTTON_10.grid(row=1,column=0,sticky=(tk.S,tk.W))
	QUIT_WINDOW.mainloop()

def browse_test_file():
	b_test_file_address=filedialog.askopenfilename(title=T_10)
	ENTRY_7.delete(0,tk.END)
	ENTRY_7.insert(0,b_test_file_address)

def browse_reference_file():
	b_reference_file_address=filedialog.askopenfilename(title=T_10)
	LIST_BOX_1.insert(tk.END,b_reference_file_address)

def remove_reference_file():
	LIST_BOX_1.delete(tk.ANCHOR)

def collect_all_documents():
	LIST_BOX_2.delete(0,tk.END)
	c_test_file_address=ENTRY_7.get()
	MATCH_FOUND=0;

	if len(c_test_file_address) == 0:
		VARIABLE_TEXT_1.set("*PLEASE ONE TEST DOCUMENT REQUIRED")

	c_reference_file_address=[]
	for i in range(LIST_BOX_1.size()):
		c_reference_file_address.append(LIST_BOX_1.get(i))

	if len(c_reference_file_address) == 0:
		VARIABLE_TEXT_1.set("*PLEASE ONE OR MORE THAN ONE REFERENCE DOCUMENT REQUIRED")

	if len(c_reference_file_address) != 0 and len(c_test_file_address) != 0:
		VARIABLE_TEXT_1.set(" ")
		test_file_name=(os.path.basename(c_test_file_address))
		shutil.copy(c_test_file_address,output_path+test_file_name)
		x=test_file_name.endswith(".cpp")
		y=test_file_name.endswith(".jpg"or".png"or".bmp"or"jpeg")
		z=test_file_name.endswith(".pdf")
		if x:
			CAF.autoFormatCode(output_path+test_file_name,output_path+test_file_name)
		elif y:
			test_file_newaddress=fm.image_to_text(c_test_file_address,output_path)
			test_file_name=(os.path.basename(test_file_newaddress))
		elif z:
			test_file_newaddress=fm.pdf_to_text(c_test_file_address,output_path)
			test_file_name=(os.path.basename(test_file_newaddress))
			print(test_file_name)
		tempstr=""
		for i in range(len(c_reference_file_address)):
			reference_file_name=(os.path.basename(c_reference_file_address[i]))
			tempstr+=c_reference_file_address[i]
			shutil.copy(c_reference_file_address[i],output_path+reference_file_name)
			x=reference_file_name.endswith(".cpp")
			y=reference_file_name.endswith(".jpg"or".png"or".bmp"or"jpeg")
			z=reference_file_name.endswith(".pdf")
			if x:
				CAF.autoFormatCode(output_path+reference_file_name,output_path+reference_file_name)
			elif y:
				reference_file_newaddress=fm.image_to_text(tempstr,output_path)
				reference_file_name=(os.path.basename(reference_file_newaddress))
			elif z:
				reference_file_newaddress=fm.pdf_to_text(tempstr,output_path)
				reference_file_name=(os.path.basename(reference_file_newaddress))
				print(reference_file_name)
			if CPDA.string_matching(output_path+test_file_name,output_path+reference_file_name):
				STRING_MATCHED_LINES.append(CPDA.string_matching(output_path+test_file_name,output_path+reference_file_name))
				MATCH_FOUND=1;
			if CPDA.tokenization(output_path+test_file_name,output_path+reference_file_name):
				TOKEN_MATCHED_LINES.append(CPDA.tokenization(output_path+test_file_name,output_path+reference_file_name))
				MATCH_FOUND=1;
			if CPDA.metrics(output_path+test_file_name,output_path+reference_file_name):
				METRICS_MATCHED_LINES.append(CPDA.metrics(output_path+test_file_name,output_path+reference_file_name))
				MATCH_FOUND=1;
			sequenceMatchPercent=CPDA.sequenceMatch(output_path+test_file_name,output_path+reference_file_name)
			VARIABLE_TEXT_6.set(sequenceMatchPercent)
			if MATCH_FOUND == 1:
				LIST_BOX_2.insert(tk.END,reference_file_name)
	if len(c_reference_file_address) != 0 and len(c_test_file_address) != 0:
		FRAME_3.tkraise()

def show_details():
	S_highlights.clear()
	T_highlights.clear()
	M_highlights.clear()
	selection = LIST_BOX_2.curselection()
	if selection:
		VARIABLE_TEXT_2.set(" ")
		LIST_BOX_3.delete(0,tk.END)

		#chithhiya kya thi
		# bagavat , mohabbat , pyaar , sneha , nimantran aur mafi tha
		# maa ki chithhi aayi hai rulane ko ek vaakya hi kafi tha

		LIST_BOX_4.delete(0,tk.END)
		LIST_BOX_5.delete(0,tk.END)
		LIST_BOX_6.delete(0,tk.END)
		LIST_BOX_11.delete(0,tk.END)
		LIST_BOX_12.delete(0,tk.END)
		test_file_name=os.path.basename(ENTRY_7.get())

		with open(output_path+test_file_name+'.txt','r')as file:
			temp = file.read()
			test_display = temp.split('\n')
		for i in range(len(test_display)):
			LIST_BOX_3.insert(tk.END,test_display[i])
			LIST_BOX_5.insert(tk.END,test_display[i])
			LIST_BOX_11.insert(tk.END,test_display[i])

		reference_name = LIST_BOX_2.get(tk.ACTIVE)
		with open(output_path+reference_name,'r')as file:
			temp = file.read()
			reference_display = temp.split('\n')
		for i in range(len(reference_display)):
			LIST_BOX_4.insert(tk.END,reference_display[i])
			LIST_BOX_6.insert(tk.END,reference_display[i])
			LIST_BOX_12.insert(tk.END,reference_display[i])

		for i in range(len(STRING_MATCHED_LINES[selection[0]])):
			LIST_BOX_3.itemconfig(STRING_MATCHED_LINES[selection[0]][i][0],bg=C_2)
			LIST_BOX_4.itemconfig(STRING_MATCHED_LINES[selection[0]][i][1],bg=C_2)
			S_highlights.add(STRING_MATCHED_LINES[selection[0]][i][0])
		percentage=float((len(S_highlights)/len(test_display))*100)
		VARIABLE_TEXT_3.set(percentage)
		for i in range(len(TOKEN_MATCHED_LINES[selection[0]])):
			LIST_BOX_5.itemconfig(TOKEN_MATCHED_LINES[selection[0]][i][0],bg=C_2)
			LIST_BOX_6.itemconfig(TOKEN_MATCHED_LINES[selection[0]][i][1],bg=C_2)
			T_highlights.add(TOKEN_MATCHED_LINES[selection[0]][i][0])
		percentage=float((len(T_highlights)/len(test_display))*100)
		VARIABLE_TEXT_4.set(percentage)

		for i in range(len(METRICS_MATCHED_LINES[selection[0]][0])):
			LIST_BOX_11.itemconfig(METRICS_MATCHED_LINES[selection[0]][0][i],bg=C_2)
			M_highlights.add(METRICS_MATCHED_LINES[selection[0]][0][i])
		for i in range(len(METRICS_MATCHED_LINES[selection[0]][1])):
			LIST_BOX_12.itemconfig(METRICS_MATCHED_LINES[selection[0]][1][i],bg=C_2)
		percentage=float((len(M_highlights)/len(test_display))*100)
		VARIABLE_TEXT_5.set(percentage)
		FRAME_4.tkraise()
	else:
		VARIABLE_TEXT_2.set("*PLEASE SELECT A FILE TO SEE THE DETAILS")

#######################################################   FRAME 1  #####################################################

LABEL_1 = tk.Label(FRAME_1,text=T_2,bg=B_C,fg=F_C,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+10))
LABEL_2 = tk.Label(FRAME_1,text=T_3,bg=B_C,fg=F_C,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+3))
LABEL_3 = tk.Label(FRAME_1,text=T_4,bg=B_C,fg=F_C,justify=tk.LEFT,wraplength=770,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+1))
BUTTON_1 = tk.Button(FRAME_1,text=B_1,command=lambda:FRAME_2.tkraise(),width=6,font= FONT_1+str(int(F_S*ratio)))

LABEL_1.grid(column=0,row=0,sticky=(tk.E,tk.W,tk.N,tk.S))
LABEL_2.grid(column=0,row=2,sticky=(tk.E,tk.W,tk.N,tk.S))
LABEL_3.grid(column=0,row=1,columnspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
BUTTON_1.grid(column=1,row=2)

for child in FRAME_1.winfo_children():child.grid_configure(padx=25,pady=25)

for i in range(3):
	FRAME_1.rowconfigure(i,weight=1)
for i in range(2):
	FRAME_1.columnconfigure(i,weight=1)

#######################################################   FRAME 2  #####################################################
LABEL_4 = tk.Label(FRAME_2,text=T_5,bg=B_C,fg=F_C,justify=tk.LEFT,font=FONT_1+str(int(F_S*ratio)+2))
LABEL_5 = tk.Label(FRAME_2,text=T_6,bg=B_C,fg=F_C,justify=tk.LEFT,font=FONT_1+str(int(F_S*ratio)))
LABEL_6 = tk.Label(FRAME_2,text=T_7,bg=B_C,fg=F_C,justify=tk.LEFT,font=FONT_1+str(int(F_S*ratio)))
ENTRY_7 = tk.Entry(FRAME_2,bg=B_C,fg=F_C,justify=tk.LEFT,font=FONT_2+str(int(F_S*ratio)),width = 60)
LABEL_7 = tk.Label(FRAME_2,textvariable=VARIABLE_TEXT_1,bg=B_C,fg=C_2,justify=tk.LEFT,font=FONT_2+str(int(F_S*ratio)))
BUTTON_2 = tk.Button(FRAME_2,text=B_3,command=browse_test_file,width=6,font=FONT_1+str(int(F_S*ratio)))
BUTTON_3 = tk.Button(FRAME_2,text=B_3,command=browse_reference_file,width=6,font=FONT_1+str(int(F_S*ratio)))
BUTTON_4 = tk.Button(FRAME_2,text=B_4,command=remove_reference_file,width=6,font=FONT_1+str(int(F_S*ratio)))
BUTTON_5 = tk.Button(FRAME_2,text=B_1,command=collect_all_documents,width=6,font= FONT_1+str(int(F_S*ratio)))
BUTTON_6 = tk.Button(FRAME_2,text=B_2,command=lambda:FRAME_1.tkraise(),width=6,font= FONT_1+str(int(F_S*ratio)))
LIST_BOX_1 = tk.Listbox(FRAME_2,width=95)
SCROLL_BAR_1 = tk.Scrollbar(FRAME_2,orient=tk.VERTICAL)
SCROLL_BAR_2 = tk.Scrollbar(FRAME_2,orient=tk.HORIZONTAL)

LABEL_4.grid(column=0,row=0,columnspan=3,sticky=(tk.W,tk.N))
LABEL_5.grid(column=0,row=1,columnspan=3,sticky=(tk.W))
LABEL_6.grid(column=0,row=4,columnspan=3,sticky=(tk.W))
ENTRY_7.grid(column=0,row=2,sticky=(tk.W,tk.E,tk.N,tk.S))
LABEL_7.grid(column=0,row=3,sticky=(tk.W,tk.E,tk.N,tk.S))
BUTTON_2.grid(column=3,row=2)
BUTTON_3.grid(column=3,row=5)
BUTTON_4.grid(column=3,row=6)
BUTTON_5.grid(column=3,row=8,sticky=(tk.E,tk.S))
BUTTON_6.grid(column=0,row=8,sticky=(tk.W,tk.S))
LIST_BOX_1.grid(column=0,row=5,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
SCROLL_BAR_1.grid(column=1,row=5,rowspan=2,sticky=(tk.N,tk.S))
SCROLL_BAR_2.grid(column=0,row=7,sticky=(tk.E,tk.W))

SCROLL_BAR_1.config(command=LIST_BOX_1.yview)
SCROLL_BAR_2.config(command=LIST_BOX_1.xview)
LIST_BOX_1.config(yscrollcommand=SCROLL_BAR_1.set,xscrollcommand=SCROLL_BAR_2.set)

for child in FRAME_2.winfo_children():child.grid_configure(padx=10,pady=10)

for i in range(2):
	FRAME_2.columnconfigure(i,weight=1)
for i in range(2):
	FRAME_2.rowconfigure(i,weight=1)

#######################################################   FRAME 3  #####################################################

LABEL_8 = tk.Label(FRAME_3,text=T_8,bg=B_C,fg=F_C,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+2))
LABEL_9 = tk.Label(FRAME_3,textvariable=VARIABLE_TEXT_2,bg=B_C,fg=C_2,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)))
BUTTON_7 = tk.Button(FRAME_3,text=B_5,command=lambda:quit_function(),width=6,font= FONT_1+str(int(F_S*ratio)))
BUTTON_8 = tk.Button(FRAME_3,text=B_2,command=lambda:FRAME_2.tkraise(),width=6,font= FONT_1+str(int(F_S*ratio)))
BUTTON_9 = tk.Button(FRAME_3,text=B_8,command=show_details,width=6,font= FONT_1+str(int(F_S*ratio)))
LIST_BOX_2 = tk.Listbox(FRAME_3)
SCROLL_BAR_24 = tk.Scrollbar(FRAME_3,orient=tk.VERTICAL)

LABEL_8.grid(column=0,row=0,sticky=(tk.W,tk.N,tk.S))
LABEL_9.grid(column=0,row=2,sticky=(tk.W,tk.N,tk.S))
BUTTON_7.grid(column=1,row=3,sticky=(tk.E,tk.S))
BUTTON_8.grid(column=0,row=3,sticky=(tk.W,tk.S))
BUTTON_9.grid(column=1,row=2,sticky=(tk.E,tk.S))
LIST_BOX_2.grid(column=0,row=1,columnspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
SCROLL_BAR_24.grid(column=2,row=1,sticky=(tk.N,tk.S))

SCROLL_BAR_24.config(command=LIST_BOX_2.yview)
LIST_BOX_2.config(yscrollcommand=SCROLL_BAR_24.set)

for child in FRAME_3.winfo_children():child.grid_configure(padx=20,pady=10)

for i in range(2):
	FRAME_3.rowconfigure(i,weight=1)
	FRAME_3.columnconfigure(i,weight=1)

#######################################################   FRAME 4  #####################################################

NOTE_BOOK = ttk.Notebook(FRAME_4)
NOTE_BOOK.grid(column=0,row=0,sticky=(tk.E,tk.W,tk.N,tk.S))

FRAME_5 = tk.Frame(NOTE_BOOK,bd=10,relief=tk.GROOVE,bg=B_C)
FRAME_6 = tk.Frame(NOTE_BOOK,bd=10,relief=tk.GROOVE,bg=B_C)
FRAME_7 = tk.Frame(NOTE_BOOK,bd=10,relief=tk.GROOVE,bg=B_C)
FRAME_8 = tk.Frame(NOTE_BOOK,bd=10,relief=tk.GROOVE,bg=B_C)
FRAME_9 = tk.Frame(NOTE_BOOK,bd=10,relief=tk.GROOVE,bg=B_C)

NOTE_BOOK.add(FRAME_5,text="STRING MATCHING")
NOTE_BOOK.add(FRAME_6,text="TOKENIZATION")
NOTE_BOOK.add(FRAME_7,text="SequenceMatcher")
NOTE_BOOK.add(FRAME_9,text="METRICS")

FRAME_4.rowconfigure(0,weight=1)
FRAME_4.columnconfigure(0,weight=1)

#######################################################   FRAME 5  #####################################################
LABEL_10 = tk.Label(FRAME_5,text=T_12,bg=B_C,fg=F_C,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+2))
LABEL_13 = tk.Label(FRAME_5,textvariable=VARIABLE_TEXT_3,bg=B_C,fg=C_2,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)))
LIST_BOX_3 = tk.Listbox(FRAME_5,height=22,width=40)
LIST_BOX_4 = tk.Listbox(FRAME_5,height=22,width=40)
SCROLL_BAR_3 = tk.Scrollbar(FRAME_5,orient=tk.VERTICAL)
SCROLL_BAR_4 = tk.Scrollbar(FRAME_5,orient=tk.HORIZONTAL)
SCROLL_BAR_5 = tk.Scrollbar(FRAME_5,orient=tk.VERTICAL)
SCROLL_BAR_6 = tk.Scrollbar(FRAME_5,orient=tk.HORIZONTAL)
BUTTON_10 = tk.Button(FRAME_5,text=B_2,command=lambda:FRAME_3.tkraise(),width=6,font= FONT_1+str(int(F_S*ratio)),height=1,padx=10,pady=10)
LABEL_10.grid(column=0,row=2,columnspan=2,sticky=(tk.N,tk.S,tk.E))
LABEL_13.grid(column=3,row=2,sticky=(tk.W,tk.N,tk.S))
BUTTON_10.grid(column=5,row=2,sticky=(tk.E,tk.S))
LIST_BOX_3.grid(column=0,row=0,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
LIST_BOX_4.grid(column=3,row=0,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
SCROLL_BAR_3.grid(column=1,row=0,rowspan=2,sticky=(tk.N,tk.S,tk.W))
SCROLL_BAR_4.grid(column=0,row=2,sticky=(tk.W,tk.E,tk.N))
SCROLL_BAR_5.grid(column=4,row=0,rowspan=2,sticky=(tk.N,tk.S,tk.W))
SCROLL_BAR_6.grid(column=3,row=2,sticky=(tk.W,tk.E,tk.N))

SCROLL_BAR_3.config(command=LIST_BOX_3.yview)
SCROLL_BAR_4.config(command=LIST_BOX_3.xview)
LIST_BOX_3.config(yscrollcommand=SCROLL_BAR_3.set,xscrollcommand=SCROLL_BAR_4.set)
SCROLL_BAR_5.config(command=LIST_BOX_4.yview)
SCROLL_BAR_6.config(command=LIST_BOX_4.xview)
LIST_BOX_4.config(yscrollcommand=SCROLL_BAR_5.set,xscrollcommand=SCROLL_BAR_6.set)

for i in range(3):
	FRAME_5.rowconfigure(i,weight=1)
for i in range(6):
	FRAME_5.columnconfigure(i,weight=1)

#######################################################   FRAME 6  #####################################################
LABEL_11 = tk.Label(FRAME_6,text=T_12,bg=B_C,fg=F_C,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+2))
LABEL_14 = tk.Label(FRAME_6,textvariable=VARIABLE_TEXT_4,bg=B_C,fg=C_2,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)))

LIST_BOX_5 = tk.Listbox(FRAME_6,height=22,width=40)
LIST_BOX_6 = tk.Listbox(FRAME_6,height=22,width=40)
SCROLL_BAR_7 = tk.Scrollbar(FRAME_6,orient=tk.VERTICAL)
SCROLL_BAR_8 = tk.Scrollbar(FRAME_6,orient=tk.HORIZONTAL)
SCROLL_BAR_9 = tk.Scrollbar(FRAME_6,orient=tk.VERTICAL)
SCROLL_BAR_10 = tk.Scrollbar(FRAME_6,orient=tk.HORIZONTAL)
BUTTON_11 = tk.Button(FRAME_6,text=B_2,command=lambda:FRAME_3.tkraise(),width=6,font= FONT_1+str(int(F_S*ratio)),height=1,padx=10,pady=10)
LABEL_11.grid(column=0,row=2,columnspan=2,sticky=(tk.N,tk.S,tk.E))
LABEL_14.grid(column=3,row=2,sticky=(tk.W,tk.N,tk.S))

BUTTON_11.grid(column=5,row=2,sticky=(tk.E,tk.S))
LIST_BOX_5.grid(column=0,row=0,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
LIST_BOX_6.grid(column=3,row=0,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
SCROLL_BAR_7.grid(column=1,row=0,rowspan=2,sticky=(tk.N,tk.S,tk.W))
SCROLL_BAR_8.grid(column=0,row=2,sticky=(tk.W,tk.E,tk.N))
SCROLL_BAR_9.grid(column=4,row=0,rowspan=2,sticky=(tk.N,tk.S,tk.W))
SCROLL_BAR_10.grid(column=3,row=2,sticky=(tk.W,tk.E,tk.N))

SCROLL_BAR_7.config(command=LIST_BOX_5.yview)
SCROLL_BAR_8.config(command=LIST_BOX_5.xview)
LIST_BOX_5.config(yscrollcommand=SCROLL_BAR_7.set,xscrollcommand=SCROLL_BAR_8.set)
SCROLL_BAR_9.config(command=LIST_BOX_6.yview)
SCROLL_BAR_10.config(command=LIST_BOX_6.xview)
LIST_BOX_6.config(yscrollcommand=SCROLL_BAR_9.set,xscrollcommand=SCROLL_BAR_10.set)

for i in range(3):
	FRAME_6.rowconfigure(i,weight=1)
for i in range(6):
	FRAME_6.columnconfigure(i,weight=1)

#######################################################   FRAME 7  #####################################################

LABEL_11 = tk.Label(FRAME_7,text=T_12+"		% Using SequenceMatcher",bg=B_C,fg=F_C,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+2))
LABEL_14 = tk.Label(FRAME_7,textvariable=VARIABLE_TEXT_6,bg=B_C,fg=C_2,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)))
LABEL_11.grid(column=0,row=0,columnspan=2,sticky=(tk.N,tk.S,tk.E))
LABEL_14.grid(column=1,row=0,sticky=(tk.W,tk.N,tk.S))
BUTTON_12 = tk.Button(FRAME_7,text=B_2,command=lambda:FRAME_3.tkraise(),width=6,font= FONT_1+str(int(F_S*ratio)),height=1,padx=10,pady=10)

BUTTON_12.grid(column=5,row=2,sticky=(tk.E,tk.S))

for i in range(3):
	FRAME_7.rowconfigure(i,weight=1)
for i in range(6):
	FRAME_7.columnconfigure(i,weight=1)

#######################################################   FRAME 8  #####################################################

LIST_BOX_9 = tk.Listbox(FRAME_8,height=22,width=40)
LIST_BOX_10 = tk.Listbox(FRAME_8,height=22,width=40)
SCROLL_BAR_15 = tk.Scrollbar(FRAME_8,orient=tk.VERTICAL)
SCROLL_BAR_16 = tk.Scrollbar(FRAME_8,orient=tk.HORIZONTAL)
SCROLL_BAR_17 = tk.Scrollbar(FRAME_8,orient=tk.VERTICAL)
SCROLL_BAR_18 = tk.Scrollbar(FRAME_8,orient=tk.HORIZONTAL)
BUTTON_13 = tk.Button(FRAME_8,text=B_2,command=lambda:FRAME_3.tkraise(),width=6,font= FONT_1+str(int(F_S*ratio)),height=1,padx=10,pady=10)

BUTTON_13.grid(column=5,row=2,sticky=(tk.E,tk.S))
LIST_BOX_9.grid(column=0,row=0,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
LIST_BOX_10.grid(column=3,row=0,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
SCROLL_BAR_15.grid(column=1,row=0,rowspan=2,sticky=(tk.N,tk.S,tk.W))
SCROLL_BAR_16.grid(column=0,row=2,sticky=(tk.W,tk.E,tk.N))
SCROLL_BAR_17.grid(column=4,row=0,rowspan=2,sticky=(tk.N,tk.S,tk.W))
SCROLL_BAR_18.grid(column=3,row=2,sticky=(tk.W,tk.E,tk.N))

SCROLL_BAR_15.config(command=LIST_BOX_9.yview)
SCROLL_BAR_16.config(command=LIST_BOX_9.xview)
LIST_BOX_9.config(yscrollcommand=SCROLL_BAR_15.set,xscrollcommand=SCROLL_BAR_16.set)
SCROLL_BAR_17.config(command=LIST_BOX_10.yview)
SCROLL_BAR_18.config(command=LIST_BOX_10.xview)
LIST_BOX_10.config(yscrollcommand=SCROLL_BAR_17.set,xscrollcommand=SCROLL_BAR_18.set)

for i in range(3):
	FRAME_8.rowconfigure(i,weight=1)
for i in range(6):
	FRAME_8.columnconfigure(i,weight=1)

#######################################################   FRAME 9  #####################################################
LABEL_12 = tk.Label(FRAME_9,text=T_12,bg=B_C,fg=F_C,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)+2))
LABEL_15 = tk.Label(FRAME_9,textvariable=VARIABLE_TEXT_5,bg=B_C,fg=C_2,justify=tk.LEFT,padx=10,pady=10,font=FONT_1+str(int(F_S*ratio)))

LIST_BOX_11 = tk.Listbox(FRAME_9,height=22,width=40)
LIST_BOX_12 = tk.Listbox(FRAME_9,height=22,width=40)
SCROLL_BAR_19 = tk.Scrollbar(FRAME_9,orient=tk.VERTICAL)
SCROLL_BAR_20 = tk.Scrollbar(FRAME_9,orient=tk.HORIZONTAL)
SCROLL_BAR_21 = tk.Scrollbar(FRAME_9,orient=tk.VERTICAL)
SCROLL_BAR_22 = tk.Scrollbar(FRAME_9,orient=tk.HORIZONTAL)
BUTTON_14 = tk.Button(FRAME_9,text=B_2,command=lambda:FRAME_3.tkraise(),width=6,font= FONT_1+str(int(F_S*ratio)),height=1,padx=10,pady=10)
LABEL_12.grid(column=0,row=2,columnspan=2,sticky=(tk.N,tk.S,tk.E))
LABEL_15.grid(column=3,row=2,sticky=(tk.W,tk.N,tk.S))

BUTTON_14.grid(column=5,row=2,sticky=(tk.E,tk.S))
LIST_BOX_11.grid(column=0,row=0,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
LIST_BOX_12.grid(column=3,row=0,rowspan=2,sticky=(tk.W,tk.E,tk.N,tk.S))
SCROLL_BAR_19.grid(column=1,row=0,rowspan=2,sticky=(tk.N,tk.S,tk.W))
SCROLL_BAR_20.grid(column=0,row=2,sticky=(tk.W,tk.E,tk.N))
SCROLL_BAR_21.grid(column=4,row=0,rowspan=2,sticky=(tk.N,tk.S,tk.W))
SCROLL_BAR_22.grid(column=3,row=2,sticky=(tk.W,tk.E,tk.N))

SCROLL_BAR_19.config(command=LIST_BOX_11.yview)
SCROLL_BAR_20.config(command=LIST_BOX_11.xview)
LIST_BOX_11.config(yscrollcommand=SCROLL_BAR_19.set,xscrollcommand=SCROLL_BAR_20.set)
SCROLL_BAR_21.config(command=LIST_BOX_4.yview)
SCROLL_BAR_22.config(command=LIST_BOX_4.xview)
LIST_BOX_12.config(yscrollcommand=SCROLL_BAR_21.set,xscrollcommand=SCROLL_BAR_22.set)

for i in range(3):
	FRAME_9.rowconfigure(i,weight=1)
for i in range(6):
	FRAME_9.columnconfigure(i,weight=1)

########################################################################################################################

WINDOW.rowconfigure(0,weight=1)
WINDOW.columnconfigure(0,weight=1)
FRAME_1.tkraise()
WINDOW.protocol("WM_DELETE_WINDOW",quit_function)
WINDOW.mainloop()
###################################################### END OF PROGRAM ######################################################

"""
PLAGIARISM DETECTION SOFTWARE VERSION 1.0
DATE: 04/11/2019 TIME:  02:15 AM
DONE BY:
	SAMEER RATHOD		( GUI )
	HRUSHIKESH JOSHI	( CODING )
	MANAS JOSHI			( TESTING )
"""
