# CLSID-Lookup
CLISID reference sheet. A CLSID is a globally unique identifier that identifies a COM class object. 

Frustrated with not being able to find what applications use what corresponding CLSID , I made this as a nice lookup. Please feel free to fork and contribute missing CLSIDs

Use the python script and raw list to produce a list free of CLSID duplicates (but not application duplicates as same application might use multiple CLSIDs)

# Powershell Command Used: 
```Get-ItemProperty -Path "HKLM:\SOFTWARE\Classes\CLSID\*"|select PSChildName,`(default`) |ft -auto *| clip```

# Refs: 

https://www.linkedin.com/posts/hackingarticles_com-hijackingpdf-activity-6984907816364855297-U4CS  
https://docs.microsoft.com/en-us/windows/win32/com/component-object-model--com--portal  
https://www.systemlookup.com/lists.php?list=1  
https://documentation.help/AutoHotKey-Functions/CLSID-List.htm   
https://www.elevenforum.com/t/list-of-windows-11-clsid-key-guid-shortcuts.1075/   


# Please see also, a tool for looking for vulnerable COM:  
https://github.com/sud0woodo/DCOMrade


Pull Requests Welcome
