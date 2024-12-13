# StepUp Job-Matching Platform

## Project Overview

The **StepUp Job-Matching Platform** is a Python-based application designed to address the challenges faced by unskilled and low-income workers in finding local job opportunities. The platform focuses on simplifying the job search process, making it easier for individuals to connect with job listings that match their skills and geographical location.

The system's core goal is to help unskilled workers find entry-level jobs in their area, thereby improving their access to stable employment opportunities and fostering economic independence. The platform is user-friendly and designed to cater to individuals with minimal technical skills, ensuring accessibility for everyone in the community.

### Features:
- **User-friendly interface**: Built using Tkinter, the platform provides an intuitive graphical interface.
- **Job Matching**: Jobs are dynamically matched to users based on their location and skills.
- **Location-based search**: Users can select their municipality to view relevant job listings.
- **Simple navigation**: The platform allows users to browse job listings, view details, and apply with ease.
- **Local Impact**: StepUp aims to bridge the gap between rural and urban job opportunities, particularly in underrepresented areas.

### Limitations:
- **Entry-Level Jobs Only**: Currently, the platform focuses on entry-level roles that require basic or no specialized skills.
- **Future Expansion**: Future updates may include specialized roles, training resources, and integration with real-time job listings.

---

## Python Concepts and Libraries

The **StepUp Job-Matching Platform** was developed using Python, and Tkinter was used for creating the graphical user interface (GUI). Below are the key concepts and libraries used in the project:

### Libraries:
- **Tkinter**: The primary library for creating the graphical user interface (GUI). It provides components like frames, labels, buttons, and input fields.
  
### Key Components:
- **Tkinter Widgets**:
  - `tk.Label`: Used for static text (titles, job descriptions).
  - `tk.Entry`: Used for user input fields like name, address, and phone number.
  - `tk.Button`: Buttons that trigger actions, such as navigating to different pages or applying for jobs.
  - `tk.OptionMenu`: Dropdown menu to select the municipality.
  - `tk.Frame`: Frames used to structure the layout of the GUI.
  
- **Event Handling**: 
  - Button commands use lambda functions (e.g., `command=lambda: go_to_jobs_page()`), and input validation ensures correct user input before progressing to the next page.

- **Dictionaries and Lists**:
  - **`job_dict`**: A dictionary where the key is the municipality name, and the value is a list of jobs available in that area.
  - **`municipalities`**: A list of available municipalities for dropdown selection.

- **Dynamic Content**: The UI updates dynamically based on user actions, such as changing job listings when a new municipality is selected.

- **Navigation**: The app has multiple pages (Home, Jobs Listing, Apply), and the content updates dynamically as the user interacts with it.

- **Error Handling**: **`messagebox.showerror()`** is used to display error messages when invalid input is detected.

---

## Sustainable Development Goals (SDGs)

This platform aligns with several United Nations Sustainable Development Goals (SDGs), particularly in promoting social and economic development in underserved communities:

### SDG 1: **No Poverty**
StepUp provides local, accessible job opportunities to individuals, offering a source of income and reducing poverty in low-income communities.

### SDG 8: **Decent Work and Economic Growth**
The platform aims to provide decent work by offering fair, entry-level jobs that contribute to economic growth. It helps users find stable employment opportunities close to home.

### SDG 10: **Reduced Inequality**
By offering job opportunities in both urban and rural municipalities, StepUp works to reduce the disparity in job availability between different areas, promoting equality.

### SDG 5: **Gender Equality**
Although not explicitly targeted, StepUp promotes gender equality by offering equal access to job opportunities for all users, regardless of gender.

### SDG 4: **Quality Education**
The platform helps users identify the skills required for various jobs and aims to integrate educational resources in the future to support job seekers in gaining the necessary qualifications.

### SDG 11: **Sustainable Cities and Communities**
By promoting local employment, StepUp contributes to building sustainable communities where people can work without having to relocate, reducing commuting and enhancing community stability.

### SDG 17: **Partnerships for the Goals**
In the long run, StepUp plans to form partnerships with local businesses, governments, and educational institutions to expand job opportunities and access to training.

---

## Program/Instructions for Running the Platform

Follow these steps to set up and run the StepUp Job-Matching Platform:

### 1. **Set Up the Environment**
   - Install Python 3.x on your computer.
   - Install Tkinter by running `pip install tk` if it’s not already included.

### 2. **Run the Program**
   - Download or clone the repository.
   - Navigate to the directory where the Python file is located.
   - Open a terminal/command prompt and run the Python script:
     ```
     python stepup_job_matching_platform.py
     ```
   - The platform will launch, and you will see the home page.

### 3. **Using the Platform**
   - **Home Page**: Enter your name, address, phone number, and age. Select your municipality from the dropdown menu.
   - **Jobs Page**: After clicking "PROCEED," the platform will display job listings for your selected municipality. You can click on job titles to view details.
   - **Apply Page**: After choosing a job, click "APPLY" to submit your application. You will be shown a confirmation page with the job details.

### 4. **Input Validation**
   - Ensure that all required fields are filled correctly before proceeding.
   - The platform will prompt you to fix any errors, such as missing information or incorrect phone numbers.

---

## Future Enhancements

- **Broader Job Listings**: Expanding to include specialized roles requiring advanced skills.
- **Training Resources**: Integrating resources for skill development to support users in qualifying for higher-level jobs.
- **Real-Time Data**: Linking the platform to real-time job listings and allowing employers to post jobs directly on the platform.

---

By connecting local job seekers with nearby opportunities, the StepUp Job-Matching Platform contributes to reducing unemployment and poverty while promoting sustainable, inclusive economic growth.
