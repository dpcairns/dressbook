#-*- coding: iso-8859-1 -*-

from Tkinter import *
import os
import fileinput
import sys
folder = os.path.abspath("dresses")
class Dress:
	def __init__(self, first_name, last_name, street, city, state, zip, phone):
		self.first_name = first_name
		self.last_name = last_name
		self.street = street
		self.city = city
		self.state = state
		self.zip = zip
		self.phone = phone
		self.note = []

	def add_note(self, new_note): 
		self.note.append(new_note)

	def read_all(self):
		print "First name: " + self.first_name
		print "Last name: "+self.last_name
		print "Street: "+self.street
		print "City: "+self.city
		print "State: "+self.state
		print "Zip Code: "+self.zip
		print "Phone number: " + self.phone
		print self.note

def delete_this_dress(filename, filename_clean, t):

	frame = Frame (t)
	frame.pack()
	label_edit = Label(frame, text="Which dress do you want to edit?")
	label_edit.pack()	
	delete_button = Button(frame, text="confirm deletion of"+filename_clean, command=lambda:os.remove(folder+"/"+filename))
	delete_button.pack()

def create_dress(nickname, first_name, last_name, street, city, state, zip, phone, frame):
	nickname = Dress(first_name, 
					last_name, 
					street,
					city,
					state, 
					zip, 
					phone)
	nickname.read_all()

	s = "First name: " + nickname.first_name + "\n"
	s += "Last name: " + nickname.last_name + "\n"
	s += "Street: " + nickname.street + "\n"
	s += "City: " + nickname.city + "\n"
	s += "State: " + nickname.state + "\n"
	s += "Zip: " + nickname.zip + "\n"
	s += "Phone number:: " + nickname.phone + "\n"
	completeName = os.path.abspath("dresses/%s,%s.txt" % (nickname.last_name, nickname.first_name))
	dress_file = open(completeName, 'w')
	dress_file.write(s)
	dress_file.close()
	filename = nickname.last_name+","+nickname.first_name+".txt"
	filename_clean = nickname.last_name+","+nickname.first_name


	show_this_dress_query_button= Button(frame, 
							text="See the new dress?", 
							command=lambda: show_this_dress(filename, filename_clean))
	show_this_dress_query_button.pack()

def on_button_click(nickname, first_name, last_name, street, city, state, zip, phone, frame):
	new_nickname = nickname.get() 
	new_first_name = first_name.get() 
	new_last_name = last_name.get() 
	new_street = street.get() 
	new_city = city.get() 
	new_state = state.get()
	new_zip = zip.get() 
	new_phone = phone.get() 
	create_dress(new_nickname, new_first_name, new_last_name, new_street, new_city, new_state, new_zip, new_phone, frame)



def new_dress():
	t = Toplevel(root)
	t.minsize(250, 5)
	icon_label=Label(t, image=icon)
	icon_label.pack(anchor=E)
	t.geometry('+460+80') 
	t.wm_title("'dress maker")
	
	status = Label(t, text="© 2015 Danny Cairns", bg="white", bd=1, relief=SUNKEN, anchor=W)
	status.pack(side=BOTTOM, fill=X)

	frame = Frame (t)
	frame.pack(side=RIGHT)

	label_new_dress_nickname = Label(frame, text="What is the nickname of this entry?")
	label_new_dress_nickname.pack()
	entry_new_dress_nickname = Entry(frame)
	entry_new_dress_nickname.pack()

	label_new_dress_first_name = Label(frame, text="What is the first name of this entry?")
	label_new_dress_first_name.pack()
	entry_new_dress_first_name = Entry(frame)
	entry_new_dress_first_name.pack()


	label_new_dress_last_name = Label(frame, text="What is the last name of this entry?")
	label_new_dress_last_name.pack()
	entry_new_dress_last_name = Entry(frame)
	entry_new_dress_last_name.pack()


	label_new_dress_street = Label(frame, text="What is the street of this entry?")
	label_new_dress_street.pack()
	entry_new_dress_street = Entry(frame)
	entry_new_dress_street.pack()


	label_new_dress_city = Label(frame, text="What is the city of this entry?")
	label_new_dress_city.pack()
	entry_new_dress_city = Entry(frame)
	entry_new_dress_city.pack()

	label_new_dress_state = Label(frame, text="What is the state of this entry?")
	label_new_dress_state.pack()
	entry_new_dress_state = Entry(frame)
	entry_new_dress_state.pack()


	label_new_dress_zip = Label(frame, text="What is the zip code of this entry?")
	label_new_dress_zip.pack()
	entry_new_dress_zip = Entry(frame)
	entry_new_dress_zip.pack()


	label_new_dress_phone = Label(frame, text="What is the phone number of this entry?")
	label_new_dress_phone.pack()
	entry_new_dress_phone = Entry(frame)
	entry_new_dress_phone.pack()


	b = Button(frame, text="save this dress", command=lambda: on_button_click( 
				entry_new_dress_nickname, 
				entry_new_dress_first_name,
				entry_new_dress_last_name, 
				entry_new_dress_street,
			 	entry_new_dress_city, 
			 	entry_new_dress_state, 
			 	entry_new_dress_zip,
			  	entry_new_dress_phone,
			  	frame))
	b.pack()




	cancel_button = Button(frame, text="cancel", command=t.destroy)
	cancel_button.config(bg="pink", fg="red")
	cancel_button.pack()

