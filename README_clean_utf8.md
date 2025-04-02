# AI-Driven Energy Dashboard for Data Center Efficiency

This repository contains a prototype system for forecasting and visualizing data center energy consumption using machine learning and sustainability metrics. The project was developed as part of the ACM 498 Graduation Thesis titled:
"AI-Driven Energy Management Systems for Data Centers: Integration of Renewable Energy for Sustainable Digital Infrastructure"
by Meltem Ener.

## Overview

As data centers become increasingly energy-intensive, this project explores how artificial intelligence can be applied to optimize energy demand forecasting and monitor the integration of renewable sources. The dashboard simulates the behavior of a smart Energy Management System (EMS), providing both forecasting capabilities and sustainability insights such as carbon offset and renewable energy share.

## Features

- Machine learning model (Random Forest) for hourly energy consumption forecasting
- Simulation of live model retraining and prediction updates
- Interactive dashboard built with React for real-time visualization
- Calculations for renewable energy contribution and estimated carbon savings

## Project Structure

```
ai-energy-dashboard/
├── backend/                    # Model retraining logic and scripts
├── dashboard/                  # React frontend components
├── data/                       # Input datasets and model predictions
├── models/                     # Folder for storing trained models
├── notebooks/                  # Jupyter notebooks for experimentation
├── README.md                   # Project documentation
└── .gitignore
```

## Setup Instructions

### Backend (Model Training)

```bash
cd backend
pip install -r requirements.txt
python retrain_model.py
```

This script retrains the model on available data, simulates new hourly entries, and writes updated predictions to `data/energy_predictions_updated.csv`.

### Frontend (Dashboard)

```bash
cd dashboard
npm install
npm run dev
```

The dashboard reads predictions from CSV and automatically refreshes every 30 seconds.

## Data Sources

- `Energy_consumption.csv`: Main dataset with features like timestamp, temperature, humidity, HVAC, lighting, occupancy, and energy use
- `measure_name_crosswalk.csv`: Maps building upgrade measures to metadata
- `energy_predictions_updated.csv`: Machine learning model output

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

## License and Citation Notes

This project is released under the MIT License (see below). It references publicly available academic sources and uses them strictly for educational and research purposes under fair use.

The original copyrights and licenses of referenced works:
- IEEE Access, E3S Web Conf., MIT Thesis, TechRxiv preprints, and other journals retain full rights.
- No proprietary code or licensed material was reused from these sources.
- All citations are for academic alignment only.

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.
