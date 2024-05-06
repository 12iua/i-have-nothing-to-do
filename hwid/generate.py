import platform
import hashlib

def generate_hwid():
    # Get the machine's hardware and software characteristics
    machine_id = platform.node()  # Machine's network name (may be the hardware UUID)
    os_info = platform.system() + platform.release()  # Operating system name and release number

    # Combine the machine ID and OS info into a single string
    combined_info = machine_id + os_info

    # Generate a HWID by hashing the combined info
    hwid = hashlib.md5(combined_info.encode()).hexdigest()

    return hwid

#save hwid to file
with open("hwid.txt", "w") as f:
    f.write(generate_hwid())