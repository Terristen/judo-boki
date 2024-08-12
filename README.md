# **Judo Boki \- A Judo Club Bookkeeping Application**

## **Overview**

**Judo Boki** is a browser-based application designed for touch-screen use as a kiosk in a judo or other martial arts studio. It manages attendance recording for each session and tracks student information, including their name, age, rank, and progress in learning various techniques. The application is built to assist instructors and students in making informed decisions regarding testing and promotions.

## **Core Mission Objectives**

* **Efficiency:** Streamline the process of attendance tracking and student progress monitoring.  
* **Simplicity:** Provide an intuitive interface that can be easily used by instructors and students, with minimal training required.  
* **Flexibility:** Accommodate the complex and hierarchical nature of judo techniques, allowing for multiple categories and overlapping classifications.  
* **Data Security:** Ensure that no Personally Identifiable Information (PII) is stored, with all data being anonymized where possible.

## **Driving Principles**

* **User-Centric Design:** Prioritize ease of use, ensuring the application is accessible to users of all technical skill levels.  
* **Maintainability:** Use modern frameworks and tools that ensure the application can be easily updated and maintained.  
* **Modularity:** Build the application in a way that allows for future expansion or integration with other systems.

## **Feature List**

* **Attendance Recording:** Track attendance for each session, with options for automatic reminders and follow-ups.  
* **Student Information Management:** Manage and display basic student info (name, age, rank, etc.).  
* **Technique Tracking:** Log techniques covered in sessions, including categories like `tachi-waza` and `ne-waza`, and track student proficiency.  
* **Tagging System:** Implement a robust tagging system to handle the complex hierarchy and overlapping nature of judo techniques.  
* **Role-Based Access:** Secure access with role-based authentication and authorization, ensuring instructors and students have appropriate permissions.

## **Architecture Overview**

### **1\. User Experience (UX)**

* **Frontend:** The application frontend will be built using the **Quasar Framework**, leveraging Vue.js for reactive, component-based design. Quasar’s built-in components and responsive design capabilities will ensure that the application works seamlessly on touch-screen kiosks and other devices.  
* **Design:** The UI will adhere to Material Design principles, ensuring a clean, modern look and feel. Emphasis will be placed on simplicity and ease of navigation.

### **2\. Middleware**

* **Framework:** The middleware will be developed using **FastAPI**, chosen for its performance, scalability, and ease of integration with modern asynchronous programming patterns. FastAPI will handle all server-side logic, including API endpoints for data management and session handling.  
* **Session Management:** FastAPI will manage user sessions, with JWT (JSON Web Tokens) used for securing API requests. Session data will be stored temporarily and associated with role-based access controls.

### **3\. Authentication & Authorization**

* **Authentication:** Users will authenticate via JWT tokens, with OAuth2 mechanisms for generating and validating tokens.  
* **Authorization:** Role-based access controls (RBAC) will be implemented, ensuring that different users (e.g., instructors, students, administrators) have access to appropriate features and data.

### **4\. Data Layer**

* **Database:** **ArangoDB** will serve as the database layer, leveraging its multi-model capabilities to handle both graph and document-based data. ArangoDB will be dockerized for easy deployment and management.  
  * **Graph Model:** Used to represent the complex relationships between judo techniques, allowing for multi-parent categories and flexible querying.  
  * **Document Model:** Used for storing student records, session data, and other entities.  
* **Data Seeding:** The database will be seeded with initial data, including the structure of techniques, student information, and session templates. Seeding scripts will be integrated into the Docker setup for ease of deployment.  
* **Backup & Recovery:** Data will be backed up using Docker volumes, with regular backups scheduled and offloaded to long-term storage as necessary.

### **5\. Deployment**

* **Containerization:** The entire stack (FastAPI middleware and ArangoDB database) will be containerized using Docker and managed with Docker Compose. This allows for easy deployment on local machines or cloud environments.  
* **Cloud Readiness:** While designed for local deployment, the application will be cloud-ready, with options for scaling and integration with cloud services if needed in the future.

## **Development and Maintenance**

* **Version Control:** All source code will be managed in a Git repository, with continuous integration (CI) pipelines set up to automate testing and deployment processes.  
* **Documentation:** Comprehensive documentation will be maintained, including API documentation generated automatically via FastAPI, and detailed usage instructions for developers and end-users.  
* **Testing:** The application will include unit and integration tests to ensure reliability and stability. Tests will be run automatically in CI pipelines.

