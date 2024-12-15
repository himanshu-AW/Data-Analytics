import pickle

# pickling 
data = {"id":12,"name":"Ram","age":20}
with open("C:/Users/himan/OneDrive/Desktop/Python/File_Handling/data.pkl","wb") as file:
    # pickle.dump(data, file)
    bin_data=pickle.dumps(data,file)
    print(bin_data)

# json is ideal for data change in b/w systems and lanuguage.
# pickle is best for python specific data structure that need to be preserved exectly.

# difference b/w pickle and json
# 1: Portable: json is more portable rather then pickle.
# 2: Speed: pickle is more faster than json
# 3: Security: pickle is less secure(potential for melicious injection) than json
# 4: complexity: pickle can handle complex data structures with it and json can handle normal data structures.
