# update-branch.sh
git stash
git checkout main &&
git pull origin main &&
git checkout "$1" &&
git merge main --no-edit
git stash pop