def edit_dress():
	t = Toplevel(root)
	t.geometry('+650+150')
	t.minsize(250, 5)
	icon_label=Label(t, image=icon)
	icon_label.pack(anchor=E)
	t.wm_title("'dress editor")
	status = Label(t, text="© 2015 Danny Cairns", bg="white", bd=1, relief=SUNKEN, anchor=W)
	status.pack(side=BOTTOM, fill=X)

	frame = Frame(t)
	frame.pack()
	label_edit = Label(frame, text="Which dress do you want to edit?")
	label_edit.pack()	
	for filename in os.listdir (folder):
		filename_clean, txt = filename.split(".")
			#filename=filename is necessary because lambda create a clusre from first item in loop, 
			#resulting in only the first entry being passed along to all instances, for some reason...
		edit_this_dress_button= Button(frame, text=filename_clean, command=lambda filename=filename,filename_clean=filename_clean:edit_this_dress(filename, filename_clean, t))
		edit_this_dress_button.pack()

	cancel_button = Button(t, text="cancel", command=t.destroy)
	cancel_button.config(bg="pink", fg="red")
	cancel_button.pack(side=BOTTOM)



def edit_this_dress(filename, filename_clean, t):

	frame = Frame(t)
	frame.pack()
	label_edit_this_dress = Label(frame, text="Which category do you want to edit?")
	label_edit_this_dress.pack()	
	this_dress = open(folder+"/"+filename, 'r')
	lines = this_dress.read().splitlines()
	for each_line in lines:
		edit_this_dress_category = Button(frame, text=each_line, command=lambda filename=filename, each_line=each_line:edit_category(each_line, filename, filename_clean, t))
		edit_this_dress_category.pack()

def edit_category(each_line, filename, filename_clean, t):
	frame = Frame (t)
	frame.pack()
	label_edit_this_category1 = Label(frame, text = "So you want to change " + each_line + ". . .") 
	label_edit_this_category1.pack()
	label_edit_this_category2 = Label(frame, text="Okay, what do you want to change it to?")
	label_edit_this_category2.pack()
	entry_this_category = Entry(frame)
	entry_this_category.pack()
	edit_this_category_button = Button(frame, 
								text="change to this", 
								command=lambda: on_button_click_edit(
								each_line,
								entry_this_category,
								filename,
								filename_clean,
								t))
	edit_this_category_button.pack()



