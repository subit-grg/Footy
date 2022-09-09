Objective:

We were required to create a service-orientated architecture for our application, this application composes of at 4 services that work together.

Service 1:

This service will interact with my application, which will also be responsible for communicating with other 3 services.

Service 2 and 3:

There services will generate a random “Object”, which will be passed on to service 4.

Service 4:

This service will also create an “Object”, depending on the results of service 2 and 3, with some pre-defined rules.


Project approach:

Initially, a risk assessment was created with some pre-defined colour codes as per image below:

![image](https://user-images.githubusercontent.com/108797865/189161639-bb93fc99-8111-43ad-8c02-9fd6adca8261.png)

Risk Assessment:

<img width="883" alt="image" src="https://user-images.githubusercontent.com/108797865/189161992-3f5352aa-2018-4727-80b3-ca7495557188.png">

Following Trello board was created to keep track of tasks required to do:

<img width="844" alt="image" src="https://user-images.githubusercontent.com/108797865/189163811-5c4a8764-c13a-4839-a29e-3322428ac12a.png">


Application Services idea:

Service 1 (front-end):

This service will interact with the app and display a webpage. When refreshed, the app will make number of HTTP requests to services 2,3&4. GET request wil be sent to services 2 &3, which will further send a POST request to service 4.

Service 2 (stadium -s2):

Once GET request is made, it randomly selects a stadiu, using choice method.

Service 3 (condition-s3):

Similaryly to service 2, it will using choice method to select condition.

Service 4 (opp-s4):

Upon receiving the responses from service 2 and 3, it will select an opposition, using POST request. Then, it interacts with service 1(front-end) service.

Examples:

![image](https://user-images.githubusercontent.com/108797865/189165597-dbc4a802-b039-4771-a3ca-6399204126b9.png)

After clicking refresh:

![image](https://user-images.githubusercontent.com/108797865/189165679-0040a729-0d52-4703-b2d5-ccdb74a955d8.png)

Development approach:

<img width="647" alt="image" src="https://user-images.githubusercontent.com/108797865/189167244-c05ca41c-9eed-4709-b30b-d4edb6567cbf.png">



Coding filing structure:

![image](https://user-images.githubusercontent.com/108797865/189167458-c2419dfa-cbd6-4b67-96d3-83afafdfc5a2.png)

![image](https://user-images.githubusercontent.com/108797865/189167561-1edc4bf8-f03d-4002-ab93-f597f1484ad8.png)


CI Pipeline and Deployment (Jenkins):

![image](https://user-images.githubusercontent.com/108797865/189167713-658c7a9f-cad2-4522-b61a-d692f547d302.png)


Testing results (Examples):

1.

![image](https://user-images.githubusercontent.com/108797865/189167808-25955dd1-585a-41db-a22a-ae74a87d6e83.png)

2.

![image](https://user-images.githubusercontent.com/108797865/189167990-28931ae3-51cd-4b9c-8346-aff0a4b91398.png)


Further Development:

Due to time constraint and unexpected tasks, I was not able to implement Docker Swarm and Ansible. For my next project, I am more aware of the time required for each tasks and will be in a better position to manage my time and implement docker swarm and ansible.











