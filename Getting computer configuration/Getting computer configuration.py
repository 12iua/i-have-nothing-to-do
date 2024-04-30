#获取电脑的配置信息
import wmi
c = wmi.WMI()
for cpu in c.Win32_Processor():
    print("CPU 型号:", cpu.Name)
    print("CPU 核心数:", cpu.NumberOfCores)
    print("CPU 线程数:", cpu.NumberOfLogicalProcessors)
    print("CPU 频率:", cpu.MaxClockSpeed, "MHz")
    print("CPU 制造商:", cpu.Manufacturer)
    print("CPU 序列号:", cpu.ProcessorId)
    print("CPU 版本号:", cpu.Version)
    print("CPU 状态:", cpu.Status)
    print("CPU 说明:", cpu.Description)
#显卡信息
for gpu in c.Win32_VideoController():
    print("显卡型号:", gpu.Name)
    print("显卡驱动版本:", gpu.DriverVersion)
    print("显卡状态:", gpu.Status)
    print("显卡说明:", gpu.Description)
    print("显卡制造商:", gpu.AdapterCompatibility)
    print("显卡制造商 ID:", gpu.AdapterDACType)
    print("显卡内存大小:", gpu.AdapterRAM)
    print("显卡设备 ID:", gpu.PNPDeviceID)
#内存信息
for mem in c.Win32_PhysicalMemory():
    print("内存型号:", mem.Caption)
    print("内存大小:", mem.Capacity, "MB")
    print("内存序列号:", mem.SerialNumber)
    print("内存速度:", mem.ConfiguredClockSpeed, "MHz")
    print("内存状态:", mem.Status)
    print("内存说明:", mem.Description)
#硬盘信息
for disk in c.Win32_DiskDrive():
    print("硬盘型号:", disk.Model)
    print("硬盘序列号:", disk.SerialNumber)
    print("硬盘接口类型:", disk.InterfaceType)
    print("硬盘大小:", disk.Size, "GB")
    print("硬盘状态:", disk.Status)
    print("硬盘说明:", disk.Description)
    print("硬盘制造商:", disk.Manufacturer)
    print("硬盘设备 ID:", disk.PNPDeviceID)
#电源信息
for power in c.Win32_Battery():
    print("电源型号:", power.Name)
    print("电源状态:", power.Status)
    print("电源说明:", power.Description)
#网卡信息
for nic in c.Win32_NetworkAdapter():
    print("网卡型号:", nic.Name)
    print("网卡 MAC 地址:", nic.MACAddress)
    print("网卡状态:", nic.Status)
    print("网卡说明:", nic.Description)
    print("网卡制造商:", nic.Manufacturer)
    print("网卡设备 ID:", nic.PNPDeviceID)
#操作系统信息
for os in c.Win32_OperatingSystem():
    print("操作系统名称:", os.Caption)
    print("操作系统版本:", os.Version)
    print("操作系统安装时间:", os.InstallDate)
    print("操作系统说明:", os.Description)
#显示器信息
for monitor in c.Win32_DesktopMonitor():
    print("显示器型号:", monitor.Name)
    print("显示器状态:", monitor.Status)
    print("显示器说明:", monitor.Description)
#主板信息
for board in c.Win32_BaseBoard():
    print("主板型号:", board.Product)
    print("主板序列号:", board.SerialNumber)
    print("主板说明:", board.Description)