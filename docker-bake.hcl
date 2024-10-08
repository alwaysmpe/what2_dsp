group "default" {
    targets = ["foundation", "base-notebook", "minimal-notebook", "juwhat"]
}

target "foundation" {
    context = "https://github.com/jupyter/docker-stacks.git#main:images/docker-stacks-foundation"
    args = {
        PYTHON_VERSION = "3.12"
    }
    tags = ["docker-stacks-foundation:latest"]
}


target "base-notebook" {
    context = "https://github.com/jupyter/docker-stacks.git#main:images/base-notebook"
    contexts = {
        docker-stacks-foundation = "target:foundation"
    }
    args = {
        BASE_CONTAINER = "docker-stacks-foundation"
    }
    tags = ["base-notebook:latest"]
}

target "minimal-notebook" {
    context = "https://github.com/jupyter/docker-stacks.git#main:images/minimal-notebook"
    contexts = {
        base-notebook = "target:base-notebook"
    }

    args = {
        BASE_CONTAINER = "base-notebook:latest"
    }
    tags = ["minimal-notebook:latest"]
}

target "juwhat" {
    context = "./docker/"
    contexts = {
        minimal-notebook = "target:minimal-notebook"
    }
    args = {
        BASE_CONTAINER = "minimal-notebook:latest"
    }

    tags = ["juwhat:latest"]
}
