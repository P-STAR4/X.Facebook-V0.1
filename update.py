import os,sys



PERINTAH = """
cd $HOME
mv data $HOME
mv results $HOME
cd ~
rm -rf X.Facebook-V0.1
git clone https://github.com/P-STAR4/X.Facebook-V0.1
cd $HOME
mv data X.Facebook-V0.1
mv results X.Facebook-V0.1
cd X.Facebook-V0.1
"""

RUN ="""
python run.py
"""

print(" |--> Tunggu Sebentar Sedang Update Script....")
os.system(PERINTAH)
print(' |')
print(' |')
print(' |--> Update Script Sudah Selesai...')
os.system("sleep 2")
os.system(RUN)
os.sys.exit()

