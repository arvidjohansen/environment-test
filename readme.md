

# UNIX / Linux / OSX

# Environment

## Listing all environment variables

`printenv`

```TERM_PROGRAM=Apple_Terminal
SHELL=/bin/bash
TERM=xterm-256color
HOME=/Users/arvidj
LOGNAME=arvidj
LC_CTYPE=UTF-8
_=/usr/bin/printenv
PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
...
```

## Modify environment before executing command
Use command `env` example:

```sh
./test1
```

>None


```sh
env fruit='apple' ./test1
```
>apple

## Set temporary environment variable
Will expire once the session is closed

`export name:value`

```sh
export fruit=pear
./test1.py
#pear
```

### Adding new value to existing environment variables

`export name=newvalue:$name`

```sh
export fruit=orange:$fruit
./test1.py
#orange:pear
```

## Adding a permanent environment variable


Simply add to previous commands to ~/.bash_profile

```sh
echo "export fruit=banana" >> ~/.bash_profile
```

## For all users

Simply add previous commands to file `etc/profile`

Or if your OS has following directory:
`/etc/profile.d`
all files within this directory will be sourced upon login


## Deleting a variable
```sh
unset fruit
```







# Path



## Viewing full path

`echo $PATH`

```
/Library/Frameworks/Python.framework/Versions/3.9/bin:
/usr/local/bin:
/usr/bin:
/bin:
/usr/sbin:
/sbin
```

## Locating a file in path


`which python`

```
/usr/bin/python
````

`which python3`

```
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
```








