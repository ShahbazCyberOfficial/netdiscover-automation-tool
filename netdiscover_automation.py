import subprocess
print("""
==========================================================
             NETDISCOVER AUTOMATION TOOL v1.0
==========================================================

Developed by: Shahbaz Bhutta

This tool performs:
✓ Live Host Discovery
✓ Network Range Scanning
✓ MAC Address Detection
✓ Vendor Identification

----------------------------------------------------------
Important Note:
• Use this tool only on networks you own or are authorized
  to assess.
• Network discovery may take some time depending on the
  network size.
• Please wait until the scanning process is completed.
==========================================================
""")
try:
    # ============================
    # Collect User Input
    # ============================

    interface = input("Enter Network Interface (e.g., eth0 / wlan0): ")
    iprange = input("Enter Network Range (e.g., 192.168.1.0/24): ")
    


except KeyboardInterrupt:
    print("\n\n[!] Input cancelled by user.")
    print("[+] Exiting Netdiscover Automation Tool...")
    exit()
try:
   # ============================
   # Start Network Discovery
   # ============================

   print("\n[+] Network discovery started...")
   print("[+] Please wait while Netdiscover scans the target network...\n")
   subprocess.run(["netdiscover",
                   "-i",
                   interface,
                   "-r",
                   iprange
                   ])
       
except KeyboardInterrupt:
    print("\n\n[!] User interrupted the scan.")
    print("[+] Program terminated successfully.")
else:
    # ============================
    # Scan Completed Successfully
    # ============================

    print("\n[+] Scan completed successfully.")
    print("[+] Thank you for using Netdiscover Automation Tool!")   