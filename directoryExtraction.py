import gdb
import os

MEMORY_ADDRESS = '*main+0xb5'

class WatchAndExtract(gdb.Breakpoint):
    def __init__(self):
        super().__init__(MEMORY_ADDRESS, internal=False)

    def stop(self):
        # Get the memory address
        rax = gdb.parse_and_eval('$rax')

        # Read the value 
        value = gdb.execute(f"x/s {rax}", to_string=True).strip()

        # Creating directories based on the value
        folder_path = value.split(':')[1].strip().strip('"').rstrip('/')

        if folder_path:
            # Create the directory if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
        
        return False
        
WatchAndExtract()
print(f"[+] Breakpoint set at {MEMORY_ADDRESS}. Waiting for the program to hit the breakpoint...")