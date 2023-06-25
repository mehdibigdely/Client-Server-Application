# Client-Server-Application
## This is a simple client-server application developed using CRUD Python module, Dash, and MongoDB.
### My goal was to write a maintainable, readable and adaptable code on the CRUD (create, read, update, delete) Python module, and to acheive that, I did my best to implement following principles:
Principles in writing code:
Optimise for the reader of the code: carefully thought about the names for methods and classes, did not use abbreveations, and one level of abstraction should operate each method.
Don't repeat yourseif: used the CRUD Python methods in the entire application.
Do the smallest, simplest thing you can do to add some value.

# Client-Server-Application
## This is a simple client-server application developed using CRUD Python module, Dash, and MongoDB.
### My goal was to write a maintainable, readable and adaptable code on the CRUD (create, read, update, delete) Python module, and to achieve that, I did my best to implement following principles:
Principles in writing code:
Optimize for the reader of the code: carefully thought about the names for methods and classes, did not use abbreviations, and one level of abstraction should operate each method.
Don't repeat yourself: used the CRUD Python methods in the entire application.
Do the smallest, simplest thing you can do to add some value.

As a computer scientistic, I strived to deliver the results in a user-friendly dashboard that minimizes the user errors and drastically reduces training costs due to its simplicity. Also, following instructed database principles and optimizations resulted a very fast and responding application, that is scalable.

You may watch screencast of completed project in YouTube, using link below: 
https://youtu.be/IZN7A-nuNh0
I installed and used a local MongoDB and Jupyter server on my Mac to complete the project.

Grazioso Salvare specializes in identifying best dog candidates for search-and-rescue training in different scenarios to rescue humans or other animals and usually in life-threatening conditions. The main shelter will be around Austin, Texas. 
Based on Grazioso Salvare’s experience, specific types and breeds of dogs respond better to training in specific situations and the age of the dogs play an important role. 
Grazioso Salvare has a comprehensive data file and want to use existing data from the animal shelters to identify and categorize available and suitable dogs and is going to use a user-friendly dashboard to interact with and visualize data from a MongoDB database, with minimal user errors and training time. 
The data from animal shelters in Austin, TX are not structured and as there are many different animals such as cats, dogs, birds, and many more, MongoDB seemed to be the best tool to work with such a diverse and unstructured information.
ACID stands for Atomicity, Consistency, Isolation, and Durability. These properties focus on the consistency and reliability of the transaction done in the database. 
MongoDB is built on the principles of CAP Theorem which focuses on Consistency, Availability, and Partition. Unlike the ACID properties of SQL databases, CAP theorem focuses on availability of data in the case of MongoDB.
To conclude, SQL databases safeguard reliability of transactions whereas MongoDB ensures high availability of data; the unstructured nature of the data, in addition to the cost-effective benefits were the main reason to choose MongoDB over SQL.[1]

Dash which is an open-source framework and works with Python, R, F# and Julia is a great tool to create web-based analytic applications. There are many useful specialized or general open-source Dash libraries that are used for creation of domain-specific Dash components, web-applications or general local applications..[2]
For this project, Dash seemed to be a perfect fit and offered everything that client needed. Even Python data scientist that are not experts in web developments and coding can benefit from dash, due to its user-friendly interface, and the fact that it can be learned and implemented quickly. 
The project started with installation of the MongoDB on the local machine or server (Ubuntu or Linux based OS are the best, however MongoDB works on Windows and Mac as well).
The next step was importing the data into the MongoDB database using the CSV file (aac_shelter_outcomes.csv). That was completed using the MongoDB Shell, which is mongosh. Learning mongosh syntax helped to be able to write and implement CRUD (Create, Read, Update, Delete) methods using Python language which was an integral part of the project.

Dash enabled me to display the returned data from MongoDB in an elegant and user-friendly way, with least issues or errors on the user’s side. 

An example of the technical side of coding:
Below are the filtration requirements for the dashboard, and to achieve the proper results, the upcoming MongoDB queries were created, implemented and displayed on the dashboard:

if __name__ == '__main__':
    application.run(port=9000)

    # WR stands for water rescuer
    if radio_value == "WR":
        data = shelter.read({"animal_type": "Dog", "sex_upon_outcome": "Intact Female",
                             "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]},
                             "age_upon_outcome_in_weeks":{"$lt":156, "$gt":26}})
    # MoW stands for Mountain or Wilderness 
    elif radio_value == "MoW":
        data = shelter.read({"animal_type": "Dog", "sex_upon_outcome": "Intact Male",
                             "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
                             "age_upon_outcome_in_weeks":{"$lt":156, "$gt":26}})
    # DoIT stands for Mountain or Wilderness                         
    elif radio_value == "DoIT":
        data = shelter.read({"animal_type": "Dog", "sex_upon_outcome": "Intact Male",
                             "breed": {"$in": ["German Shepherd","Doberman Pinscher","Golden Retriever", "Bloodhound", "Rottweiler"]},
                             "age_upon_outcome_in_weeks":{"$lt":300, "$gt":20}})
    elif radio_value == "All":
        data = shelter.read({})



