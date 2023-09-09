import subprocess
import re
import re
output = subprocess.check_output("systeminfo", shell=True, universal_newlines=True)
physical_memory_total_match = re.search(r"物理内存总量:\s+([\d,]+) MB", output)
physical_memory_available_match = re.search(r"可用的物理内存:\s+([\d,]+) MB", output)
virtual_memory_total_match = re.search(r"虚拟内存: 最大值:\s+([\d,]+) MB", output)
virtual_memory_available_match = re.search(r"虚拟内存: 使用中:\s+([\d,]+) MB", output)
physical_memory_total = str(int(physical_memory_total_match.group(1).replace(",", "")))+"\n"
physical_memory_available = str(int(physical_memory_available_match.group(1).replace(",", "")))+"\n"
virtual_memory_total = str(int(virtual_memory_total_match.group(1).replace(",", "")))+"\n"
virtual_memory_available = str(int(virtual_memory_available_match.group(1).replace(",", "")))+"\n"
with open("get.txt","w+") as f:
    f.write(physical_memory_total)
    f.write(str(int(physical_memory_total)-int(physical_memory_available))+"\n")
    f.write(virtual_memory_total)
    f.write(virtual_memory_available)