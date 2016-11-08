# monday-morning-mite

If you track your time in mite https://mite.yo.lk/ and handle tasks in
another system like in our case redmine. Than may the following is
interesting for you. 

    time-entry in mite
    note: #12355 Import dump
    time: 31 minutes

    issue in redmine with id 12355
    estimated time 60 minutes or 1 Story Point
    in case of abstract estimations

Then we calculated the velocity on estimation vs actual time in mite et
voila we know how good the estimation was. Doing this n times we get a
pretty good set of velocities and based on this series we can predict
the future ;)

This is called Evidence-Based Scheduling, or EBS described in this
article http://www.joelonsoftware.com/items/2007/10/26.html

Summary:
* Break your schedule into [...] tasks that can be measured in hours
* Nothing longer than 16 hours
* Individual development tasks are easy to estimate
* Keep track of how long you spend working on each task

* velocity: how fast the task was done relative to estimate.
* collect a series of velocities
* perfect {1, 1, 1, 1, 1, …}
* interesting {0.1, 0.5, 1.7, 0.2, 1.2, 0.9, 13.0}

Everything takes longer than expected, because the estimate didn’t
account for bug fixing, committee meetings, coffee breaks, and that
crazy boss... but there will be a consistent rating.

!!!
* 2) Fix bugs as you find them, and charge the time back to the original task.
* 4) A schedule is a box of wood blocks. 

It is assumed that all other distractions will average out.
