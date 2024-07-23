# 0x00. Pagination

## Overview

This project covers the fundamentals of pagination in the context of backend development. You'll learn how to implement various pagination strategies to efficiently handle large datasets.

## Learning Objectives

By the end of this project, you should be able to explain the following without external resources:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Resources

Read or watch:
- [REST API Design: Pagination](https://restfulapi.net/pagination/)
- [HATEOAS](https://restfulapi.net/hateoas/)

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (length will be verified)
- All functions and coroutines must be type-annotated

## Setup

### Data File

Use the `Popular_Baby_Names.csv` data file for your project.