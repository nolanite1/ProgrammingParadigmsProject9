import sys
import operator
try:
    string1 = sys.argv[1]
    string2 = sys.argv[2]
except:
    print("Not enough arguments provided via the command line")
    sys.exit()
f = open(string1,'r')
contents = f.read()
contents = contents.lower()
erasures = ['\n','\t','.','?','!',',',';',':','\'','\"']
for x in range(0,len(erasures)):
    contents = contents.replace(erasures[x],' ')
list_of_text = contents.split(' ')
f.close()
while '' in list_of_text:
    list_of_text.remove('')
seperator = open(string2,'r')
seperators = seperator.read()
seperator_list = seperators.split(',')
for x in range(0,len(seperator_list)):
    while seperator_list[x] in list_of_text:
        list_of_text.remove(seperator_list[x])
dictionary = {}
for x in range(0,len(list_of_text)-1):
    if list_of_text[x]+" "+list_of_text[x+1] in dictionary:
        dictionary[list_of_text[x]+" "+list_of_text[x+1]]+=1
    else:
        dictionary[list_of_text[x]+" "+list_of_text[x+1]] = 1
sorted_dictionary = sorted(dictionary.items(),key=operator.itemgetter(1))
print("Story file name: " + string1)
print("Skip word file name: " + string2)
print("Skip words: " + str(seperator_list))
print("The five most frequently occuring word pairs are:")
for x in range(len(sorted_dictionary)-1,len(sorted_dictionary)-6,-1):
    print(sorted_dictionary[x])
