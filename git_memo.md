
Creating dev branch: do this only once!
```
git branch dev
git checkout dev
git push -u origin dev
```
(to delete that branch: ```git branch -d dev```)

While in dev 

Commit, push & got to master branch & merge dev to master:
```
git commit -a -m "etc"
git push
git checkout master
git merge dev
```

Set the target version
```
./setver.bash major minor patch
```

See that everything works allright

Test packaging in virtualenv
```
./make_venv.bash
```

Commit & push master
```
git commit -a -m "etc"
git push
```

Push the version
```
./git_tag.bash
```

Linger in the master if you must

When back to dev, rewind it to current master
```
git checkout dev
git rebase master
```

