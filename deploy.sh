#!/usr/bin/bash

#step1 clone git repo
read -p "Enter the git repo link:" git_repo_link
git clone $git_repo_link

#step2:change directory to the cloned repository
read -p "Enter the cloned repo name:" repo_name
cd $repo_name

# Step 3: Fetch Python version
python_version=$(cat Pipfile | grep python_version | cut -d '"' -f 2)

echo "$python_version"
# Step 4: Check if Python version is installed
if python$python_version --version &> /dev/null; then
    echo "Python $python_version is already installed"
else
# Step 5: Install the Python version
    echo "Python $python_version is not installed. Installing..."
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update 
    sudo apt-get upgrade
    sudo apt-get install python$python_version
    sudo apt-get install python$python_version-distutils
fi

# Step 6: Install pip3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python$python_version get-pip.py

# Step 7: Install pipenv
python$python_version -m pip install pipenv

which_python=$(which python$python_version)
echo "$which_python"

# Step 8: Activate pipenv shell
pipenv --python=$which_python

# Step 9: Install all dependencies
pipenv install

# Step 10: Check Django project
check=$(pipenv run python  manage.py check)

# Step 11: If Django check is successful, migrate the database
if [[ $check == "system check identified no issues" ]]; then
    pipenv run python manage.py migrate
fi

# Step 12: Create launch.sh script
echo "#!/usr/bin/bash" > launch.sh
echo "pipenv run python manage.py runserver 0.0.0.0:8000" >> launch.sh
chmod +x launch.sh

