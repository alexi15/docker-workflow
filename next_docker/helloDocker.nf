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
    myfile = file('myfile.txt')
    input:
    val x from reciever

    output:
    stdout result

    """
    myfile.append($x)
    """
}

result.subscribe {
    println it.trim()
}
