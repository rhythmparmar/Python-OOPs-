import pickle

str="This is my first line. This is second line."
with open("myfile.info","wb")as fh:
    pickle.dump(str,fh)
print("File Successfully created.")
