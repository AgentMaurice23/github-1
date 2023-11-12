import tkinter as tk 
from tkinter import messagebox 


class Task:
    
    def __init__(self,nom,description,date):
        self.nom = nom
        self.description = description
        self.date = date
        
        
class TaskManager:
    
    def __init__(self,root):
        self.root=root
        self.root.title("taches")
        
        self.tasks=[]
        
        self.nomlabel=tk.Label(root,text="Nom")
        self.nomlabel.pack()
        self.nomentry=tk.Entry(root)
        self.nomentry.pack()
        
        self.descriptionlabel=tk.Label(root,text="Desciption")
        self.descriptionlabel.pack()
        self.descriptionentry=tk.Entry(root)
        self.descriptionentry.pack()
        
        self.datelabel=tk.Label(root,text="DateOfTâche")
        self.datelabel.pack()
        self.dateentry=tk.Entry(root)
        self.dateentry.pack()
        
        self.addBouton=tk.Button(root,text="Ajouter",command=self.add_tache)
        self.addBouton.pack()
        
        self.Listebox=tk.Listbox(root)
        self.Listebox.pack()
        
        self.removeButton=tk.Button(root,text="Supprimer",command=self.removetache)
        self.removeButton.pack()
        
    def add_tache(self):
        
        nom=self.nomentry.get()
        description=self.descriptionentry.get()
        date=self.dateentry.get()
        if nom and description and date:
            tache = Task(nom,description,date)
            self.tasks.append(tache)
            self.Listebox.insert(tk.END,nom)
            self.clearentries()
        else:
            messagebox.showwarning("Error", "veillez remplir tous les champs")
        
    def clearentries(self):
        self.nomentry.delete(0,tk.END)
        self.descriptionentry.delete(0,tk.END)
        self.dateentry.delete(0,tk.END)
        
    def removetache(self):
        selection=self.Listebox.curselection()
        if selection:
            index=selection[0]
            del self.tasks[index]
            self.Listebox.delete(index)
        else:
            messagebox.showwarning("Error","Aucun élément choisit")

if __name__ == "__main__":
    root=tk.Tk()
    app=TaskManager(root)
    root.mainloop()