# From Code to Care: Building ER Insights from Scratch

## Project Objectives

This project creates a comprehensive Emergency Room dataset from scratch using Python to simulate realistic healthcare operations over 24 months. The objective is to generate authentic patient demographics, admission patterns, wait times, and operational metrics that mirror real-world ER scenarios. The synthetic dataset feeds into a Power BI dashboard providing actionable insights on patient flow, resource utilization, satisfaction scores, and demographic distributions.

The analysis tracks **9,217 patient visits** with key performance indicators including average wait times (34.6 minutes), patient satisfaction scores (4.98/5), and admission rates (70%). The dashboard visualizes patient patterns by age groups, gender distribution, department referrals, racial demographics, and hourly admission trends to support healthcare decision-making and operational optimization.

##  Dashboard Highlights

### Key Metrics (1/2/2023 - 12/4/2025)
- **Total Patients**: 9,217
- **Average Wait Time**: 34.6 minutes
- **Patient Satisfaction**: 4.98/5 stars
- **Admission Rate**: 70% admitted, 30% not admitted

### Analytics Features
- **Patient Flow Analysis**: Hourly and daily admission patterns
- **Demographics Breakdown**: Age groups, gender (56% female, 44% male), racial distribution
- **Department Referrals**: Multi-specialty referral tracking
- **Satisfaction Monitoring**: Patient experience metrics
- **Operational Efficiency**: Wait time analysis and capacity utilization

##  Technical Implementation

### Data Generation Stack
```python
# Core libraries for dataset creation
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker
```

### Generated Dataset Features
- **Patient Demographics**: Age, gender, race, insurance information
- **Clinical Data**: Admission status, department referrals, satisfaction scores
- **Temporal Patterns**: 24-month timeline with realistic seasonal variations
- **Operational Metrics**: Wait times, hourly admission patterns, capacity data

### Visualization
- **Power BI Dashboard**: Interactive charts and KPI monitoring
- **Real-time Insights**: Dynamic filtering and drill-down capabilities
- **Business Intelligence**: Executive summary views and operational dashboards

## Key Insights

- **Peak Hours**: Highest patient volume during midweek periods
- **Demographics**: Balanced gender distribution with diverse age representation
- **Satisfaction**: High patient satisfaction (4.98/5) indicates quality care delivery
- **Efficiency**: 34.6-minute average wait time shows operational effectiveness
- **Department Utilization**: Comprehensive referral patterns across medical specialties

## Getting Started

### Prerequisites
```bash
Python 3.8+
pandas
numpy
faker
datetime
```

### Usage
```bash
# Clone repository
git clone https://github.com/yourusername/er-insights-from-scratch.git

# Run data generation
python generate_er_data.py

# Open Power BI file for dashboard
QuickCare_ER_Dashboard.pbix
```

## Project Structure

```
er-dashboard-project/
│
├── african_patient_dataa.csv              # Generated synthetic dataset
├── healthcare_datasets.py         # Python data generation script
├── QuickCare_ER_Dashboard.pbix # Power BI dashboard file
└── README.md                   # Project documentation
```

## Business Applications

- **Hospital Administration**: Resource planning and capacity management
- **Healthcare Analytics**: Patient flow optimization and performance monitoring
- **Quality Improvement**: Satisfaction tracking and operational efficiency
- **Strategic Planning**: Data-driven decision making for ER operations

## Future Enhancements

- Real-time data streaming integration
- Predictive analytics for patient volume forecasting
- Advanced statistical modeling
- Integration with hospital management systems

## About

Created by Sarah Iniobong Uko demonstrating:
- Synthetic data generation with Python
- Healthcare domain knowledge
- Business intelligence visualization
- End-to-end data science project management

---

*This project showcases the complete journey from data creation to business insights, highlighting both technical skills and healthcare analytics expertise.*
