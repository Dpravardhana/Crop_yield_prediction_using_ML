import pickle

# Load the pickle file
with open('model.pkl', 'rb') as file:
    data = pickle.load(file)

# Print the contents
print(data)
