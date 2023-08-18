from nltk.sentiment.vader import SentimentIntensityAnalyzer
from qiskit import QuantumCircuit, transpile, Aer, assemble
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sid = SentimentIntensityAnalyzer()

def quantum_sentiment_analysis(text):
    backend = Aer.get_backend('statevector_simulator')
    circuit = QuantumCircuit(1, 1)
    theta = sum(ord(char) for char in text) % (2 * np.pi)
    circuit.h(0)
    circuit.rz(theta, 0)
    transpiled_circuit = transpile(circuit, backend)
    qobj = assemble(transpiled_circuit)
    result = backend.run(qobj).result()
    state_vector = result.get_statevector()

    quantum_score = np.abs(state_vector[0])**2

    return quantum_score

def combined_sentiment_analysis(text):
    vader_scores = sid.polarity_scores(text)
    vader_compound = vader_scores['compound']

    quantum_score = quantum_sentiment_analysis(text)

    combined_score = (0.7 * vader_compound) + (0.3 * quantum_score)
    return vader_compound, quantum_score, combined_score

def main():
    while True:
        user_input = input("Enter text: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        vader_compound, quantum_score, combined_score = combined_sentiment_analysis(user_input)
        
        if combined_score > 0:
            sentiment = "Positive"
        else:
            sentiment = "Negative"
        
        print("Sentiment:", sentiment)
        print("VADER Score:", vader_compound)
        print("Quantum Score:", quantum_score)
        print("Combined Score:", combined_score)

        positivity = combined_score  
        negativity = -combined_score  
        neutrality = 1 - np.abs(combined_score)  

        bloch_vectors = [
            [0, 0, positivity],  
            [0, 0, negativity],  
            [positivity, 0, 0],
        ]

        fig = plt.figure()
        for idx, vector in enumerate(bloch_vectors):
            ax = fig.add_subplot(1, 3, idx + 1, projection='3d')
            ax.scatter(vector[0], vector[1], vector[2], c='blue', s=50, label='Sentiment')
            ax.set_title(f"{['Positive', 'Negative', 'Neutral'][idx]} Sentiment")
            ax.set_xlabel('Positivity')
            ax.set_ylabel('Negativity')
            ax.set_zlabel('Neutrality')
            ax.set_xlim(-1, 1)
            ax.set_ylim(-1, 1)
            ax.set_zlim(-1, 1)
            ax.legend()

        plt.show()

if __name__ == "__main__":
    main()