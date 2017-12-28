import os
import datetime
time = str(datetime.datetime.now())
time = '_' + time[:10].replace('-','_')
confirmation = 'Your AR regen file has been created under "C:\python27\"'

##Get brokerage file #'s
with open('ARfile.txt') as arfile:
    with open('department.txt', 'w') as dep:

        bfiles = arfile.readlines()
        
##Get department #'s from brokerage file #'s
        for f in range(len(bfiles)):
            department = bfiles[f]
            department = department[:2]
            dep.write('0' + department + '\n')
        dep.close()
        
 ##Create file to generate output       
        with open('ARfile.txt', 'r') as finfiles:
            with open('department.txt', 'r') as departmentfile:
                with open(str('AR_regen' + time + '.txt'), 'w') as script:
                    ffiles = finfiles.readlines()
                    dfiles = departmentfile.readlines()
                    
##Optional variables for SQL script - AR Process
                    functionstart = str("INSERT INTO [ITSMain2].[dbo].[ITSWEB_SCHEDULE_TASK] ([USER_NAME],[DB_NAME],[TASK_TYPE],[PROCESS_TYPE],[DEPTNO],[INVNO],[IN_PROCESS]) values( 'ITS-AlKoh', 'bdp', 'XML-OUTBOUND', 'AR_INV', '")
                    functionend = str("' ,0 )")
                    
##Contatenate all values together & write data to file
                    for i in range(len(ffiles)):
                        line = functionstart + dfiles[i].strip() + "', '" + ffiles[i].strip() + functionend + '\n'
                        script.write(line)
##Clean up
                    departmentfile.close()
                    os.remove('department.txt')
                    
                    print(confirmation)
                    

    
    
