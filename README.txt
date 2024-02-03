to install please run the following command in the terminal while in this directory
pip install -r requirements.txt
everything needed for c++ is in the backend files

TYLER FUCKING READ THIS SHIT AT SOME POINT YOU GOD DAMN BAFOON
to compile on windows use the below command
    g++ -o my_capture_program packetcap.cc -I. -L. -lwpcap -liphlpapi
to compile on linux use the below command
    g++ -o my_capture_program packetcap.cc -I. -L. -lpcap
