import pickle

# Zapisanie wartości 1 do pliku request_counter.pkl
with open("request_counter.pkl", "rb") as file:
    requests_counter = pickle.load(file)

print(requests_counter)
