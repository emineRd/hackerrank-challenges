import re

x = raw_input()

match = re.search(r'[0-9a-zA-BE-HJKN-UWYZ]', x)    
##################################################    
if match:
    print match.group()
    print 'False'
###################################
elif re.search(r'VV{1,}',x):
    print 'False'
elif re.search(r'LL{1,}',x):
    print 'False'
elif re.search(r'DD{1,}',x):
    print 'False'
###################################
elif re.search(r'I{4,}',x):
    print 'False' 
elif re.search(r'X{4,}',x):
    print 'False' 
elif re.search(r'C{4,}',x):
    print 'False'
elif re.search(r'M{4,}',x):
    print 'False'
###################################
elif re.search(r'I[LCDM]',x):
    print 'False'    
elif re.search(r'V[XCLDM]',x):
    print 'False'    
elif re.search(r'X[DM]',x):
    print 'False' 
elif re.search(r'L[CDM]',x):
    print 'False' 
################################### 
elif re.search(r'III[VXLCDM]',x):
    print 'False'    
elif re.search(r'XXX[LCDM]',x):
    print 'False'    
elif re.search(r'CCC[DM]',x):
    print 'False' 
###################################
elif re.search(r'IX[IVXLCDM]',x):
    print 'False' 
elif re.search(r'IV[IVXLCDM]',x):
    print 'False'  
elif re.search(r'XL[XLCDM]',x):
    print 'False'    
elif re.search(r'XC[XLCDM]',x):
    print 'False'    
elif re.search(r'CM[DM]',x):
    print 'False' 
elif re.search(r'CD[DM]',x):
    print 'False' 
###################################   
else:
    print 'True'
