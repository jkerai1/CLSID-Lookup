# CLSID-Lookup
CLISID reference sheet. A CLSID is a globally unique identifier that identifies a COM class object.

Frustrated with not being able to find what applications use what corresponding CLSID , I made this as a nice lookup. Please feel free to fork and contribute missing CLSIDs
Refs:
https://www.systemlookup.com/lists.php?list=1
https://documentation.help/AutoHotKey-Functions/CLSID-List.htm
https://www.elevenforum.com/t/list-of-windows-11-clsid-key-guid-shortcuts.1075/

# Powershell Command Used: 
Get-ItemProperty -Path "HKLM:\SOFTWARE\Classes\CLSID\*" `
    |select PSChildName,`(default`) |ft -auto * | clip
