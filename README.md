# DynamoPyAPI Serverless Application

## Application Overview

* A user-friendly web interface has been developed and hosted on Amazon S3. This interface enhances user interaction and provides a visually appealing experience.
* Python is the primary language used for developing Lambda functions. AWS Lambda functions were created to perform discrete units of work within the application. It serve as the core processing units of the application.
* CloudFront is used as a content delivery network (CDN) for the S3-hosted web application. It accelerates the delivery of content to users across the globe, improving performance and reducing latency.
* The RESTful API was designed following REST principles, using HTTP methods like GET, POST, PATCH, and DELETE. API Gateway was configured to manage API requests.
* DynamoDB tables were created to store different types of data used by the application.
* CloudWatch Logs was used to collect comprehensive application logs, such as request/response data and error logs.
