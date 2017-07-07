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
    myFile.append(result)

    """
    cd ~/docker-workflow/next_docker
    python hello.py
    """
}

result.subscribe {
    println it.trim()
}
