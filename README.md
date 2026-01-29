
# Smart Hotel Pricing & Availability Automation


Smart Hotel Pricing & Availability is a system that automatically predicts room prices and availability based on demand and helps hotels make better pricing decisions.


## How It Works

Historical hotel data is stored in MySQL and used to train a machine learning model that predicts demand. This model is exposed through a Flask REST API, which is automatically called by n8n. Based on the predicted demand, decision logic checks whether the demand is high. If it is high, surge pricing is applied, available rooms are reduced, an email alert is sent, and all updated information is stored back in MySQL.



## Tech Stack

**Python (Machine Learning)**

**Flask (REST API)**

**Automation / Agentic AI** - N8N

**Database** - MySQL 

**Gmail API**(Google Cloud Console)




## Innovation

- Converts ML predictions into autonomous business actions.
- No manual intervention required.
- Real-time alert + pricing history tracking.


## Screenshots
(https://github.com/user-attachments/assets/637b462d-a3a3-46c0-a6ec-8d3dd0d9812f) #pricing_output
(https://github.com/user-attachments/assets/a9269e3a-468e-485b-9a11-86d3c15a1313) #daily_revenue


(https://github.com/user-attachments/assets/c4f60dc9-3a73-4b4c-8a7a-7aaf6484c4d3) #N8N Workflow
(https://github.com/user-attachments/assets/8127668a-74d0-4a67-b2fb-d1db9cc95711) #notification

## Demo

https://github.com/user-attachments/assets/6d2cb3a7-35a3-44c1-bda2-77c5bb770a70



## Conclusion

This project demonstrates Agentic AI by bridging prediction, decision-making, and execution.
