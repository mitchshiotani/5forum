# 5chan Architecture

## Revision History

| Date | Description | Author
| --- | --- | --- |
| 20201-02-27 | Init | Mush |

## Table of Contents

1. Introduction
  - 1.1 Purpose
  - 1.2 Scope
  - 1.3 Definitions, Acronyms
  - 1.4 References

2. Architectural Representation

3. Architectural Goals and Constraints

4. Use-Case View

5. Logical View

6. Process View

7. Deployment View

8. Size and Performance

99. The rest is here: https://www.ecs.csun.edu/~rlingard/COMP684/Example2SoftArch.htm

## Software Architecture Document

### 1. Introduction

#### 1.1 Purpose

This document is for covering the details on what 5chan is, and will be.
It will go over use cases, and the features that will be built around them.   

#### 1.2 Scope

The document will cover basic use cases and the interactions and flow of data for each of these use cases.  
It will most likely not go over too much about performance. 

### 2. Architectural Representation

### 3. Architectural Goals and Constraints

### 4. Use-Case View

- Login
- View threads (index)
- View thread
```plantuml
@startuml
    skinparam backgroundColor #EEEBDC
    actor User
    User -> index.cgi: click on thread name
    index.cgi -> view_thread.cgi: pass thread id as param
    view_thread.cgi -> User: return html with thread info
@enduml

```
- Create thread
```plantuml
@startuml
    skinparam backgroundColor #EEEBDC
    actor User
    User -> index.cgi: click on 'create thread' button
    index.cgi -> new_thread.cgi: calls to display create thread page
    new_thread.cgi -> User: displays form to create thread
    User -> new_thread.cgi: enters new thread info, clicks submit
    new_thread.cgi --> create_thread.js: js listening for submit, collects form info
    create_thread.js -> create_thread.cgi: pass form info
    database 5chan
    create_thread.cgi -> 5chan: save new thread info
    note over 5chan: could add a feature to show response to user
@enduml
```
- Comment on thread

### 5. Logical View

### 6. Process View

### 7. Deployment View

### 8. Size and Performance
