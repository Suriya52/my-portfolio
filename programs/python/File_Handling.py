# r for Read a file.
# w for write a file. 
# a append a file. 

# We can also work with character and Image also in this File formate.

# rb for read binary 
# wb for write binary for read or write picxel of the image, photo ect..

f = open('file','r')

#f1=open('file','a')

#f1.write("Adding...") Append is used to adding a line without loosing the previos line or statment. 
print(f.read())