import tkinter as tk
from tkinter import simpledialog, messagebox

class SocialFeatures(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Social Features")
        self.geometry("400x300")
        
        self.friend_list = []
        self.group_chats = {}
        
        self.label = tk.Label(self, text="Social Features")
        self.label.pack(pady=10)
        
        self.add_friend_button = tk.Button(self, text="Add Friend", command=self.add_friend)
        self.add_friend_button.pack(pady=10)
        
        self.create_group_chat_button = tk.Button(self, text="Create Group Chat", command=self.create_group_chat)
        self.create_group_chat_button.pack(pady=10)
        
        self.plan_event_button = tk.Button(self, text="Plan Event", command=self.plan_event)
        self.plan_event_button.pack(pady=10)
        
    def add_friend(self):
        friend_name = simpledialog.askstring("Add Friend", "Enter friend's name:")
        if friend_name:
            self.friend_list.append(friend_name)
            messagebox.showinfo("Success", f"Friend '{friend_name}' added successfully!")
    
    def create_group_chat(self):
        group_name = simpledialog.askstring("Create Group Chat", "Enter group chat name:")
        if group_name:
            self.group_chats[group_name] = []
            messagebox.showinfo("Success", f"Group chat '{group_name}' created successfully!")
    
    def plan_event(self):
        event_name = simpledialog.askstring("Plan Event", "Enter event name:")
        if event_name:
            messagebox.showinfo("Success", f"Event '{event_name}' planned successfully!")

if __name__ == "__main__":
    app = SocialFeatures()
    app.mainloop()
