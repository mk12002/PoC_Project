import pandas as pd
import numpy as np

num_samples = 10000

np.random.seed(42)

data = {
    "Num_Qubits_Sent": np.random.randint(500, 1500, num_samples),
    "Num_Qubits_Measured_Correctly": np.random.randint(400, 1500, num_samples),
    "QBER": np.random.uniform(0.01, 0.15, num_samples) + np.random.normal(0, 0.02, num_samples),  
    "Photon_Splitting_Prob": np.random.uniform(0, 0.5, num_samples),
    "Intercept_Resend_Prob": np.random.uniform(0, 0.5, num_samples),
    "Eavesdropper_Success_Rate": np.random.uniform(0, 1, num_samples),
    "Final_Key_Length": np.random.randint(100, 1200, num_samples),
    "Detector_Error_Rate": np.random.uniform(0.001, 0.05, num_samples),  
    "Quantum_Channel_Noise": np.random.uniform(0.01, 0.2, num_samples),  
}

attack_labels = np.random.choice(
    [0, 1], num_samples, 
    p=[0.65, 0.35]  
)

for i in range(num_samples):
    if attack_labels[i] == 1:
        if np.random.rand() < 0.5:  
            data["QBER"][i] += np.random.uniform(0.02, 0.08)
            data["Eavesdropper_Success_Rate"][i] += np.random.uniform(0.1, 0.4)
            data["Final_Key_Length"][i] -= np.random.randint(50, 300)
            data["Quantum_Channel_Noise"][i] += np.random.uniform(0.02, 0.07)
        else:  
            data["QBER"][i] += np.random.uniform(0.07, 0.12)
            data["Eavesdropper_Success_Rate"][i] += np.random.uniform(0.4, 0.8)
            data["Final_Key_Length"][i] -= np.random.randint(300, 700)
            data["Detector_Error_Rate"][i] += np.random.uniform(0.02, 0.04)
            data["Quantum_Channel_Noise"][i] += np.random.uniform(0.05, 0.1)

for key in data:
    data[key] = np.maximum(data[key], 0)

df_qkd = pd.DataFrame(data)
df_qkd["Attack_Detected"] = attack_labels

dataset_path = "qkd_attack_dataset_v3.csv"
df_qkd.to_csv(dataset_path, index=False)

print(f"Updated dataset saved to {dataset_path}")
