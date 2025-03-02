# Security in Quantum Computing - BB84 Algorithm

## Team Members
- [Mohit Kumar](mailto:mohit.kumar2022b@vitstudent.ac.in)
- [Teresa Sara Saji](mailto:teresasara.saji2022@vitstudent.ac.in)
- [Sainy Mishra](mailto:sainy.mishra2022@vitstudent.ac.in)

## Introduction
This project explores the implementation and security aspects of the BB84 quantum key distribution (QKD) protocol. BB84, proposed by Charles Bennett and Gilles Brassard in 1984, enables two parties (Alice and Bob) to securely share a cryptographic key while detecting potential eavesdroppers (Eve). The protocol leverages quantum mechanics principles such as Heisenberg's uncertainty principle and the no-cloning theorem to ensure secure communication.

## BB84 Protocol Overview
The BB84 protocol consists of five main steps:
1. **Alice Sends Qubits**: Alice generates a random sequence of bits and encodes them into photons using rectilinear (+) or diagonal (×) bases.
2. **Bob Measures the Qubits**: Bob randomly selects bases to measure the received qubits, causing some errors due to mismatches.
3. **Basis Reconciliation**: Alice and Bob publicly compare their bases and discard mismatched measurements.
4. **Error Detection**: Alice and Bob reveal a subset of their keys to check for discrepancies caused by potential eavesdroppers.
5. **Key Distillation and Encryption**: Error correction and privacy amplification techniques are applied to obtain a secure key, which can then be used in classical encryption methods such as AES or OTP.

## Implementation Details
This project includes:
- **Simulation of BB84 Protocol**: Implementing the key distribution steps in Python using quantum computing libraries.
- **Security Analysis**: Evaluating the protocol's resistance to eavesdropping using Quantum Bit Error Rate (QBER) detection.
- **Machine Learning-based QKD Attack Detection**: Developing models to detect potential attacks using various classifiers.

### Quantum Key Distribution (QKD) Attack Detection
To enhance security, we employ machine learning techniques to detect potential attacks on QKD systems. Three models are explored:
1. **Neural Network (NN)**
   - Input Layer: QKD parameters
   - Hidden Layers: 64 and 32 neurons (ReLU activation)
   - Output Layer: Sigmoid activation (binary classification)
   - Training: Adam optimizer, Binary Cross-Entropy Loss
   
2. **Random Forest (RF)**
   - Base Model: Random Forest Classifier
   - Number of Trees: 100
   - Hyperparameter tuning via GridSearchCV
   
3. **XGBoost (XGB)**
   - Base Model: XGBoost Classifier
   - Tuned Parameters: n_estimators, learning_rate, max_depth, subsample, etc.
   - Training: 80% train, 20% test split, cross-validation

### Dataset
The dataset for training and evaluation consists of 10,000 samples, representing both normal operations and attack scenarios (35% attacks). Key parameters include:
- Number of qubits sent and measured correctly
- QBER (Quantum Bit Error Rate)
- Probability of photon splitting and intercept-resend attacks
- Final key length and detector error rate

## Benefits of BB84 Protocol
- **Quantum Security**: Secure against classical and quantum computing attacks.
- **Eavesdropping Detection**: Attempts to intercept qubits introduce detectable errors.
- **Unconditional Security**: Theoretically unbreakable when implemented correctly.
- **Compatibility**: The final key can be used with classical encryption methods.

## Challenges & Future Work
### Limitations:
- **Data Imbalance**: 35% attack cases may not reflect real-world scenarios.
- **Feature Dependency**: The models rely on predefined QKD parameters.
- **Computational Overhead**: NN and XGB models require significant resources.

### Future Enhancements:
- Implement an additional encryption layer before basis comparison.
- Explore advanced ML models like transformers for improved anomaly detection.
- Apply reinforcement learning for real-time attack adaptation.
- Investigate federated learning for distributed QKD security.
- Test real-world implementations using physical QKD systems.

## How to Run the Project

Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository>
   ```

## Conclusion
This project demonstrates the security of the BB84 protocol and the effectiveness of machine learning-based attack detection mechanisms. By integrating advanced quantum and AI techniques, we aim to improve the robustness of quantum key distribution systems.
