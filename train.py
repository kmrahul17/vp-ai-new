from sklearn.ensemble import RandomForestRegressor
import numpy as np
import joblib
import os

def generate_training_data():
    vehicles = {
        0: {'base_emission': 1000, 'efficiency': 0.7},  # Space Shuttle
        1: {'base_emission': 500, 'efficiency': 0.8},   # Space Taxi
        2: {'base_emission': 250, 'efficiency': 0.9}    # Space Pod
    }
    
    X = []
    y = []
    for _ in range(1000):
        distance = np.random.uniform(400, 225000000)
        vehicle_type = np.random.choice([0, 1, 2])
        passengers = np.random.randint(1, 20)
        X.append([distance, vehicle_type, passengers])
        vehicle = vehicles[vehicle_type]
        emission = (distance * vehicle['base_emission'] * (1 - vehicle['efficiency']) * 
                   (1 + passengers * 0.1))  # Emission in tons
        y.append(emission)
    
    return np.array(X), np.array(y)

if __name__ == "__main__":
    X, y = generate_training_data()
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, 'model.pkl'))