def on_button_click_edit(each_line, entry_this_category, filename, filename_clean, t):
	frame = Frame (t)
	frame.pack()
	category_name, old_category_item = each_line.split(": ") 
	new_category_item = entry_this_category.get()
	replaceAll(folder+"/"+filename,old_category_item,new_category_item)
	show_this_dress_query_button= Button(frame, 
							text="See the updated dress?", 
							command=lambda: show_this_dress(filename, filename_clean))
	show_this_dress_query_button.pack()

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def show_all_dresses():
	t = Toplevel(root)
	t.minsize(200, 5)
	t.wm_title("See all 'dresses")
	t.geometry('+460+150') 
	icon_label=Label(t, image=icon)
	icon_label.pack(anchor=E)
	status = Label(t, text="© 2015 Danny Cairns", bg="white", bd=1, relief=SUNKEN, anchor=W)
	status.pack(side=BOTTOM, fill=X)
	frame = Frame (t)
	frame.pack()
	for filename in os.listdir(folder):		
		filename_clean, txt = filename.split(".")
			#filename=filename is necessary because lambda create a clusre from first item in loop, 
			#resulting in only the first entry being passed along to all instances, for some reason...
		show_this_dress_button= Button(frame, text=filename_clean, command=lambda filename=filename, filename_clean=filename_clean:show_this_dress(filename, filename_clean))
		show_this_dress_button.pack()

	cancel_button = Button(frame, text="cancel", command=t.destroy)
	cancel_button.config(bg="pink", fg="red")
	cancel_button.pack()

def show_this_dress(filename, filename_clean):
	t = Toplevel(root)
	t.minsize(250, 5)
	t.wm_title("'dress viewer")
	t.geometry('+500+300') 
	icon_label=Label(t, image=icon)
	icon_label.pack(anchor=E)
	status = Label(t, text="© 2015 Danny Cairns", bg="white", bd=1, relief=SUNKEN, anchor=W)
	status.pack(side=BOTTOM, fill=X)
	label_edit_this_dress = Label(t, text=filename_clean+"'s dress")
	label_edit_this_dress.pack()
	this_dress = open(folder+"/"+filename, 'r')
	lines = this_dress.read().splitlines()
	for each_line in lines:
		show_label = Label(t, text=each_line)
		show_label.pack()
	edit_this_specific_dress_button= Button(t, text="Edit this dress?", command=lambda:edit_this_dress(filename, filename_clean, t))
	edit_this_specific_dress_button.pack()
	delete_this_dress_button= Button(t, text="Delete this dress?", command=lambda:delete_this_dress(filename, filename_clean, t))
	delete_this_dress_button.pack()
	cancel_button = Button(t, text="cancel", command=t.destroy)
	cancel_button.config(bg="pink", fg="red")
	cancel_button.pack(side=BOTTOM)
def _quit(event):
    root.destroy()

root = Tk()
icon = PhotoImage(file="favicon1.png")
root.tk.call('wm', 'iconphoto', root._w, icon)
root.wm_title("'dressbook | Today's address book")
root.geometry('400x120+140+80')
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New 'dress", command=new_dress)
subMenu.add_command(label="View all 'dresses", command=show_all_dresses) 
subMenu.add_separator()
subMenu.add_command(label="Quit", command=_quit)

editMenu = Menu(menu)
menu.add_cascade(labe="Edit", menu=editMenu)
editMenu.add_command(label="Edit 'dress", command=edit_dress) 

menu.add_cascade(image=icon)


w = Frame(root)
w.pack()
label1 = Label(w, text="Welcome to dressBook!")
label1.pack()

new_dress_button = Button(w, text ="New dress", command=new_dress)
new_dress_button.config(bg="lightgreen", fg="green")
new_dress_button.pack(side=LEFT)

edit_dress_button = Button(w, text="Edit dress", command=edit_dress)
edit_dress_button.config(bg="lightyellow", fg="orange")
edit_dress_button.pack(side=LEFT)


view_dress_button = Button(w, text="View all dresses", command=show_all_dresses)
view_dress_button.config(bg="lightblue", fg="blue")
view_dress_button.pack(side=LEFT)

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=10)

x = Frame(root)
x.pack()
quit_button = Button(x, width=150, text="quit 'dressbook")
quit_button.bind("<Button-1>", _quit)
quit_button.config(bg="pink", fg="red")
quit_button.pack(fill=X)

status = Label(root, text="© 2015 Danny Cairns", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.bind('<Control-Q>', _quit)
root.bind('<Control-q>', _quit)

root.mainloop()