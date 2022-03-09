



print(len("                 \"utterance\":"))

print(len("\"participant_0 :"))

print("abcdef"[2:-1])
save = []
with open("twenty_ex_finetuned.txt", 'r') as f:
    nl = "" 
    idd = ""
    for line in f:
        #print(type(line))
        if "example-id" in line:
            print("")
            print(idd)
            save.append(idd)
            idd = line
            #print(line)
            if len(nl) > 10:
                print(nl)
                save.append(nl[1:])
                nl = ""
            #print("")
            #line = ""
        if "participant" in line:
            if len(line) > 47 and line[47] == "\"":
                #print(line[47:-2])
                nl = nl + " " +  line[47:-2]
            else:
                #print(line[46:-2])
                nl = nl + line[46:-2]
        else:
            if len(line) > 47 and line[47] == "\"":
                #print(line[30:-2])
                nl = nl + line[30:-2]
            else:
                #print(line[29:-2])
                nl = nl + line[29:-2]
        #if "utterance" in line:
        #    hello = line.replace('\n', "")
        #    hello = line.strip('\"utterance\":')
        #    convo = convo + hello 
        pass

with open("twenty_test.txt", "w") as q:
    for line in save:
        q.write("\n\n\n")
        q.write(line)
#print(save) 
    
    #print(convos_l[1])    
    #print(len(convos_l))
    

