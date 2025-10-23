#install pip if it is not installed in your sistem 
#then install ntplib using pip install ntplib 
#for arch-linux you need to use AUR helper to install ntplib like "yay" which is I am using on my system
#yay -S python-ntplib

import ntplib
from time import ctime, time
import logging

#logging config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
);

def sntp_time_sync():

    print("#"*56);
    print(" "*20 + " " + "SNTP Time Sync" +" " +" "*20);
    print("#"*56+"\n");

    try:
        client = ntplib.NTPClient();

        response = client.request('pool.ntp.org', version=3);

        server_time = ctime(response.tx_time);
        local_time = ctime(time());

        logging.info(f"Server time (from pool.ntp.org): {server_time}");
        logging.info(f"Local system time:               {local_time}");

        #compare times 
        diff = response.tx_time - time()
        logging.info(f"Time difference: {diff:.3f} seconds");

    except Exception as e:
        logging.error("Error while synchronizing time:", e);


if __name__ == "__main__":
    sntp_time_sync();

