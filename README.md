**Web Server Log Analysis**
* Analyze web server logs to detect anomalies and gain insights using Python and PyCaret.

**📋 Overview**
* This project focuses on analyzing web server logs to identify patterns, anomalies, and critical insights. By leveraging machine learning, especially PyCaret, it provides a structured approach to process log data, visualize trends, and highlight deviations.

**⚙️ Key Features**
* Data Preparation: Parse and clean raw web server logs.

* Data Visualization: Generate comprehensive visual reports to understand traffic patterns.

* Anomaly Detection: Use PyCaret for detecting unusual patterns in logs.

* Kafka Integration: Incorporates Kafka for real-time data processing.

* MongoDB Storage: Efficiently store and retrieve logs for analysis.

**🛠️ Tech Stack**
* Programming Language: Python

* Libraries: PyCaret, Pandas, PySpark, Pymongo

* Visualization: Power BI, Matplotlib, Seaborn

* Data Pipelines: Apache Kafka

* Database: MongoDB

**📂 Project Structure**
* Data Preparation(Step 1).ipynb: Preprocessing raw log files.

* Algo(Model Creation)(Step 2).ipynb: Building and evaluating machine learning models.

* Kafka_producer(Step 3).ipynb: Producing logs to Kafka topics.

* Kafka_consumer_mongoDB_connection(Step 4).ipynb: Consuming logs and saving to MongoDB.

* Data Visualization(project).pbix: Interactive Power BI dashboard for analysis.

* Logs and Sample Data: Includes sample datasets like logs_df(ml).csv for testing and evaluation.

**🚀 How to Run**
* Clone this repository:
git clone https://github.com/AbhishekChavan31/web-server-log-analysis.git

* Install dependencies

* Start Kafka and MongoDB services.
  
* Execute notebooks in order:

* Data Preparation

* Model Training and Evaluation

* Kafka Producer & Consumer

* Use Data Visualization(project).pbix to visualize results.
📊 Sample Visualizations
The project offers interactive visualizations to explore:

* Traffic spikes and downtime. Unusual user-agent behaviors. Regional traffic patterns.
  
**🤝 Contributing**
* Contributions are welcome! Feel free to raise issues, suggest enhancements, or submit PRs.
