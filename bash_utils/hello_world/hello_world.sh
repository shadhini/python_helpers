############
# SHE BANG
############
#** specify the path to the interpreter  (or program) that should be used to run (or interpret)
#** the rest of the lines in the text file.
#!/bin/bash

##########
# PRINTS
##########
#echo "Hello, World!"

#############
# VARIABLES
#############
#ABC="abc" #** make sure to not include spaces before or after the assignment (=) sign
#directory=/etc
#echo $ABC $directory

#** Single quotes will treat every character literally.
#** Double quotes will allow you to do substitution (that is include variables within the setting of the value)
#myvar='Hello World'
#echo $myvar
#newvar="More $myvar"
#echo $newvar
#newvar='More $myvar'
#echo $newvar


##########################
# Command Line Arguments
##########################
#cp $1 $2
#echo Details for $2
#ls -lh $2

#########################
# Special Variables
#########################
#$0 - The name of the Bash script.
#$1 - $9 - The first 9 arguments to the Bash script. (As mentioned above.)
#$# - How many arguments were passed to the Bash script.
#$@ - All the arguments supplied to the Bash script.
#$? - The exit status of the most recently run process.
#$$ - The process ID of the current script.
#$USER - The username of the user running the script.
#$HOSTNAME - The hostname of the machine the script is running on.
#$SECONDS - The number of seconds since the script was started.
#$RANDOM - Returns a different random number each time is it referred to.
#$LINENO - Returns the current line number in the Bash script.

###########################
# Command Substitution
###########################
#** take the output of a command or program (what would normally be printed to the screen) and save it as the value of a variable.
#** command should be placed within brackets, preceded by a $ sign.
myvar=$(date -r /home/shadhini/dev/repos/shadhini/python_helpers/bash_utils/hello_world/original.txt)
echo $myvar


############################
# If Statement
############################
#** https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php