import socket
import threading
import tkinter as tk

class ChatClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")
        self.create_widgets()

    def create_widgets(self):
        self.message_listbox = tk.Listbox(self.root, width=50, height=20)
        self.message_listbox.pack(pady=10)

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(pady=10)
        self.message_entry.bind('<Return>', self.send_message_on_enter)  # 绑定回车键发送消息

        self.connect_to_server()

    def connect_to_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect(('127.0.0.1', 11451))

        self.prompt_for_username()  # 在连接服务器后，输入用户名

        receive_thread = threading.Thread(target=self.receive_message)
        receive_thread.start()

    def prompt_for_username(self):
        self.username = input("请输入您的用户名: ")
        self.server_socket.send(self.username.encode('utf-8'))

    def send_message(self, event=None):  # 将事件设置为默认为None，以便手动调用时不传入event参数
        message = self.message_entry.get()
        if message:
            if message.lower() == 'exit':
                self.server_socket.send('exit'.encode('utf-8'))
                self.server_socket.close()
                self.root.destroy()
            else:
                self.server_socket.send(message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)

    def send_message_on_enter(self, event):
        self.send_message()  # 回车键触发的事件处理函数

    def receive_message(self):
        while True:
            try:
                message = self.server_socket.recv(1024).decode('utf-8')
                self.message_listbox.insert(tk.END, message)
            except:
                self.message_listbox.insert(tk.END, "与服务器的连接中断。")
                self.server_socket.close()
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClientGUI(root)
    root.mainloop()
