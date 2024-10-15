# visualization.py
import matplotlib.pyplot as plt
import pandas as pd

def generate_visualization(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data['mean_radius'], bins=30, alpha=0.7, color='blue')
    plt.title('Mean Radius Distribution')
    plt.xlabel('Mean Radius')
    plt.ylabel('Frequency')
    plt.savefig('static/mean_radius_distribution.png')
    plt.close()
