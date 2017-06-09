import argparse,random

def LRU(records):
    #print "LRU"
    freqList = []
    print "rr-> ",records
    for key,val in records.items():
        rid, subjects , marks , freq , newLine = map(str,val.split('|'))
        freqList.append([freq,rid])
    return min(freqList[1]),freqList
    

def create(records):
    #print "create"
    no_of_lines = len(records)
    fileFull = False
    if no_of_lines == 20:
        fileFull = True

    rid = random.randrange(1, 100, 2)
    while rid in records.keys():
        rid = random.randrange(1, 20, 2)

    if fileFull:
        record_id,freqList = LRU(records) #freqList is not used here.
        deleted = delete(records,record_id)
        
    subjects , marks , freq , newLine= "English,Hindi,Maths" , "53,45,90" , 1 ,"\r\n"
    records[str(rid)]='|'.join([str(rid),subjects,marks,str(freq),newLine])

def delete(records,record_id):
    #print "Delete"
    del records[record_id]
    return record_id

def update(records,record_id):
    #print "Update"
    rid, subjects , marks , freq, newLine = map(str,records[record_id].split('|'))
    freq = str(int(freq)+1)
    subjectlist = list(map(str,subjects.split(',')))
    marklist = list(map(str,marks.split(',')))
    print "Updating mark of subject",subjectlist[0],"to",int(marklist[0])+1
    marklist[0] = str(int(marklist[0])+1)
    marks = ','.join(marklist)
    records[rid]='|'.join([rid,subjects,marks,freq,newLine])

    

def retrieve(records,record_id):
    #print "retrieve one"
    rid, subjects , marks , freq , newLine = map(str,records[record_id].split('|'))
    freq = str(int(freq)+1)
    records[rid]='|'.join([rid,subjects,marks,freq,newLine])


'''
def retrieve_all(records):
    print "retrieve all"
    for key,val in records.items():
            print val
'''


def write_back_records(records):
    header = 'ID|Subjects|Marks|Freq|\r\n'
    lru , freqList = LRU(records)
    freqList = sorted(freqList)
    with open("records.txt", "wb") as text_file:
        text_file.write(header)
        for record_id in freqList:
            text_file.write(records[record_id[1]])
        text_file.close()
            
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='LRU Cache System')
    #parser.add_argument('-retrieveall', type=str, help="use 'retrieveall' Get all the cached records")
    parser.add_argument('-create',type=str,  help="use 'create' Get all the cached records")
    parser.add_argument('-retrieve', nargs='*' ,type=str, help="use 'retrieve record_id' Get all the cached records")
    parser.add_argument('-update', nargs='*' ,type=str, help="use 'update record_id' Get all the cached records")
    parser.add_argument('-delete', nargs='*' ,type=str, help="use 'delete record_id' Get all the cached records")
    args = parser.parse_args()
    #print args.retrieve

    record_file =  open("records.txt",'rb') #Opening the file in read mode to read the records from the file
    #with open("records.txt", "r+") as record_file:
    print args
    
    records = {}
    for line in record_file:
        rid, subjects , marks , freq , newLine = map(str,line.split('|'))
        if rid == 'ID':
                continue
        records[rid]='|'.join([rid,subjects,marks,freq,newLine])
    record_file.close()

    '''
    if args.retrieveall: #Retrieve all
        retrieve_all(records)
    '''

    if args.retrieve:    #Retrieve one
        record_id  = args.retrieve[0]
        retrieve(records,record_id)
        #print "rid-> ",records[record_id]

    if args.update:      #Update the marks
        record_id  = args.update[0]
        update(records,record_id)
        #print "rid-> ",records[record_id]

    if args.create:      #Create a record
        create(records)
        #print records.keys

    if args.delete:      #Delete a record
        record_id  = args.delete[0]
        delete(records,record_id)
        #print records

    #print "records",records
    write_back_records(records) #For writing back the updated , created , deleted , retieved records in the file records.txt
        
