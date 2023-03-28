#!/usr/bin/env python3

import psutil

# Variable
Get_Some_Info = psutil.cpu_times()

# Give me the info I am asking for
print("Time linux kernel spent running guest OSs:", Get_Some_Info.guest)
print("Time in kernel mode:", Get_Some_Info.system)
print("Time in user mode:", Get_Some_Info.user)
print("Hardware device interrupts:", Get_Some_Info.irq)
print("I/O time:", Get_Some_Info.iowait)
print("Priority processes in user mode:", Get_Some_Info.nice)
print("OS interruptions:", Get_Some_Info.softirq)
print("Other OS times:", Get_Some_Info.steal)
print("Idle time:", Get_Some_Info.idle)
