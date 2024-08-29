group "default" {
    targets = ["foundation", "base-notebook", "minimal-notebook", "juwhat"]
}

target "foundation" {
    context = "./docker/docker-stacks/images/docker-stacks-foundation"
    args = {
        PYTHON_VERSION = "3.12"
    }
    tags = ["docker-stacks-foundation:latest"]
}


target "base-notebook" {
    context = "./docker/docker-stacks/images/base-notebook"
    contexts = {
        foundation = "target:foundation"
    }
    args = {
        BASE_CONTAINER = "docker-stacks-foundation"
    }
    tags = ["base-notebook:latest"]
}

target "minimal-notebook" {
    context = "./docker/docker-stacks/images/minimal-notebook"
    contexts = {
        foundation = "target:foundation"
        base-notebook = "target:base-notebook"
    }

    args = {
        BASE_CONTAINER = "base-notebook:latest"
    }
    tags = ["minimal-notebook:latest"]
}

target "juwhat" {
    context = "./docker/what"
    contexts = {
        foundation = "target:foundation"
        base-notebook = "target:base-notebook"
        minimal-notebook = "target:minimal-notebook"
    }
    args = {
        BASE_CONTAINER = "minimal-notebook:latest"
    }

    tags = ["juwhat:latest"]
}
