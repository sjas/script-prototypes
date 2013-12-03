# source: http://itslennysfault.com/using-git-to-deploy-to-live-server-based-on-branch-aka-how-to-git-push-to-server
# use as a post-update hook in your git server

#determine the branch
BRANCH=`echo $1 | cut -d '/' -f 3`
#needed for "dumb servers" google if you need more explanation
git update-server-info
#check for null. If we don't have a branch name lets quit
if [[ -z "$BRANCH" ]]; then
    echo 'could not determine branch.'
    exit 1
fi

#if branch is master use the dev path
if [ "$BRANCH" == 'master' ]; then
    PUSH_PATH=/path/to/dev/server/doc/root
fi

#if branch is live use the live path
if [ "$BRANCH" == 'live' ]; then
    PUSH_PATH=/path/to/live/server/doc/root
fi

#check for null and make sure the path exists
# then execute a pull from that repository
if [[  -n "$PUSH_PATH"  &&  -d "$PUSH_PATH" ]]; then
    cd $PUSH_PATH
    unset GIT_DIR
    git --git-dir $PUSH_PATH/.git pull origin $BRANCH
else
    echo 'Push path for '$PUSH_PATH' not found'
fi3
