import json

with open("type_new.json",'r') as file:
    publications = json.load(file)
print(type(publications))

publications_modified=[]
 
def author_str(author_list):
    authors_name=[]
    for author in author_list:
        authors_name.append(author["name"].replace(",",""))
    return ", ".join(authors_name)
 
for publication in publications['papers']:    
    authors =publication['author']    
    publication['author']=author_str(authors)    
    journal =publication.get('journal','Not Found')
    if journal == 'Not Found':
        print("Its a conf.")
    else:
        publication['journal']=journal['name']
        publication['volume']=journal.get('volume',"00")
        publication['number']=journal.get('number', "00")
        publication['pages']=journal.get('pages', "00")
        #publication[]
    publications_modified.append(publication)
    
    
print(publications_modified)

with open("modified_pub.json", 'w') as file:
    json.dump(publications_modified,file) 
     
     
     
# for publication in publications['papers']:
#      authors =publication['author']
#      print(", ".join([author['name'].replace(",","") for author in authors]))

     
# output_file="student_course.json"
# with open(output_file, 'w') as file:
#     json.dump(,file, indent=2)