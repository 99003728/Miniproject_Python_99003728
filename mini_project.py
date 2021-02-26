import re
smt=''
count=0
Search_key=input("Enter Search Key\n")
file_name=Search_key+'.txt'
write_file=open(file_name,'w')
read_file=open("Input.txt",'r')
read_file1=read_file.readlines()

for line in read_file1:
    smt+=line
new_str1=re.sub('\W', ' ', smt) 
new_str=re.sub(' +',' ',new_str1)
write_file1=open('abd.txt','w')
aa=" "
text_list=new_str.split(" ")
aa=aa.join(text_list)
write_file1.write(str(aa))
for x in range(len(text_list)):
    if re.fullmatch(Search_key,text_list[x],re.M | re.I):
        count+=1
        write_file.write(text_list[x-1]+' '+text_list[x]+' '+text_list[x+1]+'\n')
        
       
       

write_file.write('Total count of '+Search_key+' in input file is '+str(count))