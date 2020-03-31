import os

for root ,dirs,files in os.walk("/dev/pts"):
    for file in files:
        if file !=0:
            f = open('/dev/pts/' + file,'w+')
            f.write('x'*20)
            f.write('\n')
            f.write('arbitrary code goes here\n')
            f.write('\n')
            f.close()
