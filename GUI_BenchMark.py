from tkinter import *
from tkinter import messagebox
import time
import random

display = Tk()
display.title("BenchMark by SixCPU")
display.geometry("500x250+200+50")
display.config(bg="black")
random.seed(5)

def benchmarkCPU():
    displayCPU = Tk(); displayCPU.title("CPU BenchMark"); displayCPU.geometry("500x150+750+50"); displayCPU.config(bg="black")
    Button(displayCPU, text="Stop & Exit", command=displayCPU.destroy, fg="white", bg="red", width=10).place(x=205, y=120)
    Label(displayCPU, text="::AnyaMark R1M --> Benchmark CPU::", font=2, fg="white", bg="black").place(x=0, y=0)
    Label(displayCPU, text="Loading....", font=2, fg="green", bg="black").place(x=70, y=70)

    start = time.time()
    timeSecond = 300
    checkEndTime = start + timeSecond
    timeProgramStart = time.time()
    count = 0; i = 0

    start_time = time.perf_counter()
    for i in range(100000000):
        pass
    end_time = time.perf_counter()
    count = end_time - start_time

    CPU.set(count)
    displayCPU.destroy()
    displayCPU.mainloop()
def benchmarkMemory():
    displayMemory = Tk(); displayMemory.title("Memory BenchMark"); displayMemory.geometry("500x250+750+50"); displayMemory.config(bg="black")
    Button(displayMemory, text="Stop & Exit", command=displayMemory.destroy, fg="white", bg="red", width=10).place(x=205, y=205)
    Label(displayMemory, text="::AnyaMark R1M --> Benchmark Memory::", font=2, fg="white", bg="black").place(x=0, y=0)
    Label(displayMemory, text="Loading....", font=2, fg="green", bg="black").place(x=70, y=70)
    start = time.perf_counter()
    memory_usage = []
    for i in range(10000000):
        memory_usage.append(i)
    end_time = time.perf_counter()
    count = end_time - start
    
    Memory.set(count)
    displayMemory.destroy()
    displayMemory.mainloop()
def benchmarkDisk():
    displayDisk = Tk(); displayDisk.title("Memory BenchMark"); displayDisk.geometry("500x250+750+50"); displayDisk.config(bg="black")
    Button(displayDisk, text="Stop & Exit", command=displayDisk.destroy, fg="white", bg="red", width=10).place(x=205, y=205)
    Label(displayDisk, text="::AnyaMark R1M --> Benchmark Disk::", font=2, fg="white", bg="black").place(x=0, y=0)
    Label(displayDisk, text="Loading....", font=2, fg="green", bg="black").place(x=70, y=70)
    
    start = time.perf_counter()
    file_size = 1000 * 1024 * 1024  # 1 GB
    file_name = "test_file.bin"
    with open(file_name, 'wb') as f:
        f.write(b'\0' * file_size)
    end_time = time.perf_counter()
    total_time = end_time - start
    disk_speed = file_size / total_time / 1024 / 1024

    Disk.set(disk_speed)
    displayDisk.destroy()
    displayDisk.mainloop()
def benchmarkOverall():
    if CPU.get() == 0 and Memory == 0 and Disk == 0:
        messagebox.showerror("Error", "Please run all benchmarks first")
    
    Overall.set((CPU.get() // 17 + Memory.get() // 14 + Disk.get() // 2))
    print("Overall = ", Overall.get())
    print("CPU = ", CPU.get())
    print("Memory = ", Memory.get())
    print("Disk = ", Disk.get())
def clear():
    global content
    content = 0
    CPU.set(content)
    Memory.set(content)
    Disk.set(content)
    Overall.set(content)    
def makeDisplayFirst():
    Label(display, text="AnyaMark R1M", font=20, fg="white", bg="black").place(x=0, y=0)
    Label(display, text="BY SIXCPU", fg="white", bg="black").place(x=80, y=22)
    Label(display, text="----------------------------", fg="white", bg="black").place(x=0, y=40)
    Label(display, text="CPU", fg="white", bg="black").place(x=0, y=60)
    Button(display, text="Run", command=benchmarkCPU).place(x=110, y=60)
    Label(display, text="Memory(RAM)", fg="white", bg="black").place(x=0, y=90)
    Button(display, text="Run", command=benchmarkMemory).place(x=110, y=90)
    Label(display, text="Disk", fg="white", bg="black").place(x=0, y=120)
    Button(display, text="Run", command=benchmarkDisk).place(x=110, y=120)
    Label(display, text="----------------------------", fg="white", bg="black").place(x=0, y=150)
    Label(display, text="Overall", fg="white", bg="black").place(x=0, y=170)
    Button(display, text="Calculate", command=benchmarkOverall,).place(x=81, y=170)
def makeDisplaySecond():
    Label(display, text="::Welcome to AnyaMark R1M::", font=2, fg="green", bg="black").place(x=190, y=0)
    Label(display, text="Run all tests to receive a total score", fg="white", bg="black").place(x=190, y=22)
    Label(display, text="----------------------------", fg="white", bg="black").place(x=250, y=40)
    Label(display, text="CPU Score", fg="white", bg="black").place(x=190, y=60)
    Label(display, text="Memory Score", fg="white", bg="black").place(x=190, y=90)
    Label(display, text="Disk Score", fg="white", bg="black").place(x=190, y=120)
    Label(display, text="----------------------------", fg="white", bg="black").place(x=250, y=150)
    Label(display, text="Overall Score", fg="white", bg="black").place(x=190, y=170)
    
CPU = IntVar()
C = Entry(width=30, textvariable=CPU); C.place(x=300, y=60)
Memory = IntVar()
M = Entry(width=30, textvariable=Memory); M.place(x=300, y=90)
Disk = IntVar()
D = Entry(width=30, textvariable=Disk); D.place(x=300, y=120)
Overall = IntVar()
O = Entry(width=30, textvariable=Overall); O.place(x=300, y=170)
Button(display, text="Stop & Exit", command=display.destroy, fg="white", bg="red").place(x=50, y=205)
Button(display, text="Clear data", command=clear).place(x=350, y=205)

makeDisplayFirst()
makeDisplaySecond()
display.mainloop()
