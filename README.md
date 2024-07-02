### Step-by-Step Guide to Running the OpenStack Interaction Script

#### Prerequisites

1. **Python Installation** :

* Ensure Python 3.10 or higher is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

1. **Python Packages** :

* Install the necessary Python packages (`python-openstackclient` and `openstacksdk`):
  * Use `pip` to install:
  * pip install python-openstackclient openstacksdk
* 

1. **Access to OpenStack** :

* Obtain the following authentication details from your OpenStack environment:
  * `auth_url`: URL for the OpenStack authentication endpoint (e.g., `https://openstack.example.com/v3`).
  * `username`: Your OpenStack username.
  * `password`: Your OpenStack password.
  * `project_name`: Name of your OpenStack project.

#### Setup

4. **Clone the Repository** (Optional):
   * If you have the script already, skip this step.
5. **Create Configuration File** :

* Create a file named `openstack.yaml` in the same directory as `main.py`.
* Open `openstack.yaml` and paste the following configuration template, replacing placeholders with your actual OpenStack authentication details:

clouds:
  myopenstack:
    auth:
      auth_url: https://openstack.example.com/v3
      username: your_username
      password: your_password
      project_name: your_project_name
    region_name: RegionOne



4. * * Replace `auth_url`, `username`, `password`, and `project_name` with your actual OpenStack authentication details.

#### Running the Script

6. **Execute the Script** :

* Run the Python script `main.py`:
