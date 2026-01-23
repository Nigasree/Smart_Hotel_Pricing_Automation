
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




(https://github.com/user-attachments/assets/637b462d-a3a3-46c0-a6ec-8d3dd0d9812f)

(https://github.com/user-attachments/assets/c4f60dc9-3a73-4b4c-8a7a-7aaf6484c4d3)

(https://github.com/user-attachments/assets/08c42978-0a51-45ca-b222-48227c020d9a)
## Demo

https://github.com/user-attachments/assets/f56a0976-97f0-4a9f-b70f-6916e5832684


## Conclusion

This project demonstrates Agentic AI by bridging prediction, decision-making, and execution.