
# from PyQt5.QtGui import QFontDatabase
#
# print('1')
#
# font_id = QFontDatabase.addApplicationFont("./font/萝莉体.ttf")
#
# print('2')
#
# font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
#
# print('3')
#
# # 创建字体对象
# font = QtGui.QFont(font_name)
#
# # 创建样式表
# stylesheet = f'''
#     QLabel {{
#         font-family: {font_name};
#         font-size: 12px;
#         color: red;
#     }}
# '''


# import sys
# import time
# from multiprocessing import Process, Queue
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
# from PyQt5.QtCore import QThread, pyqtSignal
#
# # 步骤1: 创建一个用于执行任务的函数
# def process_task(task_id, queue):
#     time.sleep(2)  # 模拟任务处理时间
#     # 执行一些任务...
#     print(f"Processing task {task_id} in process {Process().name}")
#     # 将结果放入队列
#     queue.put(f"Task {task_id} finished")
#
# # 步骤2: 创建一个用于管理进程的类
# class ProcessManager(QThread):
#     finished = pyqtSignal()  # 所有进程结束时发出的信号
#
#     def __init__(self):
#         super().__init__()
#         self.queue = Queue()
#
#     def run(self):
#         # 创建并启动多个进程
#         processes = []
#         for i in range(5):  # 假设我们需要启动5个进程
#             p = Process(target=process_task, args=(i, self.queue))
#             processes.append(p)
#             p.start()
#
#         # 等待所有进程完成
#         for p in processes:
#             p.join()
#
#         # 处理队列中的结果
#         while not self.queue.empty():
#             result = self.queue.get()
#             print(result)
#
#         # 发出完成信号
#         self.finished.emit()
#
# # 步骤5: 在Qt主进程中使用ProcessManager
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Multiprocessing Example')
#         self.setGeometry(100, 100, 300, 200)
#
#         layout = QVBoxLayout()
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         start_button = QPushButton('Start Processes')
#         start_button.clicked.connect(self.start_processes)
#         layout.addWidget(start_button)
#
#         self.process_manager = ProcessManager()
#         self.process_manager.finished.connect(self.on_processes_finished)
#
#     def start_processes(self):
#         self.process_manager.start()
#
#     def on_processes_finished(self):
#         print("All processes have finished, and the main window is notified.")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec_())



# 一行流打印到999的所有素数，埃氏筛法，无上下文最快，时间复杂度O(nloglogn)

from functools import reduce
print((lambda n:sorted(list(reduce(lambda r,x:r-set(range(x**2,n,x)) if x in r else r,range(2,int(n**0.5)+1),set(range(2,n+1))))))(999))
