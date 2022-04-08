.. _getting_started-user-guide:

==========
User Guide
==========

Ohno is a command line client, wrapper, and Python module for giving you formatted error messages.
If you have a question, find a bug, or want to request a feature!
This is an open source project and we are eager for your contribution. 🎉️

.. _getting_started-user-guide-usage:


Usage
=====

Once you have ``ohno`` installed (:ref:`getting_started-installation`) you
can parse your errors fairly easily, either using ohno as a wrapper or post-run
log parser.

.. _getting_started-user-guide-usage-monitor:


Monitor
-------

To monitor something that might error, you can do:

.. code-block:: console

    $ ohno monitor <command>


We provide a set of failing scripts you can run:


.. code-block:: console

    $ ohno monitor python examples/monitor/failure.py

The output generated (by default) is markdown, and the intention is that you can open a GitHub issue
with versions, system information, and the error message.

.. code-block:: markdown

    ### To Reproduce

    ```bash
    $ python examples/monitor/failure.py
    ```            

    ### Environment

    - Version: Python 3.8.8  
    - Host:
      - architecture: x86_64
      - python-compiler: GCC 7.3.0
      - python-version: 3.8.8
      - cpu-count: 8
      - system: Linux
      - libc: glibc@2.31
  
    ### Errors

    ```bash
    >> 1     error: We cannot do that thing.     2
    ```


Parse
-----

You can also parse an existing log.


.. code-block:: console

    $ ohno monitor python examples/parse/spack-failure.txt


.. code-block:: markdown

    ### To Reproduce
    
    ```bash
    $ <fill in command here>
    ```            

    ### Environment
    
    
    - Host:
      - architecture: x86_64
      - python-compiler: GCC 7.3.0
      - python-version: 3.8.8
      - cpu-count: 8
      - system: Linux
      - libc: glibc@2.31
  
    ### Errors

    ```bash
    >> 2152     configure: error: no BPatch.h found; check path for Dyninst packa
    >> 2154     configure: error: no tau_instrumentor found; check path for PDToo
    >> 2178     configure: error: MPI Correctness Checking support cannot be buil
    >> 2186     configure: error: no f2c.h found; check path for CLAPACK package
    >> 2208     configure: error: no jvmti.h found; check path for JVMTI package
    >> 2238     configure: error: no cuda.h found; check path for CUDA Toolkit fi
    >> 2242     configure: error: no cuda_runtime_api.h found; check path for CUD
    >> 2246     configure: error: no cupti.h found; check path for CUPTI package
    >> 2256     configure: error: no ctool/ctool.h found; check path for CTool pa
    >> 2293     configure: error: no bmi.h found; check path for BMI package firs
    >> 2393     configure: error: no vtf3.h found; check path for VTF3 package fi
    >> 14683    make[4]: *** [mpi_comm_spawn_multiple_f90.lo] Error 1
    >> 14694    make[4]: *** [mpi_testall_f90.lo] Error 1
    >> 14696    make[3]: *** [all-recursive] Error 1
    >> 14698    make[2]: *** [all] Error 2
    >> 14700    make[1]: *** [all-recursive] Error 1
    >> 14702    make: *** [all-recursive] Error 1
    >> 2152     configure: error: no BPatch.h found; check path for Dyninst packa
    >> 2154     configure: error: no tau_instrumentor found; check path for PDToo
    >> 2178     configure: error: MPI Correctness Checking support cannot be buil
    >> 2186     configure: error: no f2c.h found; check path for CLAPACK package
    >> 2208     configure: error: no jvmti.h found; check path for JVMTI package
    >> 2238     configure: error: no cuda.h found; check path for CUDA Toolkit fi
    >> 2242     configure: error: no cuda_runtime_api.h found; check path for CUD
    >> 2246     configure: error: no cupti.h found; check path for CUPTI package
    >> 2256     configure: error: no ctool/ctool.h found; check path for CTool pa
    >> 2293     configure: error: no bmi.h found; check path for BMI package firs
    >> 2393     configure: error: no vtf3.h found; check path for VTF3 package fi
    >> 14686    make[4]: *** [mpi_testsome_f90.lo] Error 1
    >> 14696    make[4]: *** [mpi_testall_f90.lo] Error 1
    >> 14702    make[3]: *** [all-recursive] Error 1
    >> 14704    make[2]: *** [all] Error 2
    >> 14706    make[1]: *** [all-recursive] Error 1
    >> 14708    make: *** [all-recursive] Error 1
    ```
    
The view you see above are the lines extracted that are determined to have meaningful content.

Python Usage
============

If you are working in Python, the same interactions can be done programatically.
Here is how to monitor a command:

.. code-block:: python

    import ohno.main.client as client
    monitor = client.Monitor()
    res = monitor.run(['python', 'monitor/failure.py'])
    print(res.parse())

You can explore the results object:

.. code-block:: python

    res.errors
    res.warnings
    res.to_dict()


And the original command is now a known task to the monitor:


.. code-block:: python

    monitor.tasks
    {'python monitor/failure.py': <ohno.main.executor.shell.ShellExecutor at 0x7fd5541cce50>}
    A task is parsed by a particular kind of result (output) you are interested in:


To do the same but for an error log already generated:

.. code-block:: python

    import ohno.main.client as client
    monitor = client.Monitor()
    res = monitor.load("parse/spack-error.txt")
    print(res.parse())


This library is under development and we will have more documentation coming soon!
