## runtime.txt

`runtime.txt` is an optional text file that specifies your Dash app's Python runtime 
environment. It must be placed in your app's root directory. The contents are case 
sensitive and must contain include major and minor release, and patch numbers. 

```
python-3.9.0

```

The python runtime used by deployed apps on Dash Enterprise is different from 
the runtime available on Workspaces. Dash Enterprise 4.1.0 and 4.0.1 use `python-3.6.10` 
by default. Workspaces uses `python-3.7.4` and cannot be configured with 
`runtime.txt`.
