# ReadUPG

This is a very rough UPG reader/extractor for firmware files like the one that come with the gw-instek osciloskopes. 

Usage: python3 readupg.py fw_file.upg

Files are exctracted to the extract/ folder. Further extraction of the main root-fs (UBI image!) can be done with
~# ubireader_extract_files rootfs.img



