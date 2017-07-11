#!/usr/bin/env nextflow

params.str = 'Hello world!'

process splitLetters {

    output:
    val params.str into reciever

    """
    echo $params.str
    """
}


process convertToUpper {
    myFile = file("myfile.txt")


    input:
    val x from reciever

    output:
    val x into result

    """
    cat $x | tr '[a-z]' '[A-Z]'
    """
}

reciever.subscribe {
    println it.trim()
}

result.subscribe{
    println it
}
