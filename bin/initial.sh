# Initial setup of the environment

echo "This performs the initial setup of an environment for a Juice Django server."
echo "This should be run from the git cloned directory"
echo

read -n1 -p "Are you sure? (y/n) "
echo
if [[ $REPLY = [yY] ]]; then
    virtualenv env --no-site-packages
    source ./env/bin/activate
    mkdir -p database
    pip install -r ./setup/requirements/production.txt
    pip install -r ./setup/requirements/development.txt
fi
