#install pip if it is not installed in your sistem 
#then install ntplib using pip install ntplib 
#for arch-linux you need to use AUR helper to install ntplib like "yay" which is I am using on my system
#yay -S python-ntplib

import ntplib
from time import ctime, time

def sntp_time_sync():
    try:
    
        client = ntplib.NTPClient();

        response = client.request('pool.ntp.org', version=3);

        server_time = ctime(response.tx_time);
        local_time = ctime(time());

        print(f"Server time (from pool.ntp.org): {server_time}");
        print(f"Local system time:               {local_time}");

        #compare times 
        diff = response.tx_time - time()
        print(f"\nTime difference: {diff:.3f} seconds");

    except Exception as e:
        print("Error while synchronizing time:", e);


sntp_time_sync();
