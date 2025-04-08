# AI Energy Dashboard (Python Only)

This is a simplified, fully Python-based version of an AI-driven energy forecast dashboard.

## Features

- Python-based model training using RandomForestRegressor
- Simple visualization of energy forecast vs actual consumption
- Data saved in CSV format, graphs generated with matplotlib
- Lightweight project structure for reproducibility

## Files

- `retrain_model.py`: Trains a RandomForest model and outputs predictions to CSV
- `energy_dashboard.py`: Plots actual vs predicted consumption using matplotlib
- `data/`: Folder where CSV prediction results are stored
- `models/`: Folder where trained model is saved

## How to Run

1. Install required packages:
   ```bash
   pip install pandas scikit-learn matplotlib joblib
   ```

2. Train the model and generate predictions:
   ```bash
   python retrain_model.py
   ```

3. View the graph:
   ```bash
   python energy_dashboard.py
   ```

## References

This project builds on the following research sources:

1. E. Carter (2023). "AI-Optimized Energy Storage Systems for High-Efficiency Renewable Energy Integration." Int. J. AI, Big Data, Comput. and Mgmt. Stud.
2. A. C. Șerban & M. D. Lytras (2020). "Artificial Intelligence for Smart Renewable Energy Sector in Europe." IEEE Access.
3. K. Ning (2021). "Data Driven Artificial Intelligence Techniques in Renewable Energy System." M.S. thesis, MIT.
4. R. Bhardwaj et al. (2024). "EMS for Sustainable Data Centers." E3S Web Conf.
5. A. Ermakov (2024). "Electricity Demand Growth for Data Centres and AI and Implications for Natural Gas-Fired Power Generation."
6. K. C. Sunkara & K. Narukulla (2025). "Power Consumption and Heat Dissipation in AI Data Centers: A Comparative Analysis." Int. J. Innov. Res. Sci. Eng. Technol.
7. O. Chidolue et al. (2024). "Green Data Centers: Sustainable Practices for Energy-Efficient IT Infrastructure." Eng. Sci. Technol. J.
8. R. Reddy (2024). "Sustainable Computing: A Comprehensive Review of Energy-Efficient Algorithms and Systems." TechRxiv preprint.

## Citation and License Notes

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

Referenced works are cited under fair academic use. No proprietary code or restricted content is included from the above sources. All credit belongs to their original authors and publishers.

## Author

Meltem Ener
