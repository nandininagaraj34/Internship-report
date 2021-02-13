# Internship-report
Quick loss recuperation is a significant issue. In- network routing problems will arise, when there is a quick setup of fast setting up of a new piece of network equipment and process failure, most of the routing problems caused by some configuration or design error, to come out of these routing problems fault tolerance is used. As it knows that the faster development of the Internet technologies the mechanism of fault tolerance is required to provide high opportunity and high accuracy in a system.In my project machine learning algorithms like Support vector machine (SVM) and K-nearest neighbour (K-NN)algorithms are used to faind out the failure and overcome this failure in a node.this method which is use to anlyze the failure of a node and reson of failure during the data transmission of a node.

What is Machine Learning?

Machine Learning is a branch of artificial intelligence (AI) focused on building applications that learn from data and improve their accuracy over time without being programmed to do. It is the process of simple learning or consuming knowledge, it helps to increase knowledge, makes the process efficiently and reduce the time consuming of the process also improves the process of automation machine learning has a different type of algorithm which differ in their input and Output sets of data intended to solve the problem. Classification, clustering techniques are a part of machine learning techniques to build machine learning models. machine- learning algorithm technique is used for traffic engineering for analysing the behaviour of the network state


 What You Mean by Fault Tolerance?
 
Fault tolerance refers to the ability of a system like computer, network, cloud, cluster, etc…...to continue operating without interruption when one or more of its components fail.Fault tolerance is a concept that widely used in computer to indicate that the system continues working in the existence of failures. It has gained more concern with the emergence of cloud computing. With the large-scale and dynamic environment in clouds, errors become more popular and the need for fault tolerance becomes a must. 

![](types%20of%20faulttolerance.png)

![](relationship%20digram%20of%20fault%20error%20failure.png)

Techniques are used 
Python and 
Overview of OMNeT ++
OMNeT++ is an extensible, modular, component-based C++ simulation library and framework, primarily for building network simulators. “Network” is meant in a broader sense that includes wired and wireless communication networks, on-chip networks, queueing networks, and so on. Domain-specific functionality such as support for sensor networks, wireless ad-hoc networks, Internet protocols, performance modeling, photonic networks, etc., is provided by model frameworks, developed as independent projects. OMNeT++ offers an Eclipse-based IDE, a graphical runtime environment, and a host of other tools
Components
The main ingredients of OMNeT++ are:

•	Simulation kernel library (C++)
•	The NED topology description language
•	Simulation IDE based on the Eclipse platform
•	Interactive simulation runtime GUI (Qtenv)
•	Command-line interface for simulation execution (Cmdenv)
•	Utilities (make file creation tool, etc.)

Our proposed system helps on identifying the fault tolerant node which are failed due to any particular faults and are recovered and process quickly. Here we using machine learning technique like SVM and KNN algorithms for detection and helps to recover the nodes. We energised the fault nodes and help in further failure avoidance and help it get going to further process.

![](dataflow%20digram.png)

steps involved

Stage 1: Raw Data: In this stage, the historical fault tolerance data is agitated from Kaggle or Getup and this historical data is utilized for the prediction of failure nodes.
Stage 2:The next step is Data Pre-processing: · the pre-processing step includes
*Data transformation: Normalization.
*Data cleaning: Fill in missing null values.
*Data integration: Integration of data files.
After the dataset is transformed into a pure dataset, the dataset is split into training and testing sets so as to evaluate. Here, the training values are taken as the more recent values. Testing data is kept as 5-10 percentage of the total dataset.
Stage 3:In stage 3 the user now inputs the relevant data where it is to find and resolve fault tolerance if it occurs it is known us test dataset.
Stage 4:Now in this we classify the uploaded data set according to the system needs using KNN algorithm and after it is ready for next step feature extraction. Initialise k value which we take from test dataset, from obtained k value we calculate distance and consider nearest neighbours and make the classification (class).
Stage 5:Feature Extraction: In this layer, only the features which are to be fed extracted. We will choose the feature from above classification process.
![](calculation%20of%20hybrid%201.png)
![](graphical%20representation%20of%20hybrid%201A.png)



















This work presents fault-tolerance in the scope of SDN. Also, we provided a simple background on fault-tolerance and related concepts to develop a complete understanding of the topic. Our goal was to identify SDN fault-tolerance requirements specific to the SDN architecture and discuss approaches that can be used to improve fault-tolerance in SDN. While exploring the topic of fault-tolerance in SDN, we have identified that each layer has its faults and fault-tolerance issues. In this implementation we first explore the relative node fault failure detection, which is an important issue for supporting dependability in distributed systems, and often is an important performance bottleneck in the event of node failure. Here, we analyses the failure detections, using machine learning technique and process the failure nodes in a better solution in terms of reliability and energy effectively. For the future enhancement we want to in addition increase energy of the sensor node further to the information flow to the bottom station with minimal relay nodes. This means that in order to achieve fault-tolerance different aspects and features are needed to be targeted, and no single-focused technology will be able to provide the reliability expected in commercial networks. SVM and K-means are effectively used to analyse the fault tolerance of network router using machine learning technique.





















































 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
