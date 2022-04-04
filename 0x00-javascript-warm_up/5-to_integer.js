#!/usr/bin/node
args = process.argv;
int = parseInt(args[2]);
if (isNaN(int))
{
    console.log("Not a number");
}
else
{
    console.log("My number: " + int)
